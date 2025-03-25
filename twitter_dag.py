from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago
from datetime import timedelta
from twitter_etl import run_etl_pipeline


default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2025, 3, 26),
    'email': ['airflow@example.com'],
    'email_on_failuer': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1)
}

dag = DAG(
    'twitter_dag',
    default_args=default_args,
    description='ETL pipeline for Twitter Data'
)

run_etl = PythonOperator(
    task_id = 'complete_twitter_etl',
    python_callable = run_etl_pipeline,
    dag=dag,
)

run_etl