import requests
import vk_api
from vk_api import VkUpload 
from vk_api.longpoll import VkLongPoll, VkEventType
from random import randint

tokenbot = "3a667e067e50bfb9432fc218dea67519e041ba7a0366ca1f689d382b87d04ccf020de43d1280fa4ea3fb3"
vk_session = vk_api.VkApi(token=tokenbot)

longpoll = VkLongPoll(vk_session)
vk = vk_session.get_api()

upload = VkUpload(vk_session)

attachments = []
attachments.append('doc68106853_535852671')

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
   #������� longpoll, ���� ������ ��������� ��:			
        if event.text.lower() == '����': #���� �������� �������� �����
            if event.from_user:
                vk.messages.send( #���������� ��������
                    user_id=event.user_id,
                    random_id=randint(1, 10**17),
                    message='������ �������\n �������: ���-���-���'
                )
            elif event.from_chat:
                vk.messages.send( #���������� ��������
                    chat_id=event.chat_id,
                    random_id=randint(1, 10**17),
                    message='������ �������\n �������: ���-���-���'
                )
        elif event.text.lower() == '�������': #���� �������� �������� �����
            if event.from_user:
                vk.messages.send( #���������� ��������
                    user_id=event.user_id,
                    random_id=randint(1, 10**17),
                    message='������: 1, 2 ��� 3?',
                )
            elif event.from_chat:
                vk.messages.send( #���������� ��������
                    chat_id=event.chat_id,
                    random_id=randint(1, 10**17),
                    message='������: 1, 2 ��� 3?',
                    )
            for event in longpoll.listen():
                if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
                    if event.text.lower() == '1' or event.text.lower() == '2' or event.text.lower() == '3': #���� �������� �������� �����              
                        if event.from_user:
                            vk.messages.send( #���������� ��������
                                user_id=event.user_id,
                                random_id=randint(1, 10**17),
                                message='�� ������ '+ event.text + '. � ������?:)',
                            )
                            break
                        elif event.from_chat:
                            vk.messages.send( #���������� ��������
                                chat_id=event.chat_id,
                                random_id=randint(1, 10**17),
                                message='�� ������  '+ event.text + '. � ������?:)',
                            )
                            break
                    else:
                        if event.from_user:
                            vk.messages.send( #���������� ��������
                                user_id=event.user_id,
                                random_id=randint(1, 10**17),
                                attachment=','.join(attachments),
                                message='��� �� �����?',
                            )
                            break
                        elif event.from_chat:
                            vk.messages.send( #���������� ��������
                                chat_id=event.chat_id,
                                random_id=randint(1, 10**17),
                                attachment=','.join(attachments),
                                message='��� �� �����?',
                            )
                            break
        else:
            if event.from_user:
                vk.messages.send( #���������� ��������
                    user_id=event.user_id,
                    random_id=randint(1, 10**17),
                    attachment=','.join(attachments),
                    message='��� �� �����?',
                )
                break
            elif event.from_chat:
                vk.messages.send( #���������� ��������
                    chat_id=event.chat_id,
                    random_id=randint(1, 10**17),
                    attachment=','.join(attachments),
                    message='��� �� �����?',
                )
        continue

                    