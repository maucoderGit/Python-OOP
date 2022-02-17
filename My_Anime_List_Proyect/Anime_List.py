from character import Character

class Anime:
    _id: int
    name: str
    characters: object = Character(int ,str, int, str, str)
    category: str
    score: int

    def __init__(self, _id: int, name : str, category:str, score: int):
        self._id = _id
        self.name = name
        self.category = category
        self.score = score

    def show_data(self):
        return (f'Name: {self.name}, Category: {self.category}, Score: {self.score}')