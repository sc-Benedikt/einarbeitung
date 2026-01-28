from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template("startmenu.html")


@app.route("/citys")
def citys():
    return render_template("citys.html")


@app.route("/countries")
def countries():
    return render_template("countries.html")