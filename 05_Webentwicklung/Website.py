from flask import Flask, render_template, session, redirect, request
import json


app = Flask(__name__)

USER_FILE = r"/home/git_repo/einarbeitung/05_Webentwicklung/user.json"

app = Flask(__name__)
app.secret_key = "ich_weiß_keinen_guten_key"


def daten_nehmen():
    with open("/home/git_repo/einarbeitung/05_Webentwicklung/info_texte.json") as file:
        web_site_daten = json.load(file)
        return web_site_daten


def daten_umwandeln():
    web_site_daten = daten_nehmen()
    daten = web_site_daten[session["choice"]]
    text_daten = daten["informationen"]
    text_1 = text_daten["infotext_1"]
    text_2 = text_daten["infotext_2"]
    text_3 = text_daten["infotext_3"]
    ueberschrift = daten.get("ueberschrift")
    return text_1, text_2, text_3, ueberschrift

@app.route("/", methods=["GET", "POST"])
def login():
    name = session.get("username")

    if name == None:

        if request.method == "POST":

            username = request.form["name"]
            userpassword = request.form["password"]

            username = username.replace(" ", "")
            userpassword = userpassword.replace(" ", "")
            print(username)
            print(userpassword)
            with open(USER_FILE, "r", encoding="utf - 8") as f:
                users = json.load(f)

            if username in users and users[username] == userpassword:
                session["username"] = username
                session["password"] = userpassword
                return redirect("/auswahl")
            else:
                return render_template("/login.html")
        else:
            return render_template("/login.html")
    else:
        return redirect("/auswahl")


@app.route("/auswahl")
def hello_world():
    
    web_site_daten = daten_nehmen()
    return render_template(
        "startmenu.html",
        daten1=web_site_daten["info1"],
        daten2=web_site_daten["info2"],
        daten3=web_site_daten["info3"],
    )


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")


@app.route("/infos_num_1")
def infos1():
    session["choice"]= "info1"
    text_1, text_2, text_3, ueberschrift = daten_umwandeln()
    return render_template(
        "infos_num_1.html",
        ueberschrift=ueberschrift,
        info_text_1=text_1,
        info_text_2=text_2,
        info_text_3=text_3,
    )


@app.route("/infos_num_2")
def infos2():
    session["choice"]= "info2"
    text_1, text_2, text_3, ueberschrift = daten_umwandeln()
    return render_template(
        "infos_num_2.html",
        ueberschrift=ueberschrift,
        info_text_1=text_1,
        info_text_2=text_2,
        info_text_3=text_3,
    )


@app.route("/infos_num_3")
def infos3():
    session["choice"]= "info3"
    text_1, text_2, text_3, ueberschrift = daten_umwandeln()

    return render_template(
        "infos_num_3.html",
        ueberschrift=ueberschrift,
        info_text_1=text_1,
        info_text_2=text_2,
        info_text_3=text_3,
    )