import sqlite3
from models.enrollment import Enrollment

class EnrollmentController:
    def __init__(self, db_path='database.db'):
        self.db_path = db_path

    def enroll_student(self, student_id, course_id):
        conn = sqlite3.connect(self.db_path)
        cur = conn.cursor()
        cur.execute(
            "INSERT OR IGNORE INTO Enrollment (student_id, course_id) VALUES (?, ?)",
            (student_id, course_id)
        )
        conn.commit()
        enrollment_id = cur.lastrowid
        conn.close()
        return Enrollment(enrollment_id, student_id, course_id)

    def get_courses_by_student(self, student_id):
        conn = sqlite3.connect(self.db_path)
        cur = conn.cursor()
        cur.execute("SELECT * FROM Enrollment WHERE student_id = ?", (student_id,))
        rows = cur.fetchall()
        conn.close()
        return [Enrollment(*row) for row in rows]

    def get_students_by_course(self, course_id):
        conn = sqlite3.connect(self.db_path)
        cur = conn.cursor()
        cur.execute("SELECT * FROM Enrollment WHERE course_id = ?", (course_id,))
        rows = cur.fetchall()
        conn.close()
        return [Enrollment(*row) for row in rows]