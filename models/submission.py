class Submission:
    def __init__(self, submission_id, assignment_id, student_id, file_url, nilai, timestamp):
        self.submission_id = submission_id
        self.assignment_id = assignment_id
        self.student_id = student_id
        self.file_url = file_url
        self.nilai = nilai
        self.timestamp = timestamp

    def __repr__(self):
        return f"<Submission {self.submission_id} assignment:{self.assignment_id} student:{self.student_id}>"