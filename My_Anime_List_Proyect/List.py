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

        self.user_list.append(self.anime)
        self._sort_list()

    def _sort_list(self):
        swapped = True

        while swapped:
            swapped = False
            for i in range(len(self.user_list) - 1):
                if self.user_list[i + 1].score > self.user_list[i].score:
                    swapped = True
                    self.user_list[i], self.user_list[i + 1] = self.user_list[i + 1], self.user_list[i]
            
    def show_my_anime_list(self):
        counter = 1
        for i in self.user_list:
            print(f'{counter}.{i.show_data()}')
            counter += 1