import random
import tkinter

def get_word():
    wordlist = []
    with open("hangman_wordlist.txt", "r") as file:
        wordlist = file.read().split("\n")

    word = random.choice(wordlist)
    return word

get_word()


    

