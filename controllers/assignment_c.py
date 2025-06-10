import sqlite3
from models.assignment import Assignment

class AssignmentController:
    def __init__(self, db_path='database.db'):
        self.db_path = db_path

    def create_assignment(self, title, due_date, course_id):
        conn = sqlite3.connect(self.db_path)
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO Assignment (title, due_date, course_id) VALUES (?, ?, ?)",
            (title, due_date, course_id)
        )
        conn.commit()
        assignment_id = cur.lastrowid
        conn.close()
        return Assignment(assignment_id, title, due_date, course_id)

    def get_assignments_by_course(self, course_id):
        conn = sqlite3.connect(self.db_path)
        cur = conn.cursor()
        cur.execute("SELECT * FROM Assignment WHERE course_id = ?", (course_id,))
        rows = cur.fetchall()
        conn.close()
        return [Assignment(*row) for row in rows]

    def get_assignment_by_id(self, assignment_id):
        conn = sqlite3.connect(self.db_path)
        cur = conn.cursor()
        cur.execute("SELECT * FROM Assignment WHERE assignment_id = ?", (assignment_id,))
        row = cur.fetchone()
        conn.close()
        if row:
            return Assignment(*row)
        return None