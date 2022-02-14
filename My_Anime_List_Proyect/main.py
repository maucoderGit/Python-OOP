from character import Character
from Anime_List import Anime
from List import List


def run():
    Character_1: object = Character(1, "Okabe Rintarou", "18", "Steins;Gate", "Live")
    Anime_1: object = Anime(1, "Steis;Gate", "Seinen", 10)

    Character_2: object =  Character(2, "Kamina", 16, "Tengenn toppa Gurren lagann", "Live")
    Anime_2: object = Anime(2, "Tengenn toppa Gurren lagann", "Mecha", 10)

    new_list = List("My_anime_list", "Maucoder")
    new_list.add_anime(Anime_2)

    new_list.add_anime(Anime_1)

    new_list.show_my_anime_list()
    # ranking(Anime_2)

if __name__ == "__main__":
    run()