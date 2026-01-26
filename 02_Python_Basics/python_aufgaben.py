import json, os

with open (fr"/home/git_repo/einarbeitung/base.json", "r") as i:
    squads = json.load(i)

def Terminal_clear():
    os.system("clear")

Terminal_clear()

class Squad():
    def __init__(self, squad_dict):
        self.squads_dict = squad_dict
        self.squadName = squad_dict["squadName"]
        self.homeTown = squad_dict["homeTown"]
        self.formed = squad_dict["formed"]
        self.status = squad_dict["status"]
        self.secret_base = squad_dict["secretBase"]
        self.active = squad_dict["active"]
        self.members = squad_dict["members"]

    def member_add(self):

        new_member = {}
        new_member["name"] = input("name: ")
        new_member["age"]= input("age: ")
        new_member["secretIdentity"] = input("secretIdentity: ")

        powers = []
        powers.append(input("first power: "))
        powers.append(input("second power: "))
        powers.append(input("third power: "))

        new_member["powers"] = powers
        self.members.append(new_member)
        print("member hinzugefügt")

    def show_squads(self):

        for k, v in (self.squads_dict).items():
            if type(v) is not list:
                print(f" {k} : {v} ")

            else:
                print(f"{k} : {len(v)}")


    def show_member(self):

        for member in self.members:
            print(member.get("name"))


        member_choice = input("Welchen member anzeigen: ")
        for member in self.squads_dict.get("members"):
            if member_choice.lower() == member.get("name").lower():

                print("\n")

                for k, v in (member).items():
                    if type(v) is list:
                        for item in v:  
                            print(f"{k} : {item}")

                    else:
                        print(f"{k} : {v}")
 
    def member_delete(self):

        for member in self.members:
            print(member.get("name"))

        member_choice = input("Welchen member löschen: ")

        for member in self.members:
            if member_choice.lower() == member.get("name").lower():
                (self.members).remove(member)

                print("member gelöscht")


while True: 
            
    print("""
        Teams anschauen:    show squads
        Member hinzufügen:  add member
        Member löschen:     delete member
        Member anzeigen:    show member
        """)

    what_do = input("was möchtest du tun: ")
    options = ["show squads", "add member", "delete member", "show member"]
    if what_do in options:

        Terminal_clear() 

        options_2 = []
        for squad in squads:
            options_2.append(squad.get("squadName").lower())
            print(squad.get("squadName"))

        choice = input("für welches der oben genannten squads: ")

        Terminal_clear() 

        if choice in options_2:

            for squad in squads:
                if choice.lower() == (squad.get("squadName")).lower():
                    choice_squad = squad

            if what_do == "show squads":
                Squad(choice_squad).show_squads()

            elif what_do == "add member":
                Squad(choice_squad).member_add()

            elif what_do == "delete member":
                Squad(choice_squad).member_delete()
                
            elif what_do == "show member":
                Squad(choice_squad).show_member()
        
        else:
            continue

    elif what_do == "stop":
        break
        

