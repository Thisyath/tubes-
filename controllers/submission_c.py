import sqlite3
from models.submission import Submission

class SubmissionController:
    def __init__(self, db_path='database.db'):
        self.db_path = db_path

    def submit_assignment(self, assignment_id, student_id, file_url, nilai=None, timestamp=None):
        conn = sqlite3.connect(self.db_path)
        cur = conn.cursor()
        cur.execute(
            "INSERT OR REPLACE INTO Submission (assignment_id, student_id, file_url, nilai, timestamp) VALUES (?, ?, ?, ?, ?)",
            (assignment_id, student_id, file_url, nilai, timestamp)
        )
        conn.commit()
        submission_id = cur.lastrowid
        conn.close()
        return Submission(submission_id, assignment_id, student_id, file_url, nilai, timestamp)

    def get_submissions_by_assignment(self, assignment_id):
        conn = sqlite3.connect(self.db_path)
        cur = conn.cursor()
        cur.execute("SELECT * FROM Submission WHERE assignment_id = ?", (assignment_id,))
        rows = cur.fetchall()
        conn.close()
        return [Submission(*row) for row in rows]

    def get_submission_by_student_and_assignment(self, student_id, assignment_id):
        conn = sqlite3.connect(self.db_path)
        cur = conn.cursor()
        cur.execute("SELECT * FROM Submission WHERE student_id = ? AND assignment_id = ?", (student_id, assignment_id))
        row = cur.fetchone()
        conn.close()
        if row:
            return Submission(*row)
        return None