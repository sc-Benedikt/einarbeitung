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
                    """
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
       

def add_member():
    squad_from_member = input("which squad to add: ")
    name = input("name: ")
    age = input("age: ")
    secr_iden = input("Secretidentity: ")

    cursor.execute(
        """
    SELECT squad_id
    FROM squads
    WHERE LOWER(squadName) = LOWER(?)
    """,
        (squad_from_member,),
    )

    cursor.execute(
        """
    INSERT INTO members (member_name, member_age, member_secretIdentity, Squad_from_member)
    VALUES (?, ?, ?, ?)
    """,
        (
            name,
            age,
            secr_iden,
            squad_from_member,
        ),
    )



def show_member():

    member_choice = input("->")
    cursor.execute(
        """
    SELECT member_name, member_age, member_secretIdentity
    FROM members
    WHERE LOWER(member_name) = LOWER(?)
    """,
        (member_choice,),
    )
    member = cursor.fetchall()[0]
    print("Name: " + member[0])
    print("Age: " + member[1])
    print("secretIdentity: " + member[2])

def show_members():
    from_which_squad = input("->")
    cursor.execute(
        """
    SELECT squad_id
    FROM squads
    WHERE LOWER(squadName) = LOWER(?)
    """,
        (from_which_squad,),
    )
    squad_number = cursor.fetchall()[0][0]

    cursor.execute(
        """
    SELECT member_name
    FROM members
    WHERE LOWER(Squad_from_member) = LOWER(?)
    """,
        (squad_number,),
    )

    member = cursor.fetchall()
    for i in member:
        print(i[0])

def remove_member():
    which_member = input("->")
    cursor.execute("""
    DELETE FROM members
    WHERE LOWER(member_name) = LOWER(?)
    """, (which_member,))
    cursor.execute("""
    DELETE FROM powers_to_members
    WHERE LOWER(member_name) = LOWER(?)
    """, (which_member, ))
