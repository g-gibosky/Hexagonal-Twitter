class Tweet:
    def __init__(self, content: str, author_id: int, id: int = None): # type: ignore
        self.id = id
        self.content = content
        self.author_id = author_id
