from character import Character

class Anime:
    _id: int
    name: str
    characters: object = Character(int ,str, int)
    soundtrack: str
    category: str
    score: int

    def __init__(self, _id, name : str, category:str, score: int):
        self._id = _id
        self.name = name
        self.category = category
        self.score = score