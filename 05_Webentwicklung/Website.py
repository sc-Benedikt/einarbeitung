from flask import Flask, render_template, session, redirect, request
import sqlite3, hashlib


connection = sqlite3.connect(
    "/home/git_repo/einarbeitung/05_Webentwicklung/User_Infos.db"
)
cursor = connection.cursor()

USER_FILE = r"/home/git_repo/einarbeitung/05_Webentwicklung/user.json"

app = Flask(__name__)
app.secret_key = "ich_weiß_keinen_guten_key"


def get_data(data: str, num):

    connection = sqlite3.connect(
        "/home/git_repo/einarbeitung/05_Webentwicklung/User_Infos.db"
    )
    cursor = connection.cursor()
    choice_text = session.get("choice")
    cursor.execute(f"SELECT {data} FROM {choice_text}")
    daten = cursor.fetchall()
    if daten != None:
        return daten[num]
    else:
        return ""


@app.route("/", methods=["GET", "POST"])
def login():
    name = session.get("username")
    connection = sqlite3.connect(
        "/home/git_repo/einarbeitung/05_Webentwicklung/User_Infos.db"
    )
    cursor = connection.cursor()

    if name:
        return redirect("/auswahl")

    if request.method == "POST" and request.form.get("password") == request.form.get(
        "password_2"
    ):

        username = request.form["name"]
        userpassword = request.form["password"]

        username = username.replace(" ", "")
        userpassword = userpassword.replace(" ", "")
        if userpassword == "":
            return redirect("/")

        try:
            command_add_user = (
                "INSERT INTO users (username, userpassword) VALUES ( ?, ?)"
            )
            values = (username, (hashlib.sha256(userpassword.encode()).hexdigest()))
            cursor.execute(command_add_user, values)
            connection.commit()
            return redirect("/")
        except sqlite3.IntegrityError:
            redirect("/")

    elif request.method == "POST":

        username = request.form["name"]
        userpassword = request.form["password"]

        username = username.replace(" ", "")
        userpassword = userpassword.replace(" ", "")

        cursor.execute("SELECT username, userpassword FROM users")
        anmelde_daten = cursor.fetchall()
        for i in anmelde_daten:
            if (
                username == i[0]
                and (hashlib.sha256(userpassword.encode()).hexdigest()) == i[1]
            ):
                session["username"] = username
                session["password"] = userpassword
                return redirect("/auswahl")
        return render_template("/login.html")

    else:
        return render_template("/login.html")


@app.route("/auswahl")
def hello_world():
    return render_template(
        "startmenu.html",
        header1="citie",
        header2="Countrie",
        header3="Persons",
    )


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")


@app.route("/info_site", methods=["POST"])
def infos1():

    connection = sqlite3.connect(
        "/home/git_repo/einarbeitung/05_Webentwicklung/User_Infos.db"
    )
    cursor = connection.cursor()

    session["choice"] = request.form.get("choice")

    cursor.execute("SELECT COUNT(*) FROM (?) ", {request.form.get('choice')})
    anzahl_spalten = cursor.fetchone()[0]
    all_info_blocks = ""
    for i in range(anzahl_spalten):
        text = get_data(f"text", i)
        header = get_data(f"header", i)
        info_block = f"""
        
        <div class="text_formation example">
        <h2>{header[0]}</h2>
        <p>{text[0]}</p>
        </div>

        """

        if text != "0" and header != "0":
            all_info_blocks += info_block

    return render_template(
        "info_site.html",
        ueberschrift=session.get("choice"),
        infos=all_info_blocks,
    )


@app.route("/new_acc")
def creat_new_acc():
    return render_template("new_acc.html")


@app.route("/delete_user")
def delete_acc():
    return render_template("acc_löschen.html")


@app.route("/finall_delete", methods=["POST"])
def finall_delete():
    connection = sqlite3.connect(
        "/home/git_repo/einarbeitung/05_Webentwicklung/User_Infos.db"
    )
    cursor = connection.cursor()
    confirm = request.form["password"]
    if confirm == session["password"]:
        cursor.execute(
            "DELETE FROM users WHERE username = ?", (session.get("username"),)
        )
        connection.commit()
        session.clear()
        return redirect("/")
    return redirect("/delete")


@app.route("/daten_aendern")
def change_data():
    connection = sqlite3.connect(
        "/home/git_repo/einarbeitung/05_Webentwicklung/User_Infos.db"
    )
    cursor = connection.cursor()

    cursor.execute(f"SELECT COUNT(*) FROM {session.get('choice')}")
    anzahl_spalten = cursor.fetchone()[0]
    all_options = ""
    for i in range(anzahl_spalten):
        small_header = get_data(f"header", i)[0]

        info_block = f"""
        <option value="{small_header}">{small_header}</option>
        """

        all_options += info_block

    return render_template("/text_schreiben.html", options=all_options)


@app.route("/daten_change", methods=["POST"])
def daten_change():
    connection = sqlite3.connect(
        "/home/git_repo/einarbeitung/05_Webentwicklung/User_Infos.db"
    )
    cursor = connection.cursor()
    if request.form.get("option") == "safe":


        if request.form.get("text_to_change") != "neuer_text":
            text = request.form.get("text")
            header = request.form.get("header")
            text_choice = request.form.get("text_to_change")
            info_option = session.get("choice")

            cursor.execute(
                f"UPDATE '{info_option}' SET 'text' = '{text}', 'header' = '{header}' WHERE header = '{text_choice}'"
            )
            connection.commit()
            return redirect("/")


        cursor.execute(
            f"INSERT INTO {session.get('choice')}(header, text) VALUES ('{request.form.get('header')}','{request.form.get('text')}')"
        )
        connection.commit()

        return redirect("/")

    elif request.form.get("option") == "delete":

        table = session.get("choice")
        header = request.form.get("text_to_change")
        cursor.execute(f"DELETE FROM {table} WHERE header = ?", (header,))
        connection.commit()
        return redirect("/")
