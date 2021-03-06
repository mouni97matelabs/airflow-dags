from datetime import datetime
from airflow import DAG
import time
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator

def print_hello():
 time.sleep(10)
 return 'Hello Wolrd'

dag = DAG('hello_world', description='Hello world example', schedule_interval='0 12 * * *', start_date=datetime(2020, 9, 16), catchup=False)

dummy_operator = DummyOperator(task_id='dummy_task', retries = 3, dag=dag)

hello_operator = PythonOperator(task_id='hello_task', python_callable=print_hello, dag=dag)

dummy_operator >> hello_operator
