# refresh_data_workflow.py
from airflow.models import DAG
default_args = {
  'owner': 'jdoe',
  'email': 'jdoe@datacamp.com'
}
dag = DAG( 'refresh_data', default_args=default_args )

#etl_workflow.py
from airflow.models import DAG
default_args = {
  'owner': 'jdoe',
  'start_date': '2019-01-01'
}
dag = DAG( dag_id="etl_update", default_args=default_args )
