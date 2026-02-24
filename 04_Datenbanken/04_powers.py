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
 
        cursor.execute(
            """
        CREATE TABLE IF NOT EXISTS powers (
        power_id INTEGER PRIMARY KEY,
        power_name TEXT
        )
        """
        )

def add_values():
   if check_tabelle_true("powers") == False:
        powers_check_list = []

        for squad in all_squads:
            for member in squad.get("members"):
                for power in member.get("powers"):

                    if power not in powers_check_list:

                        print(power, type(power))
                        cursor.execute(
                        """
                        INSERT INTO powers (power_name) VALUES (?);
                        """, 
                        (power,)
                        )
                        powers_check_list.append(power)
                        conn.commit()

def power_to_member():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS power_member (
    member_id INTEGER,
    power_id INTEGER,
    FOREIGN KEY(member_id) REFERENCES member(member_id)
    FOREIGN KEY(power_id) REFERENCES power(power_id)
                   )
""")
              
    for squad in all_squads:
        for member in squad.get("members"):
            for power in member.get("powers"):
                cursor.execute(f"""
                SELECT power_id FROM powers WHERE power_name = '{power}'
            """)
                power_num = cursor.fetchall()[0][0]
                cursor.execute(f"""
                SELECT member_id FROM members WHERE name = '{member.get("name")}'
            """)
                member_num = cursor.fetchall()[0][0]
                cursor.execute(f"""
                INSERT INTO power_member (member_id, power_id) VALUES (?, ?)  
                               """, (member_num, power_num))

    conn.commit()
    
power_to_member()

