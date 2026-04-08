import sqlite3


conn = sqlite3.connect("0_base.db")
cursor = conn.cursor()


def check_tabelle_true(tabellen_name):
    try:
        cursor.execute(f"SELECT * FROM {tabellen_name} LIMIT 0")
        return True
    except:
        return False

    return False


def show_irgendwas():
    cursor.execute(
        """
    SELECT members.member_name, squads.squadName
    FROM members
    JOIN squads on members.squad_from_member = squads.squad_id
    WHERE squads.squadName = 'Avengers'
"""
    )
