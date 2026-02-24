import sqlite3
conn = sqlite3.connect("0_base.db")
cursor = conn.cursor()

def check_tabelle_true(tabellen_name):

    if cursor.execute(f"SELECT * FROM {tabellen_name} LIMIT 0"):
        return True
    else:
        return False
    
if check_tabelle_true("members"):
    print("true")
else:
    print("false")