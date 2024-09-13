import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('./data/project_data.db')
cursor = conn.cursor()

# SQL commands to drop tables
drop_tables_sql = '''
    DROP TABLE IF EXISTS test_table;
    DROP TABLE IF EXISTS users;
'''

# Execute the SQL commands
cursor.executescript(drop_tables_sql)

# Commit the changes
conn.commit()

# Close the connection
conn.close()

print("Tables 'test_table' and 'users' have been deleted.")
