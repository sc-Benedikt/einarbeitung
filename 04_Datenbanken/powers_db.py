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

    cursor.execute(
        """
    CREATE TABLE powers_from_members (
    member_id INTEGER,
    power_id INTEGER,
    FOREIGN KEY(member_id) REFERENCES member(member_id)
    FOREIGN KEY(power_id) REFERENCES power(power_id)
                   )
"""
    )

    for squad in all_squads:
        for member in squad.get("members"):
            for power in member.get("powers"):
                cursor.execute(
                    f"""
                SELECT power_id FROM powers WHERE power_name = '{power}'
            """
                )
                power_num = cursor.fetchall()[0][0]
                cursor.execute(
                    f"""
                SELECT member_id FROM members WHERE member_name = '{member.get("name")}'
            """
                )
                member_num = cursor.fetchall()[0][0]
                cursor.execute(
                    f"""
                INSERT INTO powers_from_members (member_id, power_id) VALUES (?, ?)  
                               """,
                    (member_num, power_num),
                )
    conn.commit()
 



