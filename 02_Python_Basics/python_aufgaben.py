import json

with open (fr"/home/git_repo/einarbeitung/base.json", "r") as i:
    squads = json.load(i)

class Squad():
    def __init__(self, squad_dict):
        self.squas_dict = squad_dict
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
        print(self.members)

    def anzeigen(self):
        for k, v in (self.squas_dict).items():
            if type(v) is not list:
                print(f" {k} : {v} ")
            else:
                print(f"{k} : {len(v)}")
        
        show_members = input("members anzeigen: ")
        if show_members == "yes":
            for member in self.members:
                for k, v in (member).items():
                    print(f"{k} : {v}")

print("""
      Teams anschauen: show

      
      """)

what_do = input("was möchtest du tun: ")


for squad in squads:
    print(squad.get("squadName"))

choice = input("für welches der oben genannten squads: ")

for squad in squads:
    if choice.lower() == (squad.get("squadName")).lower():
        choice_squad = squad


if what_do == "show":
    Squad(choice_squad).anzeigen()

elif what_do == "add member":
    Squad(choice_squad).member_add()



    