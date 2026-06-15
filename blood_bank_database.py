import sqlite3

# Create a database connection and a cursor object
conn = sqlite3.connect('blood_bank.db')
cursor = conn.cursor()

# Create tables for donors and blood requests
cursor.execute('''
CREATE TABLE IF NOT EXISTS donors (
    donor_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    blood_type TEXT,
    age INTEGER,
    contact TEXT,
    last_donated DATE
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS blood_requests (
    request_id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_name TEXT,
    blood_type TEXT,
    quantity INTEGER,
    date_requested DATE
);
''')

# Commit the changes and close the connection
conn.commit()
conn.close()
