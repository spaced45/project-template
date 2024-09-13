import sqlite3

# Connect to the database (or create it if it doesn't exist)
conn = sqlite3.connect('./data/project_data.db')
cursor = conn.cursor()

# Create the table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        age INTEGER,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP
    )
''')

# Insert dummy data into the table
cursor.execute('''
    INSERT INTO users (name, email, age) 
    VALUES 
    ('Alice Johnson', 'alice@example.com', 25),
    ('Bob Smith', 'bob@example.com', 30),
    ('Charlie Brown', 'charlie@example.com', 22)
''')

# Commit the changes and close the connection
conn.commit()
conn.close()
