from flask import Flask, render_template, session, redirect, request
import json, sqlite3


connection = sqlite3.connect("/home/git_repo/einarbeitung/05_Webentwicklung/User_Infos.db")

cursor = connection.cursor()

USER_FILE = r"/home/git_repo/einarbeitung/05_Webentwicklung/user.json"

app = Flask(__name__)
app.secret_key = "ich_weiß_keinen_guten_key"

def get_data(data):

    connection = sqlite3.connect("/home/git_repo/einarbeitung/05_Webentwicklung/User_Infos.db")
    cursor = connection.cursor()
    choice_text = session.get("choice")
    cursor.execute(f"SELECT {data} FROM infos WHERE info_id = {choice_text}")
    daten = cursor.fetchall()
    return daten


@app.route("/", methods=["GET", "POST"])
def login():
    name = session.get("username")

    if name == None:
        if request.method == "POST" and request.form.get("password") == request.form.get("password_2"):



            username = request.form["name"]
            userpassword = request.form["password"]

            username = username.replace(" ", "")
            userpassword = userpassword.replace(" ", "")
            if userpassword == "":
                return redirect("/")
                
            connection = sqlite3.connect("/home/git_repo/einarbeitung/05_Webentwicklung/User_Infos.db")
            cursor = connection.cursor()
            command_add_user = "INSERT INTO users (username, userpassword) VALUES ( ?, ?)"
            values = (username, userpassword)
            cursor.execute(command_add_user, values)
            connection.commit()
            return redirect("/")

        elif request.method == "POST":

            username = request.form["name"]
            userpassword = request.form["password"]

            username = username.replace(" ", "")
            userpassword = userpassword.replace(" ", "")

            connection = sqlite3.connect("/home/git_repo/einarbeitung/05_Webentwicklung/User_Infos.db")
            cursor = connection.cursor()
            cursor.execute("SELECT COUNT(*) FROM users")
            anzahl = cursor.fetchall()[0][0]

            for i in range(anzahl):
                connection = sqlite3.connect("/home/git_repo/einarbeitung/05_Webentwicklung/User_Infos.db")
                cursor = connection.cursor()
                cursor.execute("SELECT username, userpassword FROM users")
                anmelde_daten = cursor.fetchall()
                for i in anmelde_daten:
                    if username == i[0] and userpassword == i[1]:
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
    connection = sqlite3.connect("/home/git_repo/einarbeitung/05_Webentwicklung/User_Infos.db")
    cursor = connection.cursor()
    cursor.execute("SELECT big_header FROM infos")
    headers = cursor.fetchall()
    return render_template(
        "startmenu.html",
        header1=headers[0][0],
        header2=headers[1][0],
        header3=headers[2][0]
    )


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")


@app.route("/info_site", methods=["POST", "GET"])
def infos1():

    try:
        session["choice"] = request.form["choice"]
    except:
        session["choice"] = session["choice"]


    return render_template(
        "info_site.html",
        ueberschrift=get_data("big_header")[0][0],
        info_text_1=get_data("info_text_1")[0][0],
        info_header_1=get_data("small_header_1")[0][0],
        info_text_2=get_data("info_text_2")[0][0],
        info_header_2=get_data("small_header_2")[0][0],
        info_text_3=get_data("info_text_3")[0][0],
        info_header_3=get_data("small_header_3")[0][0]
    )


@app.route("/new_acc")
def creat_new_acc():
    return render_template("new_acc.html")


@app.route("/delete")
def delete_acc():
    return render_template("acc_löschen.html")

@app.route("/finall_delete", methods = ["POST"])
def finall_delete():
    confirm = request.form["password"]
    if confirm == session["password"]:
        connection = sqlite3.connect("/home/git_repo/einarbeitung/05_Webentwicklung/User_Infos.db")
        cursor = connection.cursor()
        cursor.execute("DELETE FROM users WHERE username = ?", (session.get("username"),))
        connection.commit()
        session.clear()
        return redirect("/")
    else:
        return redirect("/delete")
    

@app.route("/daten_aendern")
def change_data():
    return render_template("/text_schreiben.html",             
        info_header_1=get_data("small_header_1")[0][0],
        info_header_2=get_data("small_header_2")[0][0],
        info_header_3=get_data("small_header_3")[0][0],
                           )

@app.route("/daten_speichern", methods = ["post"])
def safe_daten():
    connection = sqlite3.connect("/home/git_repo/einarbeitung/05_Webentwicklung/User_Infos.db")
    cursor = connection.cursor()
    text = request.form.get("text")
    number = session.get("choice")
    text_choice = request.form.get("change_text")
    cursor.execute(f"UPDATE infos SET '{text_choice}' = '{text}' WHERE info_id = '{number}'")
    connection.commit()
    return redirect("/info_site")

