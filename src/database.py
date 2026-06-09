
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

connection.commit()

connection.close()