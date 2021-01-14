import vk_api
from vk_api.utils import get_random_id
from vk_api.longpoll import VkLongPoll, VkEventType
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
                return random.choice(dialog[1])
        else:
            return "Команда не опознана!"



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


    def runChatBot(self, vk_session):
        '''Запуск Чат Бота'''
        print("Запуск Чат Бота DeepSci!")

        longpoll = VkLongPoll(vk_session)
        for event in longpoll.listen():
            # Обработка ивента - сообщения
            if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
                print(event.text + " - " + ctime())
                if self.antiMat(event.text):
                    answer = "Давайте притворимся, что я этого не слышала!"
                    print(answer+ " - " + ctime())
                    self.sendAnswer(vk_session, event, answer)
                elif "ФИЗИКА" in event.text:
                    self.sendAnswer(vk_session, event, "Если ты хочешь подготовиться к ЕГЭ по физике, то выбери лекцию, которую хочешь посмотреть!")
                    # Сделать так, чтобы появились кнопки у пользователя
                else:
                    answer = self.elseMessages(event.text)
                    print(answer+ " - " + ctime())
                    self.sendAnswer(vk_session, event, answer)

# Запускаем нашу машинку
if __name__ == "__main__":
    # Уникальный токен сообщества
    token = "1683bfc2fae91ae2023865fa1431382b2014a83270b5f784a971cd8506077b0ffe12e36bf8016ab129bf6"
    myVkBot = vkBot(token)  # Создаем объект - чат бота
    vk_session = myVkBot.authorization() # Проходим авторизацию
    myVkBot.runChatBot(vk_session) # Запускаем
