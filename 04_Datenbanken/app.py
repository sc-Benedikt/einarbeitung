import sqlite3, os
from pathlib import Path
import base
from squads_db import *
from member_db import *
from powers_db import *

conn = sqlite3.connect("0_base.db")
cursor = conn.cursor()

def daten_bekommen_test():
    cursor.execute(f"""
                SELECT powers.power_name
                FROM powers
                JOIN powers_from_members ON powers.power_id = powers_from_members.power_id
                WHERE powers_from_members.member_id = 1;
    """)


try:
    cursor.execute("""
        SELECT 1 FROM members
        """, )

except sqlite3.OperationalError:

    creat_db_squads()
    creat_db_members()
    creat_db_powers()
    power_to_member()

while True:
    print("""
    ----------Hallo---------

        Options:
            show -> 1
            exit -> x   
            """)
    user_choice = input("->")

    if user_choice in ["x", "X"]:
        break

    if user_choice == "1":
        print("""#
        -------Show What--------

            Options
                Squads ->   1
                Member ->   2
                exit ->     x
              """)
        user_choice = input("->")
        if user_choice == "1":
            show_squad()
            user_choice = input("->")
        elif user_choice == "2":
            user_choice = "member"
            

    







