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
                f"""
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

