# uruchomienie programu w terminalu: python src/database.py

import sqlite3

connection = sqlite3.connect("data/minicrm.db")

cursor = connection.cursor()

create_clients_table = """

CREATE TABLE IF NOT EXISTS clients 
(
    id INTEGER PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    phone_number TEXT,
    email TEXT,
    note TEXT
);

"""

cursor.execute(create_clients_table)

show_tables_query = """ 

SELECT name
FROM sqlite_master
WHERE name='abc123';

"""
cursor.execute(show_tables_query)

result = cursor.fetchone()
if result is None:
    print("Nie znaleziono wyniku")
else:
    print(result[0])

connection.commit()

connection.close()