import random
import telebot

from token_file import MY_TOKEN

bot = telebot.TeleBot(MY_TOKEN)


@bot.message_handler(commands=["Game"])
def send_welcome(message):
    bot.reply_to(message, "Приветсвую Вас в игре 'Камень Ножницы Бумага!' Или же 'Рошамбо'"
                          "Выберите камень (к), ножницы (н), или бумагу (б)")


@bot.message_handler(func=lambda message: True)
def play_game(message):
    user_move = message.text
    if user_move not in ["к", "н", "б"]:
        bot.reply_to(message, "Пожалуйста введите либо к, н, или б.")
    else:
        computer_move = random.choice(["к", "н", "б"])
        if (user_move == "к" and computer_move == "н") or \
                (user_move == "н" and computer_move == "б") or \
                (user_move == "б" and computer_move == "к"):
            bot.reply_to(message, "Ура! Вы выиграли!")
        elif user_move == computer_move:
            bot.reply_to(message, "Вывод Ничья!")
        else:
            bot.reply_to(message, "Вы проиграли Боту!")


bot.infinity_polling()



