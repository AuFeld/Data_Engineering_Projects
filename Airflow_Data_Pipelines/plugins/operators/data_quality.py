from airlfow.hooks.postgres_hook import PostgresHook 
from airflow.models import BaseOperator 
from airflow.utils.decorators import apply_defaults

class DataQualityOperator(BaseOperator):

    ui_color = '#89DA59'

    @apply_defaults
    def __init__(self, 
                redshift_conn_id="",
                tables=[], 
                *args, **kwargs):
        
        super(DataQualityOperator, self).__init__(*args, **kwargs)
        self.redshift_conn_id = redshift_conn_id
        self.tables = tables 

    def execute(self, context):
        redshift_hook = PostgresHok(postgres_conn_id = self.redshift_conn_id)

        for table in self.tables:

            self.log.info(f"Starting data quality validation on table : {table}")
            records = redshift_hook.get_records(f"select count(*) from {table};")

            if len(records) < 1 or len(records[0]) < 1 or records[0][0] < 1: 
                self.log.error(f"Data quality validation FAILED for table : {table}.")
                raise ValueError(f"Data quality validation FAILED for table : {table}")
            self.log.info(f"Data quality validation PASSED on table : {table}")
        
        self.log.info('DataQualityOperator not implemented yet')