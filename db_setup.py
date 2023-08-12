import sqlite3

def create_database():
    conn = sqlite3.connect('utility_data.db')
    conn.close()

def create_utility_records():
    conn = sqlite3.connect('utility_data.db')
    cursor = conn.cursor()
    
    # Create the table if it doesn't exist
    cursor.execute('''CREATE TABLE IF NOT EXISTS utility_records
                      (id INTEGER PRIMARY KEY AUTOINCREMENT,
                       utility_type TEXT,
                       year INTEGER,
                       month TEXT,
                       amount REAL)''')
    
    conn.commit()
    conn.close()

def update_utility_records(utility_type, year, month, amount):
    conn = sqlite3.connect("utility_data.db")
    cursor = conn.cursor()

    # Update data in the table
    cursor.execute('''
        UPDATE utility_records
        SET amount = ?
        WHERE utility_type = ? AND year = ? AND month = ?
    ''', (amount, utility_type, year, month))

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
