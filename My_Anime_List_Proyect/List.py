from Anime_List import Anime

class List():

    user_list: list = []
    list_name: str
    user: str
    anime: object = Anime(int, str, str, int)
    count: int
    _rank: int

    def __init__(self, list_name:str, user:str):
        self.user_list:list = []
        self.list_name:str = list_name
        self.user:str = user


    def add_anime(self, anime: object):
        self.anime = anime
        self._count = 0

        # binary search Idea
        # self.counter = int(len(self.user_list) / 2)
       
        try:
            self.user_list = self._ranking(self.user_list[self._count])
        except IndexError:
            self.user_list.append(self.anime)
          

    def _ranking(self, other_rank_score:int):
        if self.anime.score < other_rank_score.score:
            self._count += 1
            self._ranking(self.user_list[self._count])
        else:
            iterator = len(self.user_list)
            while iterator > 0:
                self.user_list[self._count + 1] = self.user_list[self._count]
                iterator - 1

            self._count = 0
            self.user_list[self._count] = self.anime
            return self.user_list

    def show_my_anime_list(self):
        counter = 1
        for i in self.user_list:
            print(f'{counter}.{i.name}')
            counter += 1