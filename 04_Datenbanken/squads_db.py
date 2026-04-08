import sqlite3, json
from base import *

conn = sqlite3.connect("0_base.db")
cursor = conn.cursor()

with open("/home/git_repo/einarbeitung/base.json", "r", encoding="utf-8") as data:
    all_squads = json.load(data)



def creat_db_squads():
        cursor.execute(
            """
        CREATE TABLE IF NOT EXISTS squads (
        squad_id INTEGER PRIMARY KEY
        )
        """
        )

        for k in all_squads[0]:
            cursor.execute(
                f"""
            ALTER TABLE squads ADD COLUMN {k} TEXT
            """
            )
  

        for squad in all_squads:
            cursor.execute(
                """
                INSERT INTO squads 
                (squadName, homeTown, formed, status, secretBase, active, members) 
                VALUES 
                (?, ?, ?, ?, ?, ?, ?)
                """,
                (squad.get("squadName"),
                squad.get("homeTown"),
                squad.get("formed"),
                squad.get("status"),
                squad.get("secretBase"),
                squad.get("active"),
                len(squad.get("members"))
                )
            )
        conn.commit()

def add_squad():
    name = input("name: ")
    town = input("home Town: ")
    formed = input("formed in: ")
    status = input("status(good, neutral, evil): ")
    base = input("secret Base: ")
    aktive = input("aktiv(1 = yes, 0 = no):")
    member = input("member count:")
    cursor.execute(
        """
    INSERT INTO squads (squadName, homeTown, formed, status, secretBase, active, members)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """,
        (
            name,
            town,
            formed,
            status,
            base,
            aktive,
            member,
        ),
    )

def show_squad():

    cursor.execute(
        """
    SELECT squadName
    FROM squads
    """
    )
    squads = cursor.fetchall()
    for i in squads:
        print(i[0])

def remove_squad():
    show_squad()

    which_squad = input("->")

    cursor.execute("""
    SELECT squad_id
    FROM squads
    WHERE LOWER(squadNAME) = LOWER(?)
    """, (which_squad,))

    id_from_del_squad = int(cursor.fetchall()[0][0])

    cursor.execute("""
    DELETE FROM squads 
    WHERE squad_id = (?)
    """, (id_from_del_squad,))

    cursor.execute("""
    DELETE FROM members
    WHERE Squad_from_member = (?)
    """, (id_from_del_squad,))

