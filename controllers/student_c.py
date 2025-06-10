import sqlite3
from models.student import Student

class StudentController:
    def __init__(self, db_path='database.db'):
        self.db_path = db_path

    def create_student(self, user_id, kelas, tahun):
        conn = sqlite3.connect(self.db_path)
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO Student (user_id, kelas, tahun) VALUES (?, ?, ?)",
            (user_id, kelas, tahun)
        )
        conn.commit()
        student_id = cur.lastrowid
        conn.close()
        return Student(student_id, user_id, kelas, tahun)

    def get_student_by_user_id(self, user_id):
        conn = sqlite3.connect(self.db_path)
        cur = conn.cursor()
        cur.execute("SELECT * FROM Student WHERE user_id = ?", (user_id,))
        row = cur.fetchone()
        conn.close()
        if row:
            return Student(*row)
        return None