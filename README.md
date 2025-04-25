Running the Script:

Update DB_CONFIG with your actual connection details.

Replace the placeholder queries in run_procedure with your actual SQL queries.

Save the script to a file (e.g., run_procedure_qps.py) and run it from your terminal or command prompt:


QPS Management:

The run_queries_at_qps function aims to achieve 600 QPS by controlling the interval between each query execution.

The ThreadPoolExecutor is used to manage concurrent executions with a maximum number of threads controlled by MAX_WORKERS.


QUERIES:

Update the queries based on your need .You can use your actual queries from your application
