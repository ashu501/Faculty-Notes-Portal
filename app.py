from flask import Flask, render_template, request, redirect, send_from_directory
from werkzeug.utils import secure_filename
import os
import sqlite3
app = Flask(__name__)
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/notes")
def notes():
    return "<h1>Notes Page</h1>"

@app.route("/programs")
def programs():
    return "<h1>Programs Page</h1>"

@app.route("/about")
def about():
    return "<h1>About Page</h1>"

@app.route("/contact")
def contact():
    return "<h1>Contact Page</h1>"

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        conn = sqlite3.connect("database/faculty.db")
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM admin WHERE username=? AND password=?",
            (username, password)
        )

        user = cursor.fetchone()

        conn.close()
        if user:
            return render_template("dashboard.html")

        else:
            return "<h2>Invalid Username or Password</h2>"

    return render_template("login.html")
@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/upload", methods=["GET", "POST"])
def upload():
    if request.method == "POST":

        subject = request.form["subject"]
        unit = request.form["unit"]
        file = request.files["file"]

        if file.filename != "":
            filename = secure_filename(file.filename)
            file.save(os.path.join("uploads", filename))

            # Save note details in the database
            conn = sqlite3.connect("database/faculty.db")
            cursor = conn.cursor()

            cursor.execute(
                """
                INSERT INTO notes (subject, unit, filename)
                VALUES (?, ?, ?)
                """,
                (subject, unit, filename)
            )

            conn.commit()
            conn.close()

            return f"{filename} uploaded successfully and saved to the database!"

    return render_template("upload.html")
@app.route("/view_notes")
def view_notes():

    conn = sqlite3.connect("database/faculty.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM notes")
    notes = cursor.fetchall()

    conn.close()

    return render_template("view_notes.html", notes=notes)
@app.route("/download/<path:filename>")
def download(filename):

    upload_folder = os.path.join(app.root_path, "uploads")

    return send_from_directory(upload_folder, filename)
@app.route("/delete/<int:id>")
def delete(id):

    conn = sqlite3.connect("database/faculty.db")
    cursor = conn.cursor()

    cursor.execute("SELECT filename FROM notes WHERE id=?", (id,))
    file = cursor.fetchone()

    if file:
        filepath = os.path.join("uploads", file[0])

        if os.path.exists(filepath):
            os.remove(filepath)

    cursor.execute("DELETE FROM notes WHERE id=?", (id,))

    conn.commit()
    conn.close()

    return redirect("/view_notes")
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)