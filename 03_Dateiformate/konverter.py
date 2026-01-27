import json
import yaml
from dict2xml import dict2xml

with open (fr"/home/git_repo/einarbeitung/base.json", "r") as file:
    date = json.load(file)

def json_to_yml():
    with open (fr"/home/git_repo/einarbeitung/03_Dateiformate/base.yml", "w", encoding="utf-8") as yml_file:
        yaml.safe_dump(date, yml_file ,default_flow_style=False, allow_unicode=True)

def json_to_xml():
        xml = dict2xml(date)
        print(xml)
        with open (fr"/home/git_repo/einarbeitung/03_Dateiformate/base.xml", "w") as xml_data:
            xml_data.write(xml)
        



json_to_yml()
json_to_xml()