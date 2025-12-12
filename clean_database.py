import sqlite3

# --------------------------------------------------
# Absolute path to your SQLite database file
# --------------------------------------------------
DB_PATH = r'A:\Projects\Employee Performance Analytics\employee_performance.db'

def clear_database():
    # Connect to database using full path
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # --------------------------------------------------
    # Delete all old records
    # --------------------------------------------------
    cursor.execute("DELETE FROM performance")  # Clear performance records
    cursor.execute("DELETE FROM employee")     # Clear employee records

    # Save changes
    conn.commit()

    # Close connection
    conn.close()

    print("Database cleared successfully!")

# --------------------------------------------------
# Only runs when executed directly
# --------------------------------------------------
if __name__ == "__main__":
    clear_database()
