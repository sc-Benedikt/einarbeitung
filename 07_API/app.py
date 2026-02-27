from flask import Flask, jsonify, render_template
import sqlite3

app = Flask(__name__)


def init_db():
    connection = sqlite3.connect("base.db")
    cursor = connection.cursor()
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS items(
                        id INTEGER PRIMARY KEY,
                        type TEXT,
                        price INTEGER)"""
    )

    cursor.execute("SELECT COUNT(*) FROM items")
    count = cursor.fetchone()[0]
    if count == 0:
        values = [("Laptop", 1849.99), ("maus", 19.99), ("screen", 249.99)]
        cursor.executemany(
            "INSERT INTO items (type, price) VALUES (?, ?) ", values,
        )

    connection.commit()
    connection.close()


init_db()


@app.route("/items")
def get_all_items():
    connection = sqlite3.connect("base.db")
    cursor = connection.cursor()

    rows = cursor.execute("SELECT * FROM items").fetchall()
    connection.close()
    items = """"""
    for r in rows:
        items += f"\n id: {r[0]}, type: {r[1]}, price: {r[2]},    "
    print(items)
    return items


@app.route("/items/<int:item_id>")
def get_item(item_id):
    try:
        connection = sqlite3.connect("base.db")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM items WHERE id = (?)", (item_id,))
        option_choice = cursor.fetchall()[0]
        return f"id: {option_choice[0]}, type: {option_choice[1]}, price: {option_choice[2]} "
    except IndexError:
        return "Item not found"


if __name__ == "__main__":
    app.run(debug=True)
