# -*- coding: utf8 -*-
import requests
import vk_api
import vk
import time
from vk_api import VkUpload 
from vk_api.longpoll import VkLongPoll, VkEventType
from random import randint

#  4c186333ef3f740f9af02180d48bebec88587fa76f705287325595523e6a2d0dc4032107976de40d894a8
tokenbot = ""
vk_session = vk_api.VkApi(token=tokenbot)
longpoll = VkLongPoll(vk_session)
vk=vk_session.get_api()
upload = VkUpload(vk_session)
attachments = []
attachments.append('doc68106853_535852671')



def neponatno():
    vk.messages.send(
        user_id=event.user_id,
        random_id=randint(1, 10 ** 17),
        attachment=','.join(attachments),
        message='Это шо такое? Напиши "помощь"',
    )
def pomosh():
    vk.messages.send(  # Отправляем собщение
        user_id=event.user_id,
        random_id=randint(1, 10 ** 17),
        keyboard=open("keyboards/keyboard_start.json", "r", encoding="UTF-8").read(),
        message=""" 
                            Возможные команды:
                            - Тест
                            - Меню
                            - Помощь
                            """
    )
def test():
    vk.messages.send(  # Отправляем собщение
        user_id=event.user_id,
        random_id=randint(1, 10 ** 17),
        message='Сигнал получен\n Отвечаю: Бип-Буп-Бип'
    )
def valentinka():
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
            if event.text.lower() == 'да':
                # прохождение анкеты
                vk.messages.send(
                    user_id=event.user_id,
                    random_id=randint(1, 10 ** 17),
                    message='Спасибо!'
                )
                break
            elif event.text.lower() == 'нет':
                vk.messages.send(
                    user_id=event.user_id,
                    random_id=randint(1, 10 ** 17),
                    message='Очень жаль'  # и оповещение о предназначении анкеты
                )
                break
            else:
                neponatno()
                break
def menu():
    vk.messages.send(  # Отправляем собщение
        user_id=event.user_id,
        random_id=randint(1, 10 ** 17),
        keyboard=open("keyboards/keyboard_menu.json", "r", encoding="UTF-8").read(),
        message='---Меню---',
    )



while True:
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
       #Слушаем longpoll, если пришло сообщение то:	
            if event.text.lower() == 'помощь': #Если написали заданную фразу
                if event.from_user:
                    pomosh()

            elif event.text.lower() == 'тест': #Если написали заданную фразу
                if event.from_user:
                    test()
            elif event.text.lower() == 'меню': #Если написали заданную фразу
                if event.from_user:
                    menu()
                for event in longpoll.listen():
                    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
                        if event.text.lower() == 'валентинка':  # Если написали заданную фразу
                            if event.from_user:
                                vk.messages.send(
                                    user_id=event.user_id,
                                    random_id=randint(1, 10 ** 17),
                                    keyboard=open("keyboards/keyboard_yes_or_no.json", "r", encoding="UTF-8").read(),
                                    message='Пройти анкету?'
                                )
                                valentinka()
                                break
                        if event.text.lower() == 'расписание':  # Если написали заданную фразу
                            if event.from_user:
                                vk.messages.send(
                                    user_id=event.user_id,
                                    random_id=randint(1, 10 ** 17),
                                    message='Расписание'
                                )

            else:
                if event.from_user:
                    neponatno()
                    break
            continue
    time.sleep(1)
