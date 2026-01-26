import json
import yaml

with open (fr"/home/git_repo/einarbeitung/03_Dateiformate/base.json", "r") as file:
    date = json.load(file)

    print(date)