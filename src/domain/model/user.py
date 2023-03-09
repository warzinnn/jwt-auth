class User:
    def __init__(
        self, id: int, email: str, username: str, password: str, role: str
    ) -> None:
        self.id = id
        self.email = email
        self.username = username
        self.passwd = password
        self.role = role

    def as_dict(self):
        return {
            "email": self.email,
            "username": self.username,
            "password": self.passwd,
            "role": self.role,
        }
