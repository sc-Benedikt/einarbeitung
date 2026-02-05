import sqlite3, flask, math
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
command5 = "UPDATE infos SET big_header = 'Cities' WHERE big_header = 'Citys'"







text = "ich mag autos"

#cursor.execute("ALTER TABLE infos DROP COLUMN small_header_4s")
connection.commit()

def get_data(data):
    cursor.execute(f"SELECT {data} FROM infos WHERE info_id = 1")
    daten = cursor.fetchall()
    return daten



with open ("/home/git_repo/einarbeitung/05_Webentwicklung/templates/info_site.html") as f:
    data = f.read()
print (len(data))

if len(data) <= 1693:
    print("ja")

a = 9 / 2
float(a)
print(math.floor(a))

anzahl_spalten = math.floor(float(len(connection.execute("PRAGMA table_info(infos)").fetchall())))




print(anzahl_spalten)

# cursor.execute("DROP TABLE IF EXISTS infos")

# cursor.execute(command1)

# cursor.execute("""
# INSERT INTO infos (
#     info_id, big_header,
#     small_header_1, info_text_1,
#     small_header_2, info_text_2,
#     small_header_3, info_text_3
# ) VALUES (?, ?, ?, ?, ?, ?, ?, ?);
# """, [
#     1, "Citys", "London", "blablabla", "Berlin", "serdftgz", "Paris", "grr le alemans",
  
 
# ])

# connection.commit()

cursor.execute("UPDATE infos SET big_header = 'Cities' WHERE big_header = 'Citys'")

connection.commit()
print("fertig")
