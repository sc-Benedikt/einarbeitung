from flask import Flask, render_template
import json
app = Flask(__name__)

def daten_nehmen():
    with open ("/home/git_repo/einarbeitung/05_Webentwicklung/info_texte.json") as file:
        web_site_daten = json.load(file)
        return web_site_daten


@app.route("/")
def hello_world():
    web_site_daten = daten_nehmen()
    return render_template("startmenu.html",    
            daten1 = web_site_daten["info1"],
            daten2 = web_site_daten["info2"],
            daten3 = web_site_daten["info3"]                
                           )


@app.route("/infos_num_1")
def infos1():
    web_site_daten = daten_nehmen()
    daten = web_site_daten["info1"]
    text_daten = daten["informationen"]
    text_1 = text_daten["infotext_1"]
    text_2 = text_daten["infotext_2"]
    text_3 = text_daten["infotext_3"]

    return render_template("infos_num_1.html", 
            ueberschrift = daten.get("ueberschrift"),
            info_text_1 = text_1,
            info_text_2 = text_2,
            info_text_3 = text_3 
            )


@app.route("/infos_num_2")
def infos2():
    web_site_daten = daten_nehmen()
    daten = web_site_daten["info2"]
    text_daten = daten["informationen"]
    text_1 = text_daten["infotext_1"]
    text_2 = text_daten["infotext_2"]
    text_3 = text_daten["infotext_3"]

    return render_template("infos_num_2.html", 
            ueberschrift = daten.get("ueberschrift"),
            info_text_1 = text_1,
            info_text_2 = text_2,
            info_text_3 = text_3 
            )

@app.route("/infos_num_3")
def infos3():
    web_site_daten = daten_nehmen()
    daten = web_site_daten["info3"]
    text_daten = daten["informationen"]
    text_1 = text_daten["infotext_1"]
    text_2 = text_daten["infotext_2"]
    text_3 = text_daten["infotext_3"]

    return render_template("infos_num_3.html", 
            ueberschrift = daten.get("ueberschrift"),
            info_text_1 = text_1,
            info_text_2 = text_2,
            info_text_3 = text_3 
            )