import sqlite3
from models.material import Material

class MaterialController:
    def __init__(self, db_path='database.db'):
        self.db_path = db_path

    def create_material(self, title, file_url, course_id):
        conn = sqlite3.connect(self.db_path)
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO Material (title, file_url, course_id) VALUES (?, ?, ?)",
            (title, file_url, course_id)
        )
        conn.commit()
        material_id = cur.lastrowid
        conn.close()
        return Material(material_id, title, file_url, course_id)

    def get_materials_by_course(self, course_id):
        conn = sqlite3.connect(self.db_path)
        cur = conn.cursor()
        cur.execute("SELECT * FROM Material WHERE course_id = ?", (course_id,))
        rows = cur.fetchall()
        conn.close()
        return [Material(*row) for row in rows]

    def get_material_by_id(self, material_id):
        conn = sqlite3.connect(self.db_path)
        cur = conn.cursor()
        cur.execute("SELECT * FROM Material WHERE material_id = ?", (material_id,))
        row = cur.fetchone()
        conn.close()
        if row:
            return Material(*row)
        return None