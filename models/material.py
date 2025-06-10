class Material:
    def __init__(self, material_id, title, file_url, course_id):
        self.material_id = material_id
        self.title = title
        self.file_url = file_url
        self.course_id = course_id

    def __repr__(self):
        return f"<Material {self.material_id} {self.title}>"