import sqlite3
from models.course import Course

class CourseController:
    def __init__(self, db_path='database.db'):
        self.db_path = db_path

    def create_course(self, name, deskripsi, teacher_id):
        conn = sqlite3.connect(self.db_path)
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO Course (name, deskripsi, teacher_id) VALUES (?, ?, ?)",
            (name, deskripsi, teacher_id)
        )
        conn.commit()
        course_id = cur.lastrowid
        conn.close()
        return Course(course_id, name, deskripsi, teacher_id)

    def get_all_courses(self):
        conn = sqlite3.connect(self.db_path)
        cur = conn.cursor()
        cur.execute("SELECT * FROM Course")
        rows = cur.fetchall()
        conn.close()
        return [Course(*row) for row in rows]

    def get_course_by_id(self, course_id):
        conn = sqlite3.connect(self.db_path)
        cur = conn.cursor()
        cur.execute("SELECT * FROM Course WHERE course_id = ?", (course_id,))
        row = cur.fetchone()
        conn.close()
        if row:
            return Course(*row)
        return None