#!/usr/bin/python3.6
import requests
import json
import vk_api


class Person():
    def __init__(self, ID, vk_session):
        '''Инициализация переменных'''
        self.USER = {}
        if self.checkUser(ID):
            self.readUser(ID)
            self.ID = str(ID)
            self.PRIVILEGE = self.USER[ID]["PRIVILEGE"]
            # "ADMIN": 3, "CHAIRMAN": 2, "USER": 1
            self.FIRST_NAME = self.USER[ID]["FIRST_NAME"]
            self.LAST_NAME = self.USER[ID]["LAST_NAME"]
            # self.MESSAGES = {}
            self.ACTIVITY = self.USER[ID]["ACTIVITY"]
        else:
            user = vk_session.method("users.get", {"user_ids": ID})
            self.ID = ID
            self.PRIVILEGE = "1"
            #"ADMIN": 3, "CHAIRMAN": 2, "USER": 1
            self.FIRST_NAME = user[0]['first_name']
            self.LAST_NAME = user[0]['last_name']
            #self.MESSAGES = {}
            self.ACTIVITY = {"USUAL": 1,
                             "HANGMAN": 0}
        self.initUser()

    def toString(self):
        '''Возвращает строчное представление пользователя'''
        return "User ID: " + str(self.ID) + ";\nPRIVILEGE: " + str(self.PRIVILEGE)
        + ";\nFIRST_NAME: " + self.FIRST_NAME + ";\nLAST_NAME" + self.LAST_NAME + ";\n"

    def returnAllMessages(self):
        '''Возвращает все сообщения'''
        return False #self.MESSAGES

    def checkUser(self, ID):
        '''Проверяет есть ли пользователь в базе'''
        try:
            f = open('USERS/'+ str(ID) +'.json')
            f.close()
            return True
        except FileNotFoundError:
            return False

    def updateJson(self):
        '''Обновляет базу пользователей в файле USERS/ID.json'''
        with open('USERS/'+ str(self.ID) +'.json', 'w') as f:
            f.write(json.dumps(self.USER, indent=4))

    def readUser(self, ID):
        '''Считывает пользователей из базы'''
        with open('USERS/' + str(ID) + '.json') as file:
            self.USER = json.loads(file.read())

    def initUser(self):
        '''Инициализирует пользователя'''
        self.USER[str(self.ID)] = {
            "PRIVILEGE": self.PRIVILEGE,
            "FIRST_NAME": self.FIRST_NAME,
            "LAST_NAME": self.LAST_NAME,
            #"MESSAGES": self.MESSAGES,
            "ACTIVITY": self.ACTIVITY
        }
        self.updateJson()

    def switchActivity(self, ACTIVITY):
        for key, value in self.ACTIVITY.items():
            print(key, value)
            if key == ACTIVITY:
                self.ACTIVITY[ACTIVITY] = 1
            elif key != ACTIVITY and value == 1:
                self.ACTIVITY[key] = 0
        self.initUser()
