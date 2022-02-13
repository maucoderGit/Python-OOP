class Character:

    _id: int
    name: str
    age: int
    phrase: str
    anime: str
    status: str
    score: int

    def __init__(self,_id: int, name:str, age:int, anime:str, status: str):
        self._id = _id
        self.name : str = name
        self.age : int = age or "Unknow"
        self.anime: str = anime
        self.status: str = status

    def add_phrase(self, phrase):
        self.phrase = phrase

    def valoration(self, score):
        self.score = score

    def sumarry_character(self):
        return f'Name: {self.name}, from: {self.anime}, Age: {self.age}, Phrase: {self.phrase or ""}'