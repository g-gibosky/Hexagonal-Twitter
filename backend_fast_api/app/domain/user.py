class User:
    def __init__(self, username: str, email: str, id: int = None): # type: ignore
        self.id = id
        self.username = username
        self.email = email
