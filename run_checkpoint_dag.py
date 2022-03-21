import os
import great_expectations as ge
from airflow import DAG
from great_expectations_provider.operators.great_expectations import GreatExpectationsOperator
from airflow.operators.dummy import DummyOperator
from datetime import datetime

# Define Great Expectations project path
path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), "data_quality", "great_expectations")


with DAG(
        dag_id="data_quality_validation",
        start_date=datetime(2022, 3, 15),
        catchup=False,
        schedule_interval=None
) as dag:

    start = DummyOperator(
        task_id="start"
    )

    run_quality_check = GreatExpectationsOperator(
        task_id="run_quality_check",
        data_context_root_dir=path, # Great Expectations project path
        checkpoint_name="my_checkpoint" # Name checkpoint that want to run

    )

    end = DummyOperator(
        task_id="end"
    )

start >> run_quality_check >> end
