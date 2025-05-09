class User:
    def __init__(self, username, password, role='usuario'):
        self.username = username
        self.password = password
        self.role = role

    def to_dict(self):
        return {
            'username': self.username,
            'role': self.role
        }

    def to_line(self):
        return f"{self.username},{self.password},{self.role}\n"
