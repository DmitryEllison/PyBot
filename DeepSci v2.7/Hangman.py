import random

class Hangman:
    def __init__(self, ID):
        self.ID = ID
        self.WORD = self.randomWords("Words.txt").upper()
        self.KEY = '0'*len(self.WORD)
        self.SHOW = '*'*len(self.WORD)
        self.HP = 7
        self.HANGMAN = {}
        self.updateHangman()

    def updateHangman(self):
        self.HANGMAN = {self.ID: {"WORD": self.WORD, "KEY": self.KEY, "SHOW": self.SHOW, "HP": 7}}

    def checkChar(self, char):
        change = False
        for i, ch in enumerate(self.WORD):
            if char.upper() == ch:
                self.SHOW = self.SHOW[:i] + ch + self.SHOW[i+1:]
                self.KEY = self.KEY[:i] + "1" + self.KEY[i+1:]
                change = True
        self.updateHangman()
        return change

    def randomWords(self, name):
        with open(name, 'r', encoding="utf-8") as file:
            return random.choice(file.read().split("\n"))

    def checkWord(self):
        for i in self.SHOW:
            if i == '*':
                return False
        return True

