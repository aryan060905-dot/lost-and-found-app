import sqlite3

from flask import Flask, render_template, request , redirect

app = Flask(__name__)

@app.route("/")
def home():
    conn = sqlite3.connect("lost_found.db")
    cursor = conn.cursor()

    cursor.execute("SELECT id, item_name, description, contact, status FROM lost_items")
    items = cursor.fetchall()

    conn.close()
    return render_template("index.html", items=items)



@app.route("/report", methods=["GET", "POST"])
def report():
    success = False

    if request.method == "POST":
        item = request.form["item_name"]
        desc = request.form["description"]
        contact = request.form["contact"]
        status = request.form["status"]

        conn = sqlite3.connect("lost_found.db")
        cursor = conn.cursor()

        cursor.execute(
    "INSERT INTO lost_items (item_name, description, contact, status) VALUES (?, ?, ?, ?)",
    (item, desc, contact, status)
)

        conn.commit()
        conn.close()

        success = True

    return render_template("report.html", success=success)


@app.route("/delete/<int:item_id>")
def delete(item_id):
    conn = sqlite3.connect("lost_found.db")
    cursor = conn.cursor()

    cursor.execute("DELETE FROM lost_items WHERE id = ?", (item_id,))
    conn.commit()
    conn.close()

    return redirect("/")





if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)

