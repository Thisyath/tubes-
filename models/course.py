class Course:
    def __init__(self, course_id, name, deskripsi, teacher_id):
        self.course_id = course_id
        self.name = name
        self.deskripsi = deskripsi
        self.teacher_id = teacher_id

    def __repr__(self):
        return f"<Course {self.course_id} {self.name}>"