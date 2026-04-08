import sqlite3
from squads_db import *
from member_db import *
from powers_db import *

conn = sqlite3.connect("0_base.db")
cursor = conn.cursor()


def daten_bekommen_test():
    cursor.execute("""
                SELECT powers.power_name
                FROM powers
                JOIN powers_from_members ON powers.power_id = powers_from_members.power_id
                WHERE powers_from_members.member_id = 1;
    """)


try:
    cursor.execute(
        """
        SELECT 1 FROM members
        """,
    )

except sqlite3.OperationalError:
    creat_db_squads()
    creat_db_members()
    creat_db_powers()
    power_to_member()

while True:
    print("""
    ----------Hallo---------

        Options:
            show    -> 1
            add     -> 2
            remove  -> 3
            exit    -> x
            """)
    user_choice = input("->")

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

        elif user_choice == "2":
            show_squad()
            show_members()
            show_member()
            

        elif user_choice in ["x", "X"]:
            break

    elif user_choice == "2":
        print((
            """
        -------Add What--------

            Options
                Squads ->   1
                Member ->   2
                exit ->     x
        """
        ))
        user_choice = input("->")

        if user_choice == "1":
            add_squad()
        
        if user_choice == "2":
            show_squad()
            add_member()

        else:
            break
    
    elif user_choice == "3":
        print((
            """
        -------Remove What-------

            Options
                Squads ->   1
                Member ->   2
                exit ->     x
        """
        ))
        user_choice = input("->")
        if user_choice == "1":
            remove_squad()
        elif user_choice == "2":
            remove_member()

    else:
        break

