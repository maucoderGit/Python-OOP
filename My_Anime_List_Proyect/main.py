from character import Character
from Anime_List import Anime
from List import List

def ranking(self, other_rank):
    if self.ranker.score < other_rank:
        self._rank += 1
        _ranking(self, other_rank)
    elif self.ranker.score > other_rank:
        self._rank -= 1
        _ranking(self, other_rank)
    else:
        print(f'{self.ranker.name} rank is {self._rank}')
        return self._rank

def run():
    Character_1: object = Character(1, "Okabe Rintarou", "18", "Steins;Gate", "Live")
    Anime_1: object = Anime(1, "Steis;Gate", "Seinen", 10.0)


if __name__ == "__main__":
    run()