import os.path
import time
import sqlite3

# Below needed so database file is still found when this module imported 
# into app in directory above 
# https://stackoverflow.com/questions/28126140/python-sqlite3-operationalerror-no-such-table
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
database_name= os.path.join(BASE_DIR, "payments.db")


def add_file(filename):
    existing_filenames = get_filenames()
    if filename not in existing_filenames:
        key = record_file(filename)
    else:
        key = None
        print(f"file '{filename}' already loaded")
    return key
    

def record_file(filename):
    # The integer primary key works automatially  - no need to set
    sql = """
    insert into excel_files(filename, date_loaded)
    values(?,?)
    """
    params = [filename, time.strftime("%d-%b-%Y %H:%M:%S")]
    with sqlite3.connect(database_name) as conn:
        # Note sqlite cursor doesn't support context manager, so no `with conn.cursor ...`
        cursor = conn.cursor()
        cursor.execute(sql, params)
        generated_key = cursor.lastrowid
        conn.commit()
    return generated_key


def record_payments(file_id, rows):
    success_count = 0
    for row in rows:
        if len(row) < 5 or row[0] == "LSC Account Number":
            continue
        account_number = row[0]
        area_of_law = row[1]
        amount = row[4]
        key = record_payment(file_id, account_number, area_of_law, amount)
        if key:
            success_count += 1
    return success_count


def record_payment(file_id, account_number, area_of_law, amount):
    sql = """
    insert into payments(file_id, account_number, area_of_law, amount, status, date_created)
    values(?,?,?,?,?,?)
    """
    params = [file_id, account_number, area_of_law, amount, "New", time.strftime("%d-%b-%Y %H:%M:%S")]
    with sqlite3.connect(database_name) as conn:
        cursor = conn.cursor()
        cursor.execute(sql, params)
        generated_key = cursor.lastrowid
        conn.commit()
    return generated_key



def get_filenames():
    rows = run_query("select filename from excel_files")
    filenames = [e[0] for e in rows]
    return filenames


def get_file_details():
    rows = run_query("select * from excel_files")
    return rows

def get_payment_details():
    rows = run_query("select * from payments")
    return rows


def run_query(sql, params=()):
    with sqlite3.connect(database_name) as conn:
        cursor = conn.cursor()
        cursor.execute(sql, params)
        rows = cursor.fetchall()
    return rows



if __name__ == "__main__":
    #key = add_file("mangrove12")
    #filenames = run_query("select * from excel_files")
    #print("key", key)
    #print(filenames)
    key = record_payment(1, "0G935M", "CIVIL", 123.45)
