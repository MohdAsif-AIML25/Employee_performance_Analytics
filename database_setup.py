import sqlite3

def setup_database():
    # Connect to (or create) the SQLite database file.
    conn = sqlite3.connect('employee_performance.db')

    # Create a cursor object to execute SQL commands.
    cursor = conn.cursor()

    # ----------------------------------------------------
    # Create the employee table (if it does not exist yet)
    # ----------------------------------------------------
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS employee(
            emp_id INTEGER PRIMARY KEY,
            name TEXT,
            department TEXT
        )
    ''')

    # ---------------------------------------------------------
    # Create the performance table (if it does not exist yet)
    # ---------------------------------------------------------
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS performance(
            perf_id INTEGER PRIMARY KEY,
            emp_id INTEGER UNIQUE,
            tasks_completed INTEGER,
            hours_worked REAL,
            FOREIGN KEY(emp_id) REFERENCES employee(emp_id)
        )
    ''')

    # ----------------------------------------------------
    # Insert sample employee data
    # ----------------------------------------------------
    # Using OR IGNORE prevents the operation from failing
    # if the record already exists.
    employee = [
        (1, 'Alice', 'Engineering'),
        (2, 'Bob', 'Marketing'),
        (3, 'Charile', 'HR')
    ]
    cursor.executemany(
        'INSERT OR IGNORE INTO employee VALUES (?, ?, ?)',
        employee
    )

    # ----------------------------------------------------
    # Insert sample performance data
    # ----------------------------------------------------
    # Only emp_id is provided because perf_id auto-increments.
    performance = [
        (1, 10, 40),
        (2, 8, 35),
        (3, 5, 30)
    ]
    cursor.executemany(
        'INSERT OR IGNORE INTO performance (emp_id, tasks_completed, hours_worked) VALUES (?, ?, ?)',
        performance
    )

    # Save (commit) all changes to the database
    conn.commit()

    # Close the database connection
    conn.close()

if __name__ == '__main__':
    setup_database()
    print("Database Setup complete!....")
