import telebot
import openai
import time
# указываем ключ из личного кабинета openai
openai.api_key = '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'
messages = []

# Создаем экземпляр бота
bot = telebot.TeleBot('6007451380:AAEjLTNJCUOeeAHLYP93CcfP-6l6EVOC-OI')
# Функция, обрабатывающая команду /start
@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Я на связи. Напиши мне что-нибудь )')
    
@bot.message_handler(content_types=["photo"])
def handle_text(tg_message):
    bot.send_message(tg_message.chat.id, 'Я думаю, что на картинке что-то очень важное, но открывать специально не буду:)')
# Получение сообщений от юзера
@bot.message_handler(content_types=["text"])
def handle_text(tg_message):
    try:
        user_id = tg_message.from_user.username
        message = tg_message.text
        messages.append({"role": "user", "content": message})
        chat = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages = messages)
        reply = chat.choices[0].message.content
        bot.send_message(tg_message.chat.id, reply)
        messages.append({"role":"assistant", "content": reply})
        print(f'@{user_id}->'+message)
        print('Bot->'+reply)
        time.sleep(5)
    except:
        bot.send_message(tg_message.chat.id, 'В данный момент я нахожусь в ошибке.\nОжидайте, когда хозяин перезапустит меня\nИнтервал ответов увеличен')


# Запускаем бота
bot.polling(none_stop=True, interval=0)