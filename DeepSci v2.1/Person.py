#!/usr/bin/python3.6

class Person():
    # Static variable
    USERS = []
    def __init__(self, ID):
        self.ID = ID
        self.MESSAGES = {}
        self.ACTIVITY = {"HANGMAN": 0}
        self.PRIVILEGE = {"ADMIN": 0,
                          "CHAIRMAN": 0,
                          "USER": 1}
        self.USERS.append(ID)

    def initTheAdmin(self, ID):
        pass


    def toString(self):
        return "User ID: " + str(self.ID) + ";\n"

    def returnAllMessages(self):
        return self.MESSAGES

person1 = Person(12345)
print(person1.toString())
print(person1.USERS)
person2 = Person(54321)
print(person2.toString())

print(person2.USERS)
