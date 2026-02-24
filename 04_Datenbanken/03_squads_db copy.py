import sqlite3, json

conn = sqlite3.connect("0_base.db")
cursor = conn.cursor()

with open("/home/git_repo/einarbeitung/base.json", "r", encoding="utf-8") as data:
    all_squads = json.load(data)


def check_tabelle_true(tabellen_name):
    try:
        if cursor.execute(f"SELECT * FROM {tabellen_name} LIMIT 0"):
            return True
        else:
            return False
    except:
        return False

def creat_db_squads():
    if check_tabelle_true("squads") == False:
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
        conn.commit()


def add_values():
    if check_tabelle_true("squads") == False: 
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


creat_db_squads()
add_values()
