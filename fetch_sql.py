# Fetch SQL Data
import sqlite3
import pandas as pd

def fetch_sql_data():
    # Connect to the existing SQLite database
    conn = sqlite3.connect('employee_performance.db')

    # SQL query to join employee and performance tables
    query = '''
        SELECT 
            e.emp_id,
            e.name,
            e.department,
            p.tasks_completed,
            p.hours_worked
        FROM employee e
        LEFT JOIN performance p 
            ON e.emp_id = p.emp_id
    '''

    # Read query results into a pandas DataFrame
    df = pd.read_sql_query(query, conn)

    # Close the database connection
    conn.close()

    # Return the dataframe
    return df

# --------------------------------------------------
# Execute only if this file is run directly
# --------------------------------------------------
if __name__ == "__main__":
    data = fetch_sql_data()
    print(data)
