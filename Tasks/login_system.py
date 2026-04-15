class signup:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def register(self):
        print(f"User {self.username} registered successfully.")

class login:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def authenticate(self):
        print(f"User {self.username} authenticated successfully.")
