class Enrollment:
    def __init__(self, enrollment_id, student_id, course_id):
        self.enrollment_id = enrollment_id
        self.student_id = student_id
        self.course_id = course_id

    def __repr__(self):
        return f"<Enrollment {self.enrollment_id} student:{self.student_id} course:{self.course_id}>"