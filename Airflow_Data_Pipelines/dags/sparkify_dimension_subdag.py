from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators import LoadDimensionOperator 
from helpers import SQLQueries

def load_dimension_subdag(parent_dag_name,
                            task_id,
                            redshift_conn_id,
                            sql_statement,
                            delete_load,
                            table_name,
                            * args, **kwargs):

    dag = DAG(f'{parent_dag_name}.{task_id}')

    load_dimension_tble = LoadDimensionOperator(task_id = task_id,
                                                dag = dag, 
                                                redshift_conn_id=redshift_conn_id,
                                                sql_query = sql_statement,
                                                delete_load = delete_load,
                                                table_name = table_name)
    
    load_dimension_tble

    return dag
