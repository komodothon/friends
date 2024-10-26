from flask import Flask, render_template, request, g
import sqlite3
from os.path import join


app = Flask(__name__)

DATABASE = join('instance', 'friends.db')

# database
def get_db_connection():
    if 'db' not in g:
        g.db = sqlite3.connect(DATABASE)
        g.db.row_factory = sqlite3.Row
    
    return g.db

def get_db_as_dict(cursor):
    cursor.execute("SELECT * FROM friends")
    rows = cursor.fetchall()
    rows = [dict(row) for row in rows]   
    headers = [description[0] for description in cursor.description]
    return headers, rows



@app.teardown_appcontext
def close_db(exception):
    db = g.pop('db', None)
    if db is not None:
        db.close()



@app.route("/", methods=["GET"])
def home():
    db_connection = get_db_connection()
    cursor = db_connection.cursor()
    headers, rows = get_db_as_dict(cursor)   

    return render_template("home.html", headers=headers, rows=rows)


@app.route("/add", methods=["POST"])
def add():
    db_connection = get_db_connection()
    cursor = db_connection.cursor()

    name = request.form.get('name')
    role = request.form.get('role')
    description = request.form.get('description')
    gender = request.form.get('gender')

    # print((name, role, description, gender))
    cursor.execute("INSERT INTO friends (name, role, description, gender) VALUES (?, ?, ?, ?)", (name, role, description, gender))
    db_connection.commit()

    headers, rows = get_db_as_dict(cursor)

    # return "Friend added"
    return render_template("home.html", headers=headers, rows=rows)

@app.route("/edit/<int:id>", methods=["POST", "GET"])
def update(id):
    db_connection = get_db_connection()
    cursor = db_connection.cursor()
    cursor.execute("SELECT * FROM friends WHERE id = ? LIMIT 1", (id,))
    row = cursor.fetchone()
    row = dict(row)
    if request.method == "POST":
        name = request.form.get('name', row['name'])
        role = request.form.get('role', row['role'])
        description = request.form.get('description', row['description'])
        gender = request.form.get('gender', row['gender'])

        cursor.execute(
            "UPDATE friends SET name = ?, role = ?, description = ?, gender = ?  WHERE id = ?",
            (name, role, description, gender, id))
        
        db_connection.commit()

    headers, rows = get_db_as_dict(cursor)
    return render_template("home.html", headers=headers, rows=rows)


@app.route("/delete/<int:id>", methods=["POST"])
def delete(id):
    db_connection = get_db_connection()
    cursor = db_connection.cursor()
    
    cursor.execute("DELETE FROM friends WHERE id = ?", (id,))
    db_connection.commit()

    headers, rows = get_db_as_dict(cursor)
    return render_template("home.html", headers=headers, rows=rows)


if __name__ == '__main__':
    app.run(debug=True)