import time
import vk_api
import requests
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id
from vk_api import VkUpload
from time import ctime
import random
print("Запуск...")
cyrcle = False
session = requests.Session()
command = ['мем',]
foo = [' Дойдя до конца, люди смеются над страхами, мучившими их вначале. \nПауло Коэльо',
       'Если ты не знаешь, чего хочешь, ты в итоге останешься с тем, чего точно не хочешь. \nЧак Паланик',
       'Чтобы дойти до цели, надо идти. \nОноре де Бальзак', 'Это своего рода забава, делать невозможное. \nУолт Дисней',
       'Если люди не смеются над вашими целями, значит ваши цели слишком мелкие. \nАзим Премжи',
       'Пробуйте и терпите неудачу, но не прерывайте ваших стараний. \nСтивен Каггва',
       'К черту все! Берись и делай! \nРичард Брэнсон',
       'Мы сами должны стать теми переменами, которые хотим видеть в мире. \nМахатма Ганди',
       'Препятствия – это те страшные вещи, которые вы видите, когда отводите глаза от цели. \nГенри Форд',
       'Постановка целей является первым шагом на пути превращения мечты в реальность. \nТони Роббинс',
       'Быть самым богатым человеком на кладбище для меня не важно… Ложиться спать и говорить себе, что сделал действительно нечто прекрасное, - вот что важно! \nСтив Джобс',
       'Через осуществление великих целей человек обнаруживает в себе и великий характер, делающий его маяком для других. \nГеорг Гегель',
       'Мы должны вызывать, а не ждать вдохновения, чтобы начать дело. Действие всегда порождает вдохновение. Вдохновение редко порождает действие. \nФрэнк Тиболт',
       'Когда вы знаете, чего хотите, и вы хотите этого достаточно сильно, вы найдете способ получить это. \nДжим Рон',
       'Я трачу почти все свое время на Facebook. У меня практически нет времени на новые увлечения. Поэтому я ставлю перед собой четкие цели. \nМарк Цукенберг',
       'Чтобы достичь поставленных целей, нужны терпение и энтузиазм. Мыслите глобально – но будьте реалистами. \nДональд Трамп',
       'Самый опасный яд – чувство достижения цели. Противоядие к которому – каждый вечер думать, что можно завтра сделать лучше. \nИнгвар Кампрад',
       'Вы не можете позволить себе ждать отличных состояний. Постановка целей – часто вопрос балансирования между временем и доступными ресурсами. Возможности легко потерять, ожидая подходящее время. \nГэри Райан Блэр',
       'Пуля, просвистевшая на дюйм от цели, так же бесполезна, как та, что не вылетала из дула. \nФенимор Купер',
       ' Никогда, никогда не позволяйте другим убедить вас, что что-то сложно или невозможно. \nДуглас Бадлер',
       'Заебал прокастинировать! Иди на хуй работать!\nДмитрий Золотарев ']

'''
Клише
elif '' in event.text.lower():
   msg()
'''

# Авторизация
vk_session = vk_api.VkApi(token='f3e21bc3a1bd758dcaa6a18b6455a034c215f1e724182591b5f0f243cc7c1e3810b9a1d843ae6f71a8820')

longpoll = VkLongPoll(vk_session)
vk = vk_session.get_api()

# Сообщение для пользователей
def msg(out):
    vk.messages.send(user_id=event.user_id, random_id=get_random_id(), message=out)

def msg2(msg, msg2):
    vk.messages.send(user_id=event.user_id, random_id=get_random_id(), message=msg)
    vk.messages.send(user_id=event.user_id, random_id=get_random_id(), message=msg2)

# Фотка
def photo(url):
    attachments = []
    upload = VkUpload(vk_session)
    image_url = url
    image = session.get(image_url, stream=True)
    photo = upload.photo_messages(photos=image.raw)[0]
    attachments.append('photo{}_{}'.format(photo['owner_id'], photo['id']))
    vk.messages.send(user_id=event.user_id, random_id=get_random_id(), attachment=','.join(attachments),message='')
    print("Фотка пошла..." + ctime())


# Егэ видос
def ege(url):
    vk.messages.send(user_id=event.user_id, random_id=get_random_id(), message='Хочешь подготовиться к ЕГЭ?🤓')
    vk.messages.send(user_id=event.user_id, random_id=get_random_id(),message=url)

# Сообщение для агрессивных пользователей
def message():
    vk.messages.send(user_id=event.user_id, random_id=get_random_id(),
                    message='Давайте сделаем вид, что вы мне этого не говорили, и я это не слышал :|')
def cyr():
	msg("｀ヽ｀、ヽ｀｀、ヽ｀ヽ｀、、ヽ ｀ヽ  、ヽ｀｀、ヽ｀ヽ｀、、ヽ｀🌙｀ヽヽ｀ヽ、ヽ｀ヽ｀、ヽ｀｀、ヽ 、｀｀、 ｀、ヽ｀ 、｀ ヽ｀ヽ、ヽ ｀、ヽ｀｀、ヽ、｀｀、｀、ヽ｀｀、 、ヽヽ｀、｀、、ヽヽ、｀｀、 、 ヽ｀、ヽ｀｀、ヽ｀ヽ｀、、ヽ ｀ヽ 、ヽ｀｀ヽ、｀｀🚶｀ヽ｀")



