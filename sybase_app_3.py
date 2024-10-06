import os
import pyodbc

# Retrieve credentials from environment variables
username = os.environ['SYBASE_USERNAME']
password = os.environ['SYBASE_PASSWORD']

# Sybase connection details
server = 'sybase_server'
database = 'database'

# Construct the connection string
conn_str = (
    f"DRIVER={{FreeTDS}};"
    f"SERVER={server};"
    f"DATABASE={database};"
    f"UID={username};"
    f"PWD={password};"
)

try:
    # Establish connection
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()

    # Execute a simple query
    cursor.execute("SELECT TOP 5 * FROM sample_table")

    # Fetch and print results
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Close connection
    cursor.close()
    conn.close()

    print("Query executed successfully!")
except Exception as e:
    print(f"An error occurred: {e}")