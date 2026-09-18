class User:
    def __init__(self, id=None, username=None, password=None):
        self.id = id
        self.username = username
        self.password = password  # hash, jamais en clair

    @classmethod
    def from_dict(cls, data):
        return cls(
            id=data.get("id"),
            username=data.get("username"),
            password=data.get("password"),
        )

    def __repr__(self):
        return f"<User id={self.id} username='{self.username}'>"