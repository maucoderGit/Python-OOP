# import tkinter as tk
from character import Character
from Anime_List import Anime
from List import List


def run():
    Character_1: object = Character(1, "Okabe Rintarou", "18", "Steins;Gate", "Live")
    Anime_1: object = Anime(1, "Steis;Gate", "Seinen", 10)

    Character_2: object =  Character(2, "Kamina", 16, "Tengenn toppa Gurren lagann", "Live")
    Anime_2: object = Anime(2, "Tengenn toppa Gurren lagann", "Mecha", 9)

    Character_3: object = Character(3, "Monkey D. Luffy", 19, "God Piece", "live")
    Anime_3: object = Anime(3, "God Piece", "Shonen", 8)

    Anime_4: object = Anime(4, "Noragami", "Shonen", 7)
    Anime_5: object = Anime(5, "Full Metal Archemist", "Shonen", 10)

    new_list = List("My_anime_list", "Maucoder")

    new_list.add_element(Anime_4)
    new_list.add_element(Anime_2)
    new_list.add_element(Anime_1)
    new_list.add_element(Anime_3)
    new_list.add_element(Anime_5)
    new_list.add_element(Anime_1)

    new_list.show_my_list()

if __name__ == "__main__":
    run()