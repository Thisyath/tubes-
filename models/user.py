class User:
    def __init__(self, user_id, username, email, password):
        self.user_id = user_id
        self.username = username
        self.email = email
        self.password = password

    def __repr__(self):
        return f"<User {self.user_id} {self.username}>"