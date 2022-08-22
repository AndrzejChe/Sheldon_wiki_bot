# импортируем библиотеки
import re, telebot, wikipedia
from telebot import types
# Создаем экземпляр бота
bot = telebot.TeleBot('')
# Устанавливаем русский язык в Wikipedia
wikipedia.set_lang("ru")
# Чистим текст статьи в Wikipedia и ограничиваем его тысячей символов
def getwiki(s):
    try:
        ny = wikipedia.page(s)
                # Получаем первую тысячу символов
        wikitext=ny.content[:1000]
                # Разделяем по точкам
        wikimas=wikitext.split('.')
                # Отбрасываем всЕ после последней точки
        wikimas = wikimas[:-1]
                # Создаем пустую переменную для текста
        wikitext2 = ''
                # Проходимся по строкам, где нет знаков «равно» (то есть все, кроме заголовков)
        for x in wikimas:
                if not('==' in x):
        # Если в строке осталось больше трех символов,
        # добавляем ее к нашей переменной и возвращаем утерянные при разделении строк точки на место
                    if(len((x.strip()))>3):
                        wikitext2=wikitext2+x+'.'
                else:
                    break
        # Теперь при помощи регулярных выражений убираем разметку
        wikitext2=re.sub('\([^()]*\)', '', wikitext2)
        wikitext2=re.sub('\([^()]*\)', '', wikitext2)
        wikitext2=re.sub('\{[^\{\}]*\}', '', wikitext2)
        # Возвращаем текстовую строку
        return wikitext2
    # Обрабатываем исключение, которое мог вернуть модуль wikipedia при запросе
    except Exception as e:
        return '🤷 В энциклопедии нет информации об этом ⛔'
# Функция, обрабатывающая команду /start, добавляем кнопки
@bot.message_handler(commands=["start"])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋 Поздороваться")
    btn2 = types.KeyboardButton("❓ Отправить слово")
    btn3 = types.KeyboardButton("❌ TNE END")
    markup.add(btn1, btn2, btn3)
    bot.send_message(message.chat.id, text="Трям!, {0.first_name}!".format(message.from_user), reply_markup=markup)
@bot.message_handler(content_types=["text"])
def handle_text(message):
    if(message.text == "👋 Поздороваться"):
        bot.send_message(message.chat.id, text="Да пребудет с тобой Сила юный Падаван!🖖")
    elif (message.text == "❌ TNE END"):
        bot.send_message(message.chat.id, text="✌🏼 Рад был помочь! Задавай глупые вопросы, получай умные ответы!😉")
    elif (message.text == "❓ Отправить слово"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    else:
        bot.send_message(message.chat.id, getwiki(message.text))
        bot.send_message(message.from_user.id, "☑ ‍Готово")
# Запускаем бота
bot.polling(none_stop=True, interval=0)
