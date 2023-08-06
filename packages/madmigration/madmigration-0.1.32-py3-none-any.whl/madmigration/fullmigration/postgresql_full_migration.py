from madmigration.db_operations.operations import DBOperations
from madmigration.utils.logger import configure_logging
from madmigration.fullmigration.full_migration import FullMigrate

logger = configure_logging(__file__)

class PostgresqlFullMigration(FullMigrate):
    def __init__(self, source_db_operations: DBOperations, destination_db_operations: DBOperations):
        super().__init__(source_db_operations, destination_db_operations)

    def collect_all_schemas_from_source_database(self):
        self.schemas = self.source_db_operations.get_all_schemas()
        self.schemas = ['_admin', '_finance', 'dwh_metrics']

    def clone_database(self):
        for schema in self.schemas:
            if schema in self.EXCLUDED_SCHEMAS:
                continue
            logger.info(f'Creating schema {schema}...')

            self.destination_db_operations.create_schema(schema)

            source_db_metadata = self.source_db_operations.get_reflected_metadata_of_schema(schema=schema)
            self.destination_db_operations.create_all_tables_with_metadata(source_db_metadata)

    def drop_all_tables_constraints_in_destination_db(self):
        for schema in self.schemas:
            if schema in self.EXCLUDED_SCHEMAS:
                continue

            tables = self.destination_db_operations.get_all_tables(schema=schema)
        
            for table in tables:
                fks = self.destination_db_operations.get_foreign_keys_constraints(table.name, schema=schema)
                if not fks:
                    logger.info(f'Foreign Key not found for table {table} in schema {schema}')
                    continue
                for fk in fks:
                    self.destination_db_operations.drop_constraint(fk['name'], table.name, 'foreignkey', schema=schema)

    def copy_data_from_source_to_destination(self):
        for schema in self.schemas:
            if schema in self.EXCLUDED_SCHEMAS:
                continue
        
            tables = self.source_db_operations.get_all_tables(schema=schema)

            for table in tables:
                yield_data = self.source_db_operations.query_data_from_table(table)
                for data in yield_data:
                    self.destination_db_operations.insert_data(table_name=table.fullname, data=data._asdict(), schema=schema)