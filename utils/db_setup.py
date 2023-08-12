import sqlite3

# Create a connection and cursor
conn = sqlite3.connect("utility_data.db")
cursor = conn.cursor()

# Create the table to store utility records
cursor.execute('''
    CREATE TABLE IF NOT EXISTS utility_records (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        utility_type TEXT,
        month TEXT,
        amount REAL
    )
''')

# Commit changes and close the connection
conn.commit()
conn.close()

def insert_utility_record(utility_type, month, amount):
    conn = sqlite3.connect("utility_data.db")
    cursor = conn.cursor()

    # Insert data into the table
    cursor.execute('''
        INSERT INTO utility_records (utility_type, month, amount)
        VALUES (?, ?, ?)
    ''', (utility_type, month, amount))

    # Commit changes and close the connection
    conn.commit()
    conn.close()

def get_utility_records():
    conn = sqlite3.connect("utility_data.db")
    cursor = conn.cursor()

    # Retrieve data from the table
    cursor.execute('SELECT * FROM utility_records')
    records = cursor.fetchall()

    # Close the connection
    conn.close()

    return records
