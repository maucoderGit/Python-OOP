from Anime_List import Anime
from character import Character

class List:

    finished: bool
    ranker: object = Anime(int, str, str, str, float)
    fav_character: object = Character(int, str, int, str, str)
    _rank: int

    def __init__(self, finished, hype, ranker):
        self.finished: bool = finished
        self.ranker = ranker
        self._ranking = ranking()

    def _ranking(self, other_rank):
        if self.ranker.score < other_rank:
            self._rank += 1
            _ranking(self, other_rank)
        elif self.ranker.score > other_rank:
            self._rank -= 1
            _ranking(self, other_rank)
        else:
            print(f'{self.ranker.name} rank is {self._rank}')
            return self._rank