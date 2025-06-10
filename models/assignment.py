class Assignment:
    def __init__(self, assignment_id, title, due_date, course_id):
        self.assignment_id = assignment_id
        self.title = title
        self.due_date = due_date
        self.course_id = course_id

    def __repr__(self):
        return f"<Assignment {self.assignment_id} {self.title}>"