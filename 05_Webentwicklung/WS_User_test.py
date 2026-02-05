import sqlite3, flask
from flask import session


connection = sqlite3.connect("/home/git_repo/einarbeitung/05_Webentwicklung/User_Infos.db")

cursor = connection.cursor()

command1 = """CREATE TABLE IF NOT EXISTS
    infos(info_id INTEGER PRIMARY KEY AUTOINCREMENT, big_header TEXT, 
    small_header_1 TEXT, info_text_1 TEXT, 
    small_header_2 TEXT, info_text_2 TEXT, 
    small_header_3 TEXT, info_text_3 TEXT)"""

command2 = ("INSERT INTO INFOS (big_header, small_header_1, info_text_1, small_header_2, info_text_2, small_header_3, info_text_3) VALUES (?, ?, ?, ?, ?, ?, ?)")
values = ('Personen', 'Daniil', 'uw iach', 'Nelson', 'Free nelson', 'Philipp', 'asdfghjklö')
command3 = "SELECT big_header FROM infos"
command5 = "asd"







text = "ich mag autos"

cursor.execute(f"UPDATE infos SET info_text_1 = '{text}' WHERE info_id = 1 ")
connection.commit()

def get_data(data):
    cursor.execute(f"SELECT {data} FROM infos WHERE info_id = 1")
    daten = cursor.fetchall()
    return daten

print("fertig")




# for i in range(5):
#     cursor.execute(f"SELECT * FROM users WHERE acc_id = {i}")
#     result = cursor.fetchall()
#     print(result)

# connection.commit()
