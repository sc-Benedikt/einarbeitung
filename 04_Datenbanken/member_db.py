import sqlite3, json
from base import *

conn = sqlite3.connect("0_base.db")
cursor = conn.cursor()

with open("/home/git_repo/einarbeitung/base.json", "r", encoding="utf-8") as data:
    all_squads = json.load(data)



def creat_db_members():
  
        cursor.execute(
            """
        CREATE TABLE IF NOT EXISTS members (
        member_id INTEGER PRIMARY KEY,
        member_name TEXT,
        member_age TEXT,
        member_secretIdentity TEXT,
        Squad_from_member INTEGER,
        FOREIGN KEY (squad_from_member) REFERENCES squads(squad_id)
        )
        """
        )

     

        for squad in all_squads:
            for personal_details in squad.get("members"):
                
                cursor.execute("""
                SELECT squad_id FROM squads WHERE squadName = ?
                """, (squad.get("squadName"),))
                suqad_id = cursor.fetchall()[0][0]

                cursor.execute(
                    f"""
                    INSERT INTO members 
                    (member_name, member_age, member_secretIdentity, squad_from_member)
                    VALUES 
                    (?, ?, ?, ? )
                    """,
                    (personal_details.get("name"),
                    personal_details.get("age"),
                    personal_details.get("secretIdentity"),
                    suqad_id
                    )
                )
        conn.commit()
       





