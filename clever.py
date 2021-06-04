# for index, name in enumerate(sr.Microphone.list_microphone_names()):
#     print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))
import os
import time
import speech_recognition as sr
from fuzzywuzzy import fuzz
import pyttsx3
import datetime
import random

# настройки
# opts = {
#     "alias": ('кеша', 'кеш', 'инокентий', 'иннокентий', 'кишун', 'киш',
#               'кишаня', 'кяш', 'кяша', 'кэш', 'кэша'),
#     "tbr": ('скажи', 'расскажи', 'покажи', 'сколько', 'произнеси'),
#     "cmds": {
#         "ctime": ('текущее время', 'сейчас времени', 'который час'),
#         "radio": ('включи музыку', 'воспроизведи радио', 'включи радио'),
#         "stupid1": ('расскажи анекдот', 'рассмеши меня', 'ты знаешь анекдоты')
#     }

r = sr.Recognizer()
m = sr.Microphone(device_index=1)
speak_engine = pyttsx3.init()


pts = {"привет":["Привет!", "Приветульки"],
       "как дела":["Нормально", "Отлично", "Плохо"],
       "почему":["Сам не знаю", "Просто настроения нету"],
       "кто твои родители": ["По сути у меня нету родителей, но у меня есть создатели, Артур и Степа!"],
       "что ты умеешь": ["Я пока что мало что знаю и умею, но если ты меня будешь обучать я стану умнее"]}

main = speak_engine.getProperty('voices')

# new_question = input('Введи новый вопрос >>')
# new_answer = input('Введи ответ на вопрос(если их несколько то пишите между ними знак *) >>')
# searcher = input("Задайте вопрос?")
# del_key = input("Хотите ли вы удалить вопрос(напишите вопрос который хотите удалить)")


def add(new_answer, new_question):
    if new_question in list(pts):
        print('Такой вопрос есть, введи другой')
    elif new_question not in list(pts) and '*' not in new_answer:
        pts.update({new_question : new_answer})
    else:
        new_answer_split = new_answer.split("*")
        pts.update({new_question : new_answer_split})
    print(pts)


def search(lol, pts):
    a = 0
    for i in list(pts):
        if lol in i:
            speak(random.choice(pts[i]))
            a += 1
    if a == 0:
        print('Вы меня не обучили как отвечать на такой вопрос')


def delate(del_key, pts):
    del pts[del_key]


voices = speak_engine.getProperty('voices')
speak_engine.setProperty('voice', voices[0].id)


def speak(what):
    print(what)
    speak_engine.say(what)
    speak_engine.runAndWait()
    speak_engine.stop()


def callback(recognizer, audio):
    voice = recognizer.recognize_google(audio, language="ru-RU").lower()
    spis = voice.split(' кома ')
    if spis[0] in list(pts):
        search(spis[1], pts)
    elif spis[0] == 'добавить':
        add(spis[1], [spis[2]])
        print(pts)
    elif spis[0] == 'удалить':
        delate(spis[1], pts)
        print(pts)
    print("[log] Распознано: " + voice)
    speak_engine.say(voice)
    speak_engine.runAndWait()
    speak_engine.stop()


        # if voice.startswith(opts["alias"]):
        #     # обращаются к Кеше
        #     cmd = voice
        #
        #     for x in opts['alias']:
        #         cmd = cmd.replace(x, "").strip()
        #
        #     for x in opts['tbr']:
        #         cmd = cmd.replace(x, "").strip()
        #
        #     # распознаем и выполняем команду
        #     cmd = recognize_cmd(cmd)
        #     execute_cmd(cmd['cmd'])

    # except sr.UnknownValueError:
    #     print("[log] Голос не распознан!")
    #     speak_engine.say('Голос не распознан')
    #     speak_engine.runAndWait()
    #     speak_engine.stop()
    # except sr.RequestError as e:
    #     print("[log] Неизвестная ошибка, проверьте интернет!")


# def recognize_cmd(cmd):
#     RC = {'cmd': '', 'percent': 0}
#     for c, v in opts['cmds'].items():
#
#         for x in v:
#             vrt = fuzz.ratio(cmd, x)
#             if vrt > RC['percent']:
#                 RC['cmd'] = c
#                 RC['percent'] = vrt
#
#     return RC


# def execute_cmd(cmd):
#     if cmd == 'ctime':
#         # сказать текущее время
#         now = datetime.datetime.now()
#         speak("Сейчас " + str(now.hour) + ":" + str(now.minute))
#
#     elif cmd == 'radio':
#         # воспроизвести радио
#         os.system("D:\\Jarvis\\res\\radio_record.m3u")
#
#     elif cmd == 'stupid1':
#         # рассказать анекдот
#         speak("Мой разработчик не научил меня анекдотам ... Ха ха ха")
#
#     else:
#         print('Команда не распознана, повторите!')


# запуск

# with m as source:
#     r.adjust_for_ambient_noise(source)

# speak_engine = pyttsx3.init()

# Только если у вас установлены голоса для синтеза речи!


# speak("Добрый день, повелитель")
# speak("Кеша слушает")

stop_listening = r.listen_in_background(m, callback)
while True: time.sleep(0.1) # infinity loop