from flask import Flask, render_template, session, redirect, request
import json, sqlite3


connection = sqlite3.connect(
    "/home/git_repo/einarbeitung/05_Webentwicklung/User_Infos.db"
)

cursor = connection.cursor()

USER_FILE = r"/home/git_repo/einarbeitung/05_Webentwicklung/user.json"

app = Flask(__name__)
app.secret_key = "ich_weiß_keinen_guten_key"


def get_data(data: str):

    connection = sqlite3.connect(
        "/home/git_repo/einarbeitung/05_Webentwicklung/User_Infos.db"
    )
    cursor = connection.cursor()
    choice_text = session.get("choice")
    cursor.execute(f"SELECT {data} FROM infos WHERE info_id = {choice_text}")
    daten = cursor.fetchall()
    return daten


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
        # "INSERT INTO users (user, p) VALUERS (?, ?)"
        try:
            command_add_user = "INSERT INTO users (username, userpassword) VALUES ( ?, ?)"
            values = (username, userpassword)
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
            if username == i[0] and userpassword == i[1]:
                session["username"] = username
                session["password"] = userpassword
                return redirect("/auswahl")
        return render_template("/login.html")

    else:
        return render_template("/login.html")


@app.route("/auswahl")
def hello_world():
    connection = sqlite3.connect(
        "/home/git_repo/einarbeitung/05_Webentwicklung/User_Infos.db"
    )
    cursor = connection.cursor()
    cursor.execute("SELECT big_header FROM infos")
    headers = cursor.fetchall()
    return render_template(
        "startmenu.html",
        header1=headers[0][0],
        header2=headers[1][0],
        header3=headers[2][0],
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

    session["choice"] = request.form.get("choice", 1)

    anzahl_spalten = len(connection.execute("PRAGMA table_info(infos)").fetchall()) // 2
    anzahl_spalten -= 1
    all_info_blocks = ""
    for i in range(1, anzahl_spalten + 1):
        info_text = get_data(f"info_text_{i}")
        small_header = get_data(f"small_header_{i}")
        info_block = f"""
        
        <div class="text_formation example">
        <h2>{small_header[0][0]}</h2>
        <p>{info_text[0][0]}</p>
        </div>
        """
        if info_text != "0" and small_header != "0":
            all_info_blocks += info_block

    return render_template(
        "info_site.html",
        ueberschrift=get_data("big_header")[0][0],
        infos=all_info_blocks,
    )


@app.route("/new_acc")
def creat_new_acc():
    return render_template("new_acc.html")


@app.route("/delete")
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
    connection = sqlite3.connect("/home/git_repo/einarbeitung/05_Webentwicklung/User_Infos.db")
    cursor = connection.cursor()
    
    anzahl_spalten = len(connection.execute("PRAGMA table_info(infos)").fetchall()) // 2
    anzahl_spalten -= 1
    all_options = ""
    for i in range(1, anzahl_spalten + 1):
        small_header = get_data(f"small_header_{i}")

        info_block = f"""
        <option value="info_text_{i}">{small_header[0][0]}</option>
        """

        all_options += info_block


    return render_template(
        "/text_schreiben.html",
        options = all_options
    )


@app.route("/daten_speichern", methods=["POST"])
def safe_daten():
    connection = sqlite3.connect(
        "/home/git_repo/einarbeitung/05_Webentwicklung/User_Infos.db"
    )
    cursor = connection.cursor()
    if request.form.get("change_text") != "neuer_text":
        text = request.form.get("text")
        number = session.get("choice")
        text_choice = request.form.get("change_text")
        cursor.execute(
            f"UPDATE infos SET '{text_choice}' = '{text}' WHERE info_id = '{number}'"
        )
        connection.commit()
        return render_template("/login.html")
    
    connection = sqlite3.connect("/home/git_repo/einarbeitung/05_Webentwicklung/User_Infos.db")
    cursor = connection.cursor()
    text_daten = request.form.get("text")
    header_daten = request.form.get("header")
    neue_info_num = len(connection.execute("PRAGMA table_info(infos)").fetchall()) // 2
  

    for infos in range (1, 3, +1):
        if header_daten and text_daten:
            values = (f'{header_daten}', f'{text_daten}')
        else:
            values = ('0', '0', f'{infos}')
        cursor.execute(f"""UPDATE infos SET small_header_{neue_info_num} = ?, info_text_{neue_info_num} = ? WHERE info_id = ?""", (values))
       
    
    return redirect("/")