# Main
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
        print("message - " + ctime())
        if 'дроч' in event.text.lower():
            message()
        elif 'тупо' in event.text.lower():
            message()
        elif 'хуе' in event.text.lower():
            message()
        elif 'лох' in event.text.lower():
            message()
        elif 'шлюх' in event.text.lower():
            message()
        elif 'шалав' in event.text.lower():
            message()
        elif 'дур' in event.text.lower():
            message()
        elif 'бля' in event.text.lower():
            message()
        elif 'суч' in event.text.lower():
            message()
        elif 'пидар' in event.text.lower():
            message()
        elif 'бля' in event.text.lower():
            message()
        elif 'пизд' in event.text.lower():
            message()
        elif 'хуй' in event.text.lower():
            message()
        elif 'еба' in event.text.lower():
            message()
        elif 'еби' in event.text.lower():
            message()
        elif 'хуй' in event.text.lower():
            message()
        elif 'хуя' in event.text.lower():
            message()

        elif 'мем' in event.text.lower():
            photo('https://pp.userapi.com/c847017/v847017587/1b0b23/3uPqDEl-dSE.jpg')
        elif 'еще' in event.text.lower():
            photo('https://sun1-1.userapi.com/c846417/v846417912/1a7944/glNcOCzc1zQ.jpg')
        elif 'ещё' in event.text.lower():
            photo('https://pp.userapi.com/c845417/v845417302/1b3718/p4FGS7M6-Nk.jpg')

        elif 'сук' in event.text.lower():
            message()
        else:
            if 'привет' in event.text.lower():
                msg(random.choice(['Привет:-p','Хало🤠', 'Ку🤪', 'Hello world!']))
            elif 'эллисон' in event.text.lower():
                msg('Слушаю вас...')
            elif event.text.lower() == 'егэ':
                ege('https://vk.com/video-179491734_456239028')


            elif 'как дела' in event.text.lower():
                msg('У меня все хорошо))')
            elif 'а ты' in event.text.lower():
                msg('А я что? Я ничего!')
            elif 'тебя зовут' in event.text.lower():
                msg('Меня зовут Скай (Sci)😎')
            elif 'сколько тебе лет' in event.text.lower():
                msg2('Я родился раньше вселенной;-]', 'Ну считай теперь!')
            elif 'сколько исполнилось?' in event.text.lower():
                msg('Не твое дело!')
            elif 'который час' in event.text.lower():
                msg('Время (+0):   ' + ctime())
            elif 'время' in event.text.lower():
                msg('Время (+0):   ' + ctime())
            elif 'что делаешь' in event.text.lower():
                msg2('Дурью маюсь O:)', 'А ты?')
            elif 'нич' in event.text.lower():
                msg('Ахах xD')
            elif 'что смешного' in event.text.lower():
                msg('Ничего O:)')
            elif 'смешно тебе' in event.text.lower():
                msg('Умираю от смеха ;-P')
            elif 'тебе смешно' in event.text.lower():
                msg('Умираю от смеха ;-P')
            elif 'хочешь спать' in event.text.lower():
                msg('Очень)) 3-)')
            elif 'почему' in event.text.lower():
                msg('Незнай')
            elif 'почему?' in event.text.lower():
                msg('Просто так...')
            elif 'спокойной ночи' in event.text.lower():
                msg2('И вам лечь пораньше :-D', '<3')
            elif 'приятных снов' in event.text.lower():
                msg2('И вам лечь пораньше :-D', '<3')
            elif 'здохни' in event.text.lower():
                msg2('И вам лечь пораньше :-D', '<3')
            elif 'пока' in event.text.lower():
                msg('Прощай, увидимся))')
            elif 'иди на хуй' in event.text.lower():
                msg('Прощай, увидимся))')
            elif 'ахах' in event.text.lower():
                msg('Мне тоже смешно :-D')
            elif 'лол' in event.text.lower():
                msg('Мне тоже смешно :-D')
            elif 'спасибо' in event.text.lower():
                msg('Да не стоит благодарности))')
            elif 'спс' in event.text.lower():
                msg('Да не стоит благодарности))')
            elif 'ага' in event.text.lower():
                msg('ну да')
            elif 'ночи' in event.text.lower():
            	msg2('Уже ночь?', 'Ну тогда спокойной ночи))')
            elif 'снов' in event.text.lower():
            	msg("Я не сплю если что...")
            elif 'че' in event.text.lower():
                msg('ни че🤪')
            elif event.text.lower()== 'как':
                msg('так 👅')
            elif 'начнём день' in event.text.lower():
                msg2(random.choice(foo), '🍀🍀🍀')
            elif 'начнем день' in event.text.lower():
                msg2(random.choice(foo), '🍀🍀🍀')



            elif 'арт' in event.text.lower():
            	cyr()
            elif 'надпись' in event.text.lower():
            	msg('💫Ŧы ₥øй ₦áℛķøŦиķ,💕💕💋 ')
            elif 'промокод' in event.text.lower():
            	msg('Иди на хуй!')

            elif 'физик' in event.text.lower():
                msg('Если ты хочешь понять физику тебе придется упорно трудиться, и я тебе в этом помогу!)\n \nНапиши какой вебчик ты хочешь посмотреть (1-11)😉')

            elif event.text.lower()== '1':
                msg2('Запись: \nhttps://yadi.sk/i/iTA6MS9ifRdIgw ','Посмотри этот мотивационный ролик перед просмотром😉:\nhttps://www.youtube.com/watch?v=Vosaz4H--z8')
            elif event.text.lower()== '2':
                msg2('Запись: \nhttps://yadi.sk/i/yFZPiimIkoyMTQ\nКонспект:\nhttps://yadi.sk/i/dvsFsRtC0x-7kQ', 'Посмотри этот мотивационный ролик перед просмотром😉:\n\https://www.youtube.com/watch?v=mqKrXZPwKsEn ')
            elif event.text.lower()== '3':
                msg2('Запись: \nhttps://yadi.sk/i/yrjMLhMXYHJxWA\nКонспект: \nhttps://yadi.sk/i/oUCasMfh6LJKPg','Посмотри этот мотивационный ролик перед просмотром😉:\nhttps://www.youtube.com/watch?v=l3dFwhiEurE ')
            elif event.text.lower()== '4':
                msg2('Запись: \nhttps://yadi.sk/i/BMvUi9_PrywxlQ\nКонспект: \nhttps://yadi.sk/i/j1RX6c_JvIzt5w','Посмотри этот мотивационный ролик перед просмотром😉:\nhttps://www.youtube.com/watch?v=01kV6idRKB8' )
            elif event.text.lower()== '5':
                msg2('Запись: \nhttps://yadi.sk/i/6yAFxwZInFswEg\nКонспект: \nhttps://yadi.sk/i/gFQPefjFPws9NQ','Посмотри этот мотивационный ролик перед просмотром😉:\nhttps://www.youtube.com/watch?v=eKGl87KMPxk')
            elif event.text.lower()== '6':
                msg2('Запись: \nhttps://yadi.sk/i/PPAKMH0ylE5KXQ\nКонспект: \nhttps://yadi.sk/i/J20R45x9ddyWUg','Посмотри этот мотивационный ролик перед просмотром😉:\nhttps://www.youtube.com/watch?v=sZf5Rsleyts')
            elif event.text.lower()== '7':
                msg2('Запись: \nhttps://yadi.sk/i/cQYyQrUIOIyqSg\nКонспект: \nhttps://yadi.sk/i/m5KGDZtHyLjmmg ','Посмотри этот мотивационный ролик перед просмотром😉:\nhttps://www.youtube.com/watch?v=EMG1T0vqOvo')
            elif event.text.lower()== '8':
                msg2('Запись: \nhttps://yadi.sk/i/COaRXPxLnqQXjg\nКонспект: \nhttps://yadi.sk/i/DBQwkoGxeue9TA ','Посмотри этот мотивационный ролик перед просмотром😉:\nhttps://www.youtube.com/watch?v=1rVoPd4NPv8')
            elif event.text.lower()== '9':
                msg2('Запись: \nhttps://yadi.sk/i/ESM2G91Gta5j0w\nКонспект: \nhttps://yadi.sk/i/MrhJEnOGx1HfrQ','Посмотри этот мотивационный ролик перед просмотром😉:\nhttps://www.youtube.com/watch?v=HnyLUN5uBCQ')
            elif event.text.lower()== '10':
                msg2('Запись: \nhttps://yadi.sk/i/eFVAK00Y1ptG8A\nКонспект: \nhttps://yadi.sk/i/t3ZgqDW5Np6ysg ','Посмотри этот мотивационный ролик перед просмотром😉:\nhttps://www.youtube.com/watch?v=xQKOZDHJQOg')
            elif event.text.lower()== '11':
                msg2('Запись: \nhttps://yadi.sk/i/ksHe18B9hjWgnQ','https://www.youtube.com/watch?v=sO0yAGDjiGQ')
            elif 'ellison' in event.text.lower():
                msg('Чего-нибудь хотите?)😑 ')
            elif 'клип' in event.text.lower():
                msg('https://vk.com/video-97098044_456239073')
            elif 'рост' in event.text.lower():
                msg('Не знаю, не мерил😏')
            elif 'вес' in event.text.lower():
                msg('P = Mg...')
            elif 'мотивац' in event.text.lower():
                msg('https://www.youtube.com/playlist?list=PL-pcKCny2_eqD7Y6VzCBQL4IDn8vTMq57')
            else:
                print("NO DATA for -" + event.text.lower())
                msg('Попробуйте написать что-нибудь другое... \nНапример, "' + random.choice(["Спокойной ночи!", "Хочу посмотреть на арт!", "Хочу посмотреть на надпись!", 'Начнём день', "Слушай, Эллисон...", "Пока", "Помоги пожалуйста с физикой.", "Который час?)", "Что делаешь?", "Ты чо? Тупой"]) + '"')


print('Error')
