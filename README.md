# data_quality_check

Once data not meet expectations requirement it will turn error like this

![image](https://user-images.githubusercontent.com/74217351/159283500-d71e8c33-2069-458a-b590-907d372e65e5.png)

![image](https://user-images.githubusercontent.com/74217351/159284049-e58297dc-3435-487f-a502-e5b5859a32a1.png)


And from Great Expectations dashboard you will find the detailed error

![image](https://user-images.githubusercontent.com/74217351/159284268-cd2faa6d-b54b-4ca0-badc-847cac2f9506.png)


Step by step :
1. `pip install great_expectations airflow-provider-great-expectations>=0.1.0`
2. `great_expectations init -d name_dir`
3. `great_expectations suite new`
4. `great_expectations checkpoint new name_checkpoint name_suite`

Then you can run the DAG file in Airflow
