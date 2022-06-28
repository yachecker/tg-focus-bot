import telebot
import random
from telebot import types

bot = telebot.TeleBot('5560157308:AAH6Bf5xpLc-3ORG-I-OK9sOSu1TLvRJzfQ')
sentenceStarts = ['Я и не сомневался что', "Хе-хе, на ушко мне напели что",
                  "Я бы поставил свой дом на кон что", "Без сомнении, я так и знал что"]


@bot.message_handler(commands=['start'])
def send_welcome(msg):
    bot.send_message(
        msg.chat.id, 'Доступные команды:\n/calc - посчитает вам число [ВВОДИТЕ ТРЁХЗНАЧНОЕ ЧИСЛО]\n/guess - постарается угадать число [ВВОДИТЕ ДВУХЗНАЧНОЕ ЧИСЛО]\n/start - вызовет это меню')
    bot.send_message(msg.chat.id, 'Привет! Я бот который будет угадывать цифру.\n\tЗагадай трехзначное число\n\tОтними от него сумму цифр\n\tУбери 1 цифру и сообщи её мне\n\tНапример 439, 439 - (4+3+9) = 423\n\tЯ например убираю число 3, у меня получилось 42.\n\tПопробуй ты, я угадаю число, обещаю!\nЕсли что начинай уже вводить')


@bot.message_handler(commands=['calc'])
def calculator(msg):
    if not msg.text.split()[1:] or msg.text.split()[1:][0] == ' ' or len(msg.text.split()[1:][0]) != 3:
        msge = bot.send_message(
            msg.chat.id, 'Введите корректное трёхзначное число.')
        bot.register_next_step_handler(msge, calculator)
    else:
        number = msg.text.split()[1:][0]
        result = str(
            int(number) - (int(number[0]) + int(number[1]) + int(number[2])))
        bot.send_message(
            msg.chat.id, f'Получилось: "{result}"\n\tТеперь вы можете попробовать ввести:\n{result[0]}{result[1]}\tзагадано {result[2]}\n{result[0]}{result[2]}\tзагадано {result[1]}\n{result[1]}{result[2]}\tзагадано {result[0]}')


@bot.message_handler(commands=['guess'])
def startScam(msg):
    markup = types.ReplyKeyboardMarkup().add("✅Да", "❌Нет")
    if not msg.text.split()[1:] or msg.text.split()[1:][0] == ' ':
        msge = bot.send_message(
            msg.chat.id, "Введите число, не оставляйте поле пустым\nПопробуйте ввести /guess 49")
        bot.register_next_step_handler(msge, startScam)
    else:
        if len(msg.text.split()[1:][0]) != 2:
            msge = bot.send_message(
                msg.chat.id, 'Введите корректные данные, вы ввели не два числа!!!\nПопробуйте еще раз!\nКстати, вы в бесконечном круге, я не успокоюсь пока вы не введете нормальное число\n(можете ввести любое двузначное число)')
            bot.register_next_step_handler(msge, startScam)
        else:
            number = msg.text.split()[1:][0]
            if (int(number[0]) + int(number[1]) > 9):
                msge = bot.send_message(
                    msg.chat.id, f'Вы убрали цифру: {18-(int(number[0])+int(number[1]))}')
            elif(int(number[0]) + int(number[1]) == 9): 
                msge = bot.send_message(
                    msg.chat.id, 'Вы убрали цифру 9?', reply_markup=markup)
                bot.register_next_step_handler(msge, next_step)
            else:
                msge = bot.send_message(
                    msg.chat.id, f'Вы убрали цифру: {9-(int(number[0]) + int(number[1]))}')
def next_step(msg):
    if msg.text == "✅Да":
        bot.send_message(msg.chat.id, f"{sentenceStarts[random.randint(0, len(sentenceStarts)-1)]} вы убрали цифру 9",reply_markup=types.ReplyKeyboardRemove())
    elif msg.text == "❌Нет":
        bot.send_message(msg.chat.id, f"{sentenceStarts[random.randint(0, len(sentenceStarts)-1)]} вы убрали цифру 0",reply_markup=types.ReplyKeyboardRemove())
      
bot.polling()
