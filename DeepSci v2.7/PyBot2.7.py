#!/usr/bin/python3.6
# -*- coding: utf-8 -*-

import vk_api
from vk_api.utils import get_random_id
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from Person import Person
from Hangman import Hangman
import requests
import random
import sys
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
        self.HANGMAN = {}


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

    def cprint(self, text):
        '''Сервер не вопринимает мир по UTF-8, он использует ASCII... Не будьте как сервер!'''
        try:
            print(text)
        except SyntaxError:
            print(text.encode('utf-8'))



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

    def commands(self, vk_session, event, PRIVILEGE):
        if PRIVILEGE >= 2:
            # CHAIRMAN or ADMIN
            pass
        if PRIVILEGE == 3:
            # ADMIN
            if event.text == "\exit":
                self.sendAnswer(vk_session, event, answer="DeepSci chat bot stops!")
                sys.exit()

    def createButton(self,message, vk_session, event):
        '''Создание кнопок для ФИЗИКИ'''
        # Печально, но если передать keybord как аргумент, то кнопки у пользователя не выводятся

        vk = vk_session.get_api()
        # Обрабатываем крайние случаи лекций, чтобы список не вылезал за границу (потому что на клаве лекции с номерами -1 0 +1 )
        if int(self.PHYS_NUM) == 1:
            self.PHYS_NUM = 2
        elif int(self.PHYS_NUM) == 11:
            self.PHYS_NUM = 10

        # Создаем клавиатуру
        keyboard = VkKeyboard(one_time=True)
        # - text в данном случае служит как часть кодового слова, которые находтся в массиве self.PHYSICS
        text = '-я лекция по ' + 'физике'
        # num - локальная переменная, которую мы выводим в списке выбора лекций
        num = self.PHYS_NUM - 1
        keyboard.add_button(str(num) + text, color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button(str(self.PHYS_NUM) + text, color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        # Добавляем +1 к текущим лекциям, ведь предыдущую он получил
        num = self.PHYS_NUM+1
        keyboard.add_button(str(num) + text, color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()

        keyboard.add_button('Хватит!', color=VkKeyboardColor.NEGATIVE)
        self.PHYS_NUM += 1
        vk.messages.send(user_id=event.user_id, random_id=get_random_id(), keyboard=keyboard.get_keyboard(), message=message)

    def menu(self, event, vk_session):
        keyboard = VkKeyboard(one_time=False)
        keyboard.add_button('Привет', color=VkKeyboardColor.SECONDARY)
        keyboard.add_line()
        keyboard.add_button('ВИСЕЛИЦА', color=VkKeyboardColor.PRIMARY)
        keyboard.add_button('ФИЗИКА', color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button('Хватит', color=VkKeyboardColor.NEGATIVE)
        vk_session.get_api().messages.send(user_id=event.user_id, random_id=get_random_id(), keyboard=keyboard.get_keyboard(),
                         message="Меню")

    def manageMessage(self, event, vk_session, person):
        self.cprint(person.USER)
        self.cprint("\t" + event.text + " - " + ctime())
        if event.text[0] == '\\':
            # Обработка команд от пользователя
            self.commands(vk_session, event, int(person.PRIVILEGE))

        elif self.antiMat(event.text):
            # Реакция на МАТюки
            answer = "Давайте притворимся, что я этого не слышала!"
            self.sendAnswer(vk_session, event, answer)

        elif "меню" == event.text.lower():
            self.menu(event, vk_session)

        elif person.ACTIVITY["HANGMAN"] == 1 and str(event.user_id) in self.HANGMAN:
            hangman = self.HANGMAN[str(event.user_id)]
            if "хватит" in event.text.lower():
                person.switchActivity("USUAL")
            elif len(event.text) != 1:
                self.sendAnswer(vk_session, event, "Сейчас ты играешь в Виселицу! Чтобы преждевременно закончить игру нажми на 'Хватит'")
            elif hangman.HP == 0:
                self.sendAnswer(vk_session, event, "У вас не осталось жизней!\nПопробуй угадать слово заново.")
                person.switchActivity("USUAL")
            else:
                if hangman.checkChar(event.text):
                    if hangman.checkWord():
                        self.sendAnswer(vk_session, event, "Поздравляем🎉!\nТы большой молодец✨!\nКак уже всем понятно, заданным словом было - " + hangman.SHOW + ".")
                        person.switchActivity("USUAL")
                    else:
                        self.sendAnswer(vk_session, event, "Буква " + event.text + " подошла!\nТеперь слово выглядит:\n" + hangman.SHOW)
                else:
                    hangman.HP -= 1
                    self.sendAnswer(vk_session, event, "Буква не подошла!\nУ тебя осталось " + str(hangman.HP) + "💙 жизней.\nВведи новую букву.")
            hangman.updateHangman()

        elif "физика" in event.text.lower():
            self.PHYS_NUM = 2
            # Сделать так, чтобы появились кнопки у пользователя
            self.createButton("Если хочешь подготовится к ЕГЭ по физике выбери нужную лекцию!", vk_session, event)

        elif "виселица" in event.text.lower():
            person.switchActivity("HANGMAN")
            hangman = Hangman(str(event.user_id))
            self.HANGMAN[str(event.user_id)] = hangman
            self.sendAnswer(vk_session, event, "Я загадал рандомное слово: " + hangman.SHOW + "\nПопробуй отгадать!"
                            + "\nУ тебя " + str(7) + "💙 жизней!\nЧтобы начать заново снова нажми на кнопку 'Виселица', а чтобы закончить - 'Хватит'")
            self.cprint("Загаданное слово - " + hangman.WORD)

        elif event.text in self.PHYSICS:
            # Инициализируем номер лекции
            self.PHYS_NUM = self.PHYSICS.index(event.text) + 1
            # Парсим список лекций из файла (parseText возвращает массив)
            lectures = self.parseText("Physics.txt", "UQ")
            # Проходим по лекциям и находим нужную нам под номером self.PHYS_NUM
            for lecture in lectures:
                if lecture[0] == str(self.PHYS_NUM):
                    message = "Лекция "+ str(self.PHYS_NUM) + ":\n" + lecture[1][0]
                    self.sendAnswer(vk_session, event, message)
                    # Не у всех лекций есть скрипты, поэтому обрабатываем их отдельно
                    if lecture[1][1]!='None':
                        message = "Скрипт по лекции:" + lecture[1][1]
                        self.sendAnswer(vk_session, event, message)
                    message = "Если тебе лень, посмотри мотивирующий ролик:" + lecture[1][2]
                    self.sendAnswer(vk_session, event, message)
            # вызываем фцнкцию заново
            self.createButton("Выбирай ещё!", vk_session, event)
        else:
            # Обрабатываем все другие сообщения
            answer = random.choice(self.elseMessages(event.text))
            self.sendAnswer(vk_session, event, answer)


    def runChatBot(self, vk_session):
        '''Запуск Чат Бота'''
        self.cprint("Запуск Чат Бота DeepSci!")

        longpoll = VkLongPoll(vk_session)
        for event in longpoll.listen():
            # Обработка ивента - сообщения
            if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
                # Создаем объект - пользователя
                person = Person(str(event.user_id), vk_session)
                self.OLD_MESSAGE = event.text
                self.manageMessage(event, vk_session, person)
                # Обновим информацию в базе
                person.updateJson()


# Запускаем нашу машинку
if __name__ == "__main__":
    # Уникальный токен сообщества
    token = "MyToken"
    myVkBot = vkBot(token)  # Создаем объект - чат бота
    vk_session = myVkBot.authorization() # Проходим авторизацию
    myVkBot.runChatBot(vk_session) # Запускаем
