import sqlite3

"""
Make SQLITE datbase with two tables.
*** This drops the tables, so will wipe any existing data ***
"""


# Note sqlite looks to lack date data type, so using TEXT here
make_excel_table = """
CREATE TABLE excel_files
(id INTEGER PRIMARY KEY NOT NULL,
filename TEXT NOT NULL,
date_loaded TEXT NOT NULL);
"""

make_payment_table = """
CREATE TABLE payments
(id INTEGER PRIMARY KEY NOT NULL,
file_id INTEGER NOT NULL,
account_number TEXT NOT NULL,
area_of_law TEXT NOT NULL,
amount REAL NOT NULL,
status TEXT NOT NULL,
external_id TEXT,
error_message TEXT,
date_created TEXT,
date_updated TEXT);
"""


with sqlite3.connect('payments.db') as conn:
    conn.execute("drop table if exists excel_files")
    conn.execute("drop table if exists payments")
    conn.execute(make_excel_table)
    conn.execute(make_payment_table)
