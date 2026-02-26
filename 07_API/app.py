from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)

if __name__  == "__main__":

    app.run(debug=True)

def init_db():
    connection = sqlite3.connect("base.db")
    cursor = connection.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS items(
                        id INTEGER PRIMARY KEY,
                        type TEXT,
                        price INTEGER)""")

    cursor.execute("SELECT COUNT(*) FROM items")
    count = cursor.fetchone()[0]
    if count == 0:
        cursor.execute("INSERT INTO items (type, price) VALUES (?, ?)", ("Laptop", 1200))
        cursor.execute("INSERT INTO items (type, price) VALUES (?, ?)", ("maus", 20))
        cursor.execute("INSERT INTO items (type, price) VALUES (?, ?)", ("screen", 300))
    connection.commit()
    connection.close()

init_db()


@app.route("/items")
def get_all_items():
    connection = sqlite3.connect("base.db")
    cursor = connection.cursor()

    rows = cursor.execute("SELECT * FROM items").fetchall()
    items  = [{"id" : r[0], "type":r[1],"price":r[2]} for r in rows]
    connection.close()
    return jsonify(items) 

@app.route("/items/<int:item_id>")
def get_item(item_id):
    connection = sqlite3.connect("base.db")
    cursor = connection.cursor()
    return cursor.execute("SELECT * FROM items WHERE id = (?)", (item_id,)).fetchall()
  
    return ("item nicht gefunden")

