from flask_login import UserMixin

class User(UserMixin):
    def __init__(self, username, flags_solved) -> None:
        self.id = username
        self.flags_solved = flags_solved