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
        self._long = len(self.user_list)

        try:
            if self._long == 0:
                self.user_list.append(self.anime)
            else:
                self.user_list.append(self.anime)
                # self._ranking(self.user_list[self._count])
                self._sort_list(self._long)
        except IndexError as error:
            print(error)

    def _sort_list(self, iterations):
        self._count = 0
        iterations -= 1
        counter: int = self._long
        
        try:
            while counter > 0:
              
                iterator_1 = self.user_list[self._count]
                iterator_2 = self.user_list[self._count + 1]
    
                if iterator_1.score > iterator_2.score:
                    self.user_list[self._count] = iterator_1
                else:
                    self.user_list[self._count] = iterator_2
                    self.user_list[self._count + 1] = iterator_1

                self._count += 1
            
        except IndexError as error:
            if iterations > 0:
                return(self._sort_list(iterations))

            
    # def _set_position(self):
    #     if self.user_list[self._position] == self.anime:
    #         return True
    #     else:
    #         return False

    def show_my_anime_list(self):
        counter = 1
        for i in self.user_list:
            print(f'{counter}.{i.show_data()}')
            counter += 1

    def _lenght_validator(self):
        if self._long >= self._count + 1:
            return True
        else:
            return False