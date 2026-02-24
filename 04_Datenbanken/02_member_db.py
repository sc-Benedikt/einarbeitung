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


def creat_db_members():
    if check_tabelle_true("members") == False:
        cursor.execute(
            """
        CREATE TABLE IF NOT EXISTS members (
        member_id INTEGER PRIMARY KEY
        )
        """
        )

        members = all_squads[0].get("members")

        for k in members[0]:
            cursor.execute(
                f"""
            ALTER TABLE members ADD COLUMN {k};
            """
            )
            conn.commit()




def add_values():
    for squad in all_squads:
        for charact in squad.get("members"):
            charact_string = json.dumps(charact.get("powers"))

            

            cursor.execute(
                f"""
                INSERT INTO members 
                (name, age, secretIdentity, powers)
                VALUES 
                (?, ?, ?, ?)
                """,
                (charact.get("name"),
                charact.get("age"),
                charact.get("secretIdentity"),
                charact_string
                )
            )

    conn.commit()


creat_db_members()
add_values()
