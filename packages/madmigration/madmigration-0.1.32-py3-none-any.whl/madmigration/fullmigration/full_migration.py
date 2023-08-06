from madmigration.db_operations.operations import DBOperations
from madmigration.utils.logger import configure_logging

logger = configure_logging(__file__)


class FullMigrate:
    def __init__(self, source_db_operations: DBOperations, destination_db_operations: DBOperations):
        self.source_db_operations = source_db_operations
        self.destination_db_operations = destination_db_operations
        self.EXCLUDED_SCHEMAS = ['information_schema']

    def run(self):
        self.collect_all_schemas_from_source_database()
        self.clone_database()
        self.drop_all_tables_constraints_in_destination_db()
        self.copy_data_from_source_to_destination()

    def collect_all_schemas_from_source_database(self):
        "This function is written for postgresql"
        pass

    def clone_database(self):
        pass

    def drop_all_tables_constraints_in_destination_db(self):
        pass

    def copy_data_from_source_to_destination(self):
        pass
