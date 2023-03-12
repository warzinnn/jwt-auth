class User:
    def __init__(self, email: str, username: str, password: str, role: str) -> None:
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

    def __repr__(self) -> str:
        return f"User(email={self.email}, username={self.username}, password={self.passwd}, role={self.role})"

    def __eq__(self, other):
        if isinstance(other, User):
            if (
                other.email == self.email
                and other.username == self.username
                and other.passwd == self.passwd
                and other.role == self.role
            ):
                return True
        return False
