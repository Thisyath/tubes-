import sqlite3
from models.user import User
from utils.password import hash_password, verify_password

class UserController:
    def __init__(self, db_path='database.db'):
        self.db_path = db_path

    def create_user(self, username, email, password):
        conn = sqlite3.connect(self.db_path)
        cur = conn.cursor()
        hashed_password = hash_password(password)
        try:
            cur.execute(
                "INSERT INTO User (username, email, password) VALUES (?, ?, ?)",
                (username, email, hashed_password)
            )
            conn.commit()
            user_id = cur.lastrowid
            return User(user_id, username, email, hashed_password)
        except sqlite3.IntegrityError:
            return None
        finally:
            conn.close()

    def get_user_by_username(self, username):
        conn = sqlite3.connect(self.db_path)
        cur = conn.cursor()
        cur.execute("SELECT * FROM User WHERE username = ?", (username,))
        row = cur.fetchone()
        conn.close()
        if row:
            return User(*row)
        return None

    def verify_user(self, username, password):
        user = self.get_user_by_username(username)
        if user and verify_password(password, user.password):
            return user
        return None