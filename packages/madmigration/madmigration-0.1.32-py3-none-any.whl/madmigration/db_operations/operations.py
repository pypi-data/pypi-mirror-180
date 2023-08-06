from sqlalchemy import create_engine, inspect, Table, MetaData, ForeignKeyConstraint
from sqlalchemy.orm import Session
from sqlalchemy.exc import ProgrammingError, NoSuchTableError
from sqlalchemy.engine import reflection
from sqlalchemy.engine.url import make_url
from sqlalchemy.schema import DropConstraint, DropTable

from sqlalchemy_utils.functions.database import database_exists, create_database

from madmigration.utils.logger import configure_logging
from madmigration.utils.helpers import goodby_message, database_not_exists

from alembic.migration import MigrationContext
from alembic.operations import Operations

from contextlib import contextmanager

import sys
from typing import Optional

logger = configure_logging(__name__)

 
@contextmanager
def OperationContextManager(engine):
    conn = engine.connect()
    ctx = MigrationContext.configure(conn)
    op = Operations(ctx)
    yield op
    conn.close()

@contextmanager
def InspectorReflection(engine):
    inspector = reflection.Inspector.from_engine(engine)
    yield inspector

@contextmanager
def Transaction(engine):
    conn = engine.connect()
    transactional = conn.begin()
    yield transactional
    conn.close()


class DBOperations:
    def __init__(self, uri, create_database=False):
        try:
            self.uri = uri
            self.password_masked_database_uri = make_url(self.uri)

            if create_database:
                self.create_database_if_not_exists()

            self.engine = create_engine(uri, echo=False)
            self.session = Session(self.engine, autocommit=False, autoflush=False)
            
            self.metadata = MetaData(bind=self.engine)
            self.metadata.reflect(self.engine)

            self.inspector = reflection.Inspector.from_engine(self.engine)

        except Exception as err:
            logger.error(err)
            sys.exit(1)

    @contextmanager
    def reflected_metadata(self, schema=None):
        if schema:
            logger.info(f'Reflecting schema {schema}')
        else:
            logger.warn(f'Reflecting empty schema {schema}')

        self.metadata.clear()
        self.metadata.reflect(schema=schema)
        yield self.metadata
    

    def check_if_database_exists(self):
        return True if database_exists(self.uri) else False
            
    def create_database_if_not_exists(self, check_for_database: callable = database_exists):
        if check_for_database(self.uri):
            logger.error("Database exists in destination. Please remove before beginning migration!")
            sys.exit(1)
        else:
            while True:
                msg = input(f"The database {self.password_masked_database_uri} does not exists, would you like to create it in the destination?(y/n) ")
                if msg.lower() == "y":
                    try:
                        create_database(self.uri)
                        logger.info(f"Database {self.password_masked_database_uri} created..")
                        break
                    except Exception:
                        goodby_message(database_not_exists(self.uri), 1)
                elif msg.lower() == "n":
                    goodby_message("Destination database does not exist \nExiting ...", 0)
                print("Please, select command")

    def drop_table(self, table_name):
        with OperationContextManager(self.engine) as op:
            op.drop_table(table_name)
            logger.info(f"Table {table_name} dropped")

    def bulk_drop_tables(self, *table_name):
        try:
            for tb in table_name:
                self.drop_table(tb)
            return True
        except Exception as err:
            logger.error(err)
            sys.exit(1)

    def update_column(self, table_name, column_name, col_type, **options):            
        with OperationContextManager(self.engine) as op:
            op.alter_column(table_name, column_name,type_=col_type,postgresql_using=f"{column_name}::{col_type}") #FIXME not working

    def create_table(self, table_name: str, *columns) -> bool:
        with OperationContextManager(self.engine) as op:
            op.create_table(table_name, *columns)

        logger.info(f"Table {table_name} is created")


    def add_column(self, table_name: str, *column) -> bool:
        with OperationContextManager(self.engine) as op:
            for col in column:
                op.add_column(table_name, col)
            logger.info(f"Columns {column} added into table {table_name}")


    def create_fk_constraint(self, fk_constraints: list, const_columns: dict) -> bool:
        """ Get list of foreign keys from static list `fk_constraints` and create it  """
        with OperationContextManager(self.engine) as op:
            for constraint in fk_constraints:
                dest_table_name = constraint.pop("table_name")
                column_name = constraint.pop("column_name")
                source_table = constraint.pop("source_table")
                dest_column = constraint.pop("dest_column")
                temp = [i for i in const_columns[source_table]]
                if not dest_column in temp:
                    op.create_foreign_key(
                        None,
                        source_table,
                        dest_table_name,
                        [dest_column],
                        [column_name],
                        **constraint,
                    )

    def drop_fk(self, fk_constraints):
        with OperationContextManager(self.engine) as op:
            for fk in fk_constraints:
                op.drop_constraint(fk[1], fk[0], type_="foreignkey")
                logger.info(f"Dropped foreign key constraint {fk}")


    def db_drop_everything(self):
        """ From http://www.sqlalchemy.org/trac/wiki/UsageRecipes/DropEverything """
        tables = []
        all_foreign_keys = []
        with InspectorReflection(self.engine) as inspector: 
            for table_name in inspector.get_table_names():
                fks = []
                for fk in inspector.get_foreign_keys(table_name):
                    if not fk["name"]:
                        continue
                    fks.append(ForeignKeyConstraint((), (), name=fk["name"]))
                t = Table(table_name, self.metadata, *fks)
                tables.append(t)
                all_foreign_keys.extend(fks)
            
        with self.engine.connect() as conn:
            for foreignkey in all_foreign_keys:
                conn.execute(DropConstraint(foreignkey))

            for table in tables:
                conn.execute(DropTable(table))

    def collect_fk_and_constraint_columns(self, table_list, schema=None):
        """ 
        Collect foreign key constraints for tables
        """
        dest_fk = {}
        contraints_columns = {}

        with InspectorReflection(self.engine) as inspector:
            try:
                for table_name in inspector.get_table_names(schema=schema):
                    __table = f'{schema}.{table_name}'
                    if __table in table_list:
                        for fk in inspector.get_foreign_keys(table_name):
                            if not fk["name"]:
                                continue
                            dest_fk[fk["referred_table"]].append((__table, fk["name"]))
                            contraints_columns[table_name].append(*fk["constrained_columns"])
            except Exception as err:
                logger(err)
                sys.exit()

        return dest_fk, contraints_columns

    def is_column_exists_in_table(self, table_name: str, column_name: str) -> bool:
        with InspectorReflection(self.engine) as inspector:
            columns = inspector.get_columns(table_name)
            for col in inspector.get_columns(table_name):
                if column_name in col["name"]:
                    return True
            return False

    def is_table_exists(self, table_name: str) -> bool:
        """Check table exist or not"""
        return table_name in self.get_all_tables_names()

    def insert_data(self, table_name, data: dict, schema=None):
        table = self.get_table_attribute_from_base(table_name, schema=schema)
        try:
            logger.info(f"Inserting data into table {table_name}")
            stmt = table.insert().values(**data)
        except Exception as err:
            logger.error(err, exc_info=True)
            sys.exit(1)
        self.execute_stmt(stmt=stmt)

    def execute_stmt(self, stmt):
        try:
            with self.engine.connect() as connection:
                connection.execute(stmt)
        except Exception as err:
            logger.error(err)

    def query_data_from_table(self, table_name, yield_per=1):
        logger.info(f'Quering data from table {table_name}')
        return self.session.query(table_name).yield_per(yield_per)


    def get_table_attribute_from_base(self, source_table_name: str, schema=None):
        try:
            with self.reflected_metadata(schema=schema) as metadata:
                return metadata.tables.get(source_table_name)
        except AttributeError as err:
            logger.error(err)
            sys.exit(1)

    def get_all_schemas(self):
        insp = inspect(self.engine)
        return insp.get_schema_names()

    def get_all_tables(self, schema=None):
        with self.reflected_metadata(schema=schema) as metadata:
            return list(metadata.tables.values())

    def get_table(self, table_name, schema=None):
        tables = self.get_all_tables(schema=schema)
        __table = f'{schema}.{table_name}'
        try:
            return tables[__table]
        except KeyError as err:
            logger.error(f"Table {table_name} not found", err)

    def get_all_tables_names(self):
        tables = self.get_all_tables()
        return [table for table in tables]

    def get_table_constraints(self, table):
        return table.constraints

    def get_table_columns(self, table):
        return table.columns.values()

    def drop_constraint(self, constraint_name, table_name, constraint_type, schema=None):
        with OperationContextManager(self.engine) as op:
            try:
                op.drop_constraint(constraint_name, table_name, type_=constraint_type, schema=None)
            except ProgrammingError as err:
                logger.error(err)

    def test_set_fk(self, constraint_name, table_name):
        with OperationContextManager(self.engine) as op:
            try:
                print(help(op.create_check_constraint))
                # op.create_check_constraint(constraint_name, table_name)
            except Exception as err:
                logger.error(err)

    def get_foreign_keys_constraints(self, table_name, schema=None) -> Optional[list[dict]]:
        """ 
        Collect foreign key constraints for tables
        """
        try:
            return self.inspector.get_foreign_keys(table_name, schema=schema)
        except NoSuchTableError as err:
            logger.error(f'Table {table_name} not found in schema {schema}', exc_info=True)

    def create_all_tables_with_metadata(self, metadata):
        logger.info(f"Creating metadata in destination database {self.engine.url}")
        metadata.create_all(bind=self.engine)

    def create_schema(self, schema: str):
        with self.engine.connect() as conn:
            logger.info(f'Creating schema if not exists {schema} in {self.engine.url}')
            conn.execute(f'CREATE SCHEMA IF NOT EXISTS {schema}')

    def get_reflected_metadata_of_schema(self, schema):
        with self.reflected_metadata(schema=schema) as metadata:
            return metadata

