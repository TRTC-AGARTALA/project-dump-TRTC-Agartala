student_attendance/
│
├── app.py
├── attendance.db
│
├── templates/
│   ├── login.html
│   ├── dashboard.html
│   └── attendance.html
│
└── static/
    └── style.css
pip install flask
from flask import Flask, render_template, request, redirect, session
import sqlite3

app = Flask(__name__)
app.secret_key = "student_secret_key"


def get_db():
    return sqlite3.connect("attendance.db")


# Create database
conn = get_db()
conn.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE,
    password TEXT,
    name TEXT
)
""")

conn.execute("""
CREATE TABLE IF NOT EXISTS attendance (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER,
    date TEXT
)
""")

# Demo student
try:
    conn.execute(
        "INSERT INTO students (username, password, name) VALUES (?, ?, ?)",
        ("student1", "1234", "Ajoy")
    )
    conn.commit()
except sqlite3.IntegrityError:
    pass

conn.close()


@app.route("/")
def home():
    return redirect("/login")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        conn = get_db()
        student = conn.execute(
            "SELECT * FROM students WHERE username=? AND password=?",
            (username, password)
        ).fetchone()
        conn.close()

        if student:
            session["student_id"] = student[0]
            session["student_name"] = student[3]
            return redirect("/dashboard")

        return render_template("login.html", error="Invalid username or password")

    return render_template("login.html")


@app.route("/dashboard")
def dashboard():
    if "student_id" not in session:
        return redirect("/login")

    return render_template(
        "dashboard.html",
        name=session["student_name"]
    )


@app.route("/attendance", methods=["GET", "POST"])
def attendance():
    if "student_id" not in session:
        return redirect("/login")

    if request.method == "POST":
        from datetime import date

        today = str(date.today())
        conn = get_db()

        existing = conn.execute(
            "SELECT * FROM attendance WHERE student_id=? AND date=?",
            (session["student_id"], today)
        ).fetchone()

        if not existing:
            conn.execute(
                "INSERT INTO attendance (student_id, date) VALUES (?, ?)",
                (session["student_id"], today)
            )
            conn.commit()

        conn.close()

    conn = get_db()
    records = conn.execute(
        "SELECT date FROM attendance WHERE student_id=? ORDER BY date DESC",
        (session["student_id"],)
    ).fetchall()
    conn.close()

    return render_template("attendance.html", records=records)


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")


if __name__ == "__main__":
    app.run(debug=True)
    from flask import Flask, render_template, request, redirect, session
import sqlite3

app = Flask(__name__)
app.secret_key = "student_secret_key"


def get_db():
    return sqlite3.connect("attendance.db")


# Create database
conn = get_db()
conn.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE,
    password TEXT,
    name TEXT
)
""")

conn.execute("""
CREATE TABLE IF NOT EXISTS attendance (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER,
    date TEXT
)
""")

# Demo student
try:
    conn.execute(
        "INSERT INTO students (username, password, name) VALUES (?, ?, ?)",
        ("student1", "1234", "Ajoy")
    )
    conn.commit()
except sqlite3.IntegrityError:
    pass

conn.close()


@app.route("/")
def home():
    return redirect("/login")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        conn = get_db()
        student = conn.execute(
            "SELECT * FROM students WHERE username=? AND password=?",
            (username, password)
        ).fetchone()
        conn.close()

        if student:
            session["student_id"] = student[0]
            session["student_name"] = student[3]
            return redirect("/dashboard")

        return render_template("login.html", error="Invalid username or password")

    return render_template("login.html")


@app.route("/dashboard")
def dashboard():
    if "student_id" not in session:
        return redirect("/login")

    return render_template(
        "dashboard.html",
        name=session["student_name"]
    )


@app.route("/attendance", methods=["GET", "POST"])
def attendance():
    if "student_id" not in session:
        return redirect("/login")

    if request.method == "POST":
        from datetime import date

        today = str(date.today())
        conn = get_db()

        existing = conn.execute(
            "SELECT * FROM attendance WHERE student_id=? AND date=?",
            (session["student_id"], today)
        ).fetchone()

        if not existing:
            conn.execute(
                "INSERT INTO attendance (student_id, date) VALUES (?, ?)",
                (session["student_id"], today)
            )
            conn.commit()

        conn.close()

    conn = get_db()
    records = conn.execute(
        "SELECT date FROM attendance WHERE student_id=? ORDER BY date DESC",
        (session["student_id"],)
    ).fetchall()
    conn.close()

    return render_template("attendance.html", records=records)


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")


if __name__ == "__main__":
    app.run(debug=True)
    