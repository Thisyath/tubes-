class Teacher:
    def __init__(self, teacher_id, user_id, departemen, spesialisasi):
        self.teacher_id = teacher_id
        self.user_id = user_id
        self.departemen = departemen
        self.spesialisasi = spesialisasi

    def __repr__(self):
        return f"<Teacher {self.teacher_id} user:{self.user_id}>"