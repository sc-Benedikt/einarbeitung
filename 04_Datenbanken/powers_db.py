import sqlite3, json
from base import *

conn = sqlite3.connect("0_base.db")
cursor = conn.cursor()

with open("/home/git_repo/einarbeitung/base.json", "r", encoding="utf-8") as data:
    all_squads = json.load(data)


def creat_db_powers():
  
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS powers (
            power_id INTEGER PRIMARY KEY,
            power_name TEXT
            )
            """
        )

    
        powers_check_list = []

        for squad in all_squads:
            for member in squad.get("members"):
                for power in member.get("powers"):

                    if power not in powers_check_list:

                        cursor.execute(
                            """
                        INSERT INTO powers (power_name) VALUES (?);
                        """,
                            (power,),
                        )
                        powers_check_list.append(power)
                      


def power_to_member():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS powers_to_members (
    power_name TEXT,
    member_name TEXT,
    PRIMARY KEY (power_name, member_name)
    FOREIGN KEY (power_name) REFERENCES powers(power_name),
    FOREIGN KEY (member_name) REFERENCES members(member_name)
    )

    """)


    for squad in all_squads:
        for member in squad.get("members"):
            for power in member.get("powers"):


                    cursor.execute("""
                    INSERT OR IGNORE INTO powers_to_members(power_name, member_name)
                    VALUES (?, ?)
                                """, (power, member.get("name"),))
    conn.commit()


def show_powers():
    cursor.execute("""
    SELECT 

    """)
    power_id = cursor.fetchall()
    cursor.execute("""
    SELECT power_name
    FROM powers
    WHERE LOWER(power_id) = LOWER(?)
    """,  (power_id,))