import os
from model.user import User

class UsuarioService:
    def __init__(self, filepath):
        self.filepath = filepath

    def get_all_users(self):
        users = []
        if not os.path.exists(self.filepath):
            return users

        with open(self.filepath, 'r', encoding='utf-8') as f:
            for line in f:
                parts = line.strip().split(',')
                if len(parts) == 3:
                    users.append(User(*parts))
        return users

    def save_all_users(self, users):
        with open(self.filepath, 'w', encoding='utf-8') as f:
            for user in users:
                f.write(user.to_line())

    def create_user(self, username, password, role='usuario'):
        users = self.get_all_users()
        if any(u.username == username for u in users):
            return False
        users.append(User(username, password, role))
        self.save_all_users(users)
        return True

    def update_user(self, username, password=None, role=None):
        users = self.get_all_users()
        updated = False
        for u in users:
            if u.username == username:
                if password:
                    u.password = password
                if role:
                    u.role = role
                updated = True
                break
        if updated:
            self.save_all_users(users)
        return updated

    def delete_user(self, username):
        users = self.get_all_users()
        new_users = [u for u in users if u.username != username]
        if len(users) == len(new_users):
            return False
        self.save_all_users(new_users)
        return True
