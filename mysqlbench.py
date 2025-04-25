import mysql.connector
from concurrent.futures import ThreadPoolExecutor
import time

# Database connection details
DB_CONFIG = {
    'host': 'your_host',  # Your MySQL host (e.g., 'localhost')
    'user': 'your_username',  # Your MySQL username
    'passwd': 'your_password',  # Your MySQL password
}

QPS = 600  # Queries per second
INTERVAL = 1 / QPS  # Interval between each query
MAX_WORKERS = 50  # Maximum number of threads in the pool

def run_procedure(db_name):
    try:
        conn = mysql.connector.connect(
            host=DB_CONFIG['host'],
            user=DB_CONFIG['user'],
            passwd=DB_CONFIG['passwd'],
            database=db_name
        )
        cursor = conn.cursor()

        # Drop tables
        cursor.execute("DROP TABLE IF EXISTS your_table1;")
        cursor.execute("DROP TABLE IF EXISTS your_table2;")

        # Create tables
        cursor.execute("CREATE TABLE your_table1 (id INT PRIMARY KEY, name VARCHAR(50));")
        cursor.execute("CREATE TABLE your_table2 (id INT PRIMARY KEY, value VARCHAR(50));")

        # Execute your queries and stored procedure calls
        cursor.execute("INSERT INTO your_table1 (id, name) VALUES (1, 'test1');")
        cursor.execute("INSERT INTO your_table2 (id, value) VALUES (1, 'value1');")
        cursor.callproc('your_procedure1', (param1, param2))  # Adjust as per your procedure
        cursor.callproc('your_procedure2', (param1, param2))  # Adjust as per your procedure

        conn.commit()
        cursor.close()
        conn.close()
        print(f"Procedure executed on {db_name}")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    except Exception as e:
        print(f"Unexpected error: {e}")

# List of your database names
databases = ['test1', 'test2', 'test3', 'test4', 'test6', 'test7', 'test9', 'test10']

def run_queries_at_qps():
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        while True:
            futures = []
            start_time = time.time()
            for db_name in databases:
                futures.append(executor.submit(run_procedure, db_name))
                time.sleep(INTERVAL)
            for future in futures:
                future.result()  # Wait for all threads to complete
            end_time = time.time()
            elapsed_time = end_time - start_time
            print(f"Batch executed in {elapsed_time:.2f} seconds")

if __name__ == "__main__":
    run_queries_at_qps()
