#!/usr/bin/python3.6

import vk_api
from vk_api.utils import get_random_id
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
import requests
import random
from time import ctime

class vkBot():
    def __init__(self, token):
        self.token = token
        self.Type = {"SET": 0, "UQ": 1}
        self.BAD_WORDS = "BadWords.txt"
        self.LECTURE_ON_PHYSICS = "Physics.txt"
        self.ANSWERS = "Answers.txt"
        self.OLD_MESSAGE = ""
        self.PHYSICS = ["1-я лекция по физике", "2-я лекция по физике", "3-я лекция по физике",
                        "4-я лекция по физике", "5-я лекция по физике", "6-я лекция по физике",
                        "7-я лекция по физике", "8-я лекция по физике", "9-я лекция по физике",
                        "10-я лекция по физике", "11-я лекция по физике"]
        self.PHYS_NUM = 2


    def authorization(self):
        '''Авторизация'''
        session = requests.Session()
        vk_session = vk_api.VkApi(token=self.token)
        return vk_session

    def antiMat(self, message):
        '''Проверяет сообщение на мат'''
        bad_words = self.parseText(self.BAD_WORDS, "SET")
        for word in bad_words:
            if word.lower() in message.lower():
                return True
        return False


    def elseMessages(self, message):
        '''Обработка всех остальных сообщений'''
        answers = self.parseText(self.ANSWERS, "UQ")

        for dialog in answers:
            if dialog[0] in message.lower():
                return dialog[1]
        else:
            return [message]


    def parseText(self, name, type):
        '''Обрабатывает файлы ответов на сообщения'''
        r = open(name, "r", encoding="utf-8")
        text = r.read().replace("'", "")
        if self.Type[type] == 0:
            return text.replace(" ", "").split(",")
        elif self.Type[type] == 1:
            dialogs = text.replace("'", "").split(";")
            arr = []
            for i, value in enumerate(dialogs):
                arr.append(value.split(":", 1))
            for i  in arr:
                if len(i) >= 2:
                    i[1] = i[1].split(",")

            return arr


    def sendAnswer(self, vk_session, event, answer):
        '''Отправка ответного сообщения'''
        vk = vk_session.get_api()
        vk.messages.send(user_id=event.user_id, random_id=get_random_id(), message=answer)


    def createButton(self,message, vk_session, event):
        '''Создание кнопок для ФИЗИКИ'''
        # Печально не если передать keybord как аргумент, то кнопки у пользователя не выводятся
        keybord = VkKeyboard(one_time=True)
        vk = vk_session.get_api()
        if int(self.PHYS_NUM) == 1:
            self.PHYS_NUM = 2
        elif int(self.PHYS_NUM) == 11:
            self.PHYS_NUM = 10

        keyboard = VkKeyboard(one_time=True)
        num = self.PHYS_NUM-1
        # Возможно позже можно будет расширить функционал не только для лекций по физике
        text = '-я лекция по ' + 'физике'
        keyboard.add_button(str(num) + text, color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button(str(self.PHYS_NUM) + text, color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        num = self.PHYS_NUM+1
        keyboard.add_button(str(num) + text, color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button('Хватит!', color=VkKeyboardColor.NEGATIVE)
        self.PHYS_NUM += 1

        vk.messages.send(
            user_id=event.user_id,
            random_id=get_random_id(),
            keyboard=keyboard.get_keyboard(),
            message=message
        )


    def manageMessage(self, event, vk_sessioan):
        print(event.text + " - " + ctime())

        if self.antiMat(event.text):
            answer = "Давайте притворимся, что я этого не слышала!"
            print("PyBot: " + answer + " - " + ctime())
            self.sendAnswer(vk_session, event, answer)
        elif "ФИЗИКА" in event.text:
            self.PHYS_NUM = 2
            # Сделать так, чтобы появились кнопки у пользователя
            self.createButton("Если хочешь подготовится к ЕГЭ по физике выбери нужную лекцию!", vk_session, event)
            print("User with " + str(event.user_id) + " ID asking for Lecture of Phyisics!")

        elif event.text in self.PHYSICS:
            self.PHYS_NUM = self.PHYSICS.index(event.text) + 1
            lectures = self.parseText("Physics.txt", "UQ")
            for lecture in lectures:
                if lecture[0] == str(self.PHYS_NUM):
                    message = "Лекция "+ str(self.PHYS_NUM) + ":\n" + lecture[1][0]
                    self.sendAnswer(vk_session, event, message)
                    if lecture[1][1]!='None':
                        message = "Скрипт по лекции:" + lecture[1][1]
                        self.sendAnswer(vk_session, event, message)
                    message = "Если тебе лень, посмотри ролик:" + lecture[1][2]
                    self.sendAnswer(vk_session, event, message)


            self.createButton("Выбирай ещё!", vk_session, event)
        else:
            answer = random.choice(self.elseMessages(event.text))
            print(answer + " - " + ctime())
            self.sendAnswer(vk_session, event, answer)


    def runChatBot(self, vk_session):
        '''Запуск Чат Бота'''
        print("Запуск Чат Бота DeepSci!")

        longpoll = VkLongPoll(vk_session)
        for event in longpoll.listen():
            # Обработка ивента - сообщения
            if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
                self.OLD_MESSAGE = event.text
                self.manageMessage(event, vk_session)


# Запускаем нашу машинку
if __name__ == "__main__":
    # Уникальный токен сообщества
    token = "1683bfc2fae91ae2023865fa1431382b2014a83270b5f784a971cd8506077b0ffe12e36bf8016ab129bf6"
    myVkBot = vkBot(token)  # Создаем объект - чат бота
    vk_session = myVkBot.authorization() # Проходим авторизацию
    myVkBot.runChatBot(vk_session) # Запускаем