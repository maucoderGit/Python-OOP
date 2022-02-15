from Anime_List import Anime

class List():

    user_list: list
    list_name: str
    user: str
    anime: object = Anime(int, str, str, int)
    count: int

    def __init__(self, list_name:str, user:str):
        self.user_list:list = []
        self.list_name:str = list_name
        self.user:str = user


    def add_anime(self, anime: object):
        self.anime = anime
        print(self.anime)
        self._count = 0

        # binary search Idea
        # self.counter = int(len(self.user_list) / 2)
        try:
            if len(self.user_list) == 0:
                self.user_list.append(self.anime)
            else:
                self.user_list[self._count] = self._ranking(self.user_list[self._count])
        except IndexError:

            # add self.anime to last position in array
            self.user_list.append(self.anime)
            self._sort_list()

    def _ranking(self, other_rank_score:int):
        if self.anime.score < other_rank_score.score:
            self._count += 1
            self._ranking(self.user_list[self._count])
        else:
            self.user_list[self._count + 1] = other_rank_score
            self._count += 1

                # self._ranking(other_rank_score)
       
    def _sort_list(self):
        try:
            iterations: int = len(self.user_list)
            # self.user_list[self._count]: object = self.anime
            # self.user_list.append(self.anime)
            
            while iterations > 0:
                iterator_1 = self.user_list[self._count]
                iterator_2 = self.user_list[self._count + 1]

                if self._set_position() !=  True:
                    self.user_list[self._count] = self.anime

                self.user_list[self._count + 1] = iterator_1

                iterations -= 1
                self._count += 1
        
        except IndexError:
            self._count = 0
            # self.user_list.append(self.user_list[self._count])

    def _set_position(self):
        if self.user_list[self._count] == self.anime:
            return True
        else:
            return False

    def show_my_anime_list(self):
        counter = 1
        for i in self.user_list:
            print(f'{counter}.{i.show_data()}')
            counter += 1