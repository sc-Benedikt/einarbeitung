import json
import yaml
from dict2xml import dict2xml

file_path = "/home/git_repo/einarbeitung/"

with open(f"{file_path}base.json", "r") as file:
    date = json.load(file)


def json_to_yml():
    with open(
        f"{file_path}03_Dateiformate/base.yml", "w", encoding="utf-8"
    ) as yml_file:
        yaml.safe_dump(date, yml_file, default_flow_style=False, allow_unicode=True)


def json_to_xml():
    xml = dict2xml(date)
    with open(f"{file_path}03_Dateiformate/base.xml", "w") as xml_data:
        xml_data.write(xml)


json_to_yml()
json_to_xml()
