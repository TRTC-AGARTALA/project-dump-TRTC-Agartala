from flask import Flask, render_template, request, redirect
import sqlite3
from datetime import date

app = Flask(__name__)

def get_db():
    conn = sqlite3.connect("attendance.db")
    conn.row_factory = sqlite3.Row
    return conn

# Create database
def create_database():
    conn = get_db()

    conn.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            roll_no TEXT NOT NULL UNIQUE
        )
    """)

    conn.execute("""
        CREATE TABLE IF NOT EXISTS attendance (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id INTEGER,
            date TEXT,
            status TEXT,
            FOREIGN KEY(student_id) REFERENCES students(id)
        )
    """)

    conn.commit()
    conn.close()


@app.route("/")
def home():
    conn = get_db()
    students = conn.execute("SELECT * FROM students").fetchall()
    conn.close()
    return render_template("index.html", students=students)


@app.route("/add_student", methods=["POST"])
def add_student():
    name = request.form["name"]
    roll_no = request.form["roll_no"]

    conn = get_db()

    try:
        conn.execute(
            "INSERT INTO students (name, roll_no) VALUES (?, ?)",
            (name, roll_no)
        )
        conn.commit()
    except sqlite3.IntegrityError:
        pass

    conn.close()
    return redirect("/")


@app.route("/mark_attendance", methods=["POST"])
def mark_attendance():
    today = str(date.today())
    conn = get_db()

    students = conn.execute("SELECT * FROM students").fetchall()

    for student in students:
        status = request.form.get(f"status_{student['id']}")

        if status:
            old = conn.execute(
                "SELECT * FROM attendance WHERE student_id=? AND date=?",
                (student["id"], today)
            ).fetchone()

            if old:
                conn.execute(
                    "UPDATE attendance SET status=? WHERE student_id=? AND date=?",
                    (status, student["id"], today)
                )
            else:
                conn.execute(
                    "INSERT INTO attendance (student_id, date, status) VALUES (?, ?, ?)",
                    (student["id"], today, status)
                )

    conn.commit()
    conn.close()

    return redirect("/")


@app.route("/attendance")
def attendance():
    conn = get_db()

    records = conn.execute("""
        SELECT students.name, students.roll_no,
               attendance.date, attendance.status
        FROM attendance
        JOIN students ON students.id = attendance.student_id
        ORDER BY attendance.date DESC
    """).fetchall()

    conn.close()

    return render_template("attendance.html", records=records)


if __name__ == "__main__":
    create_database()
    app.run(debug=True)