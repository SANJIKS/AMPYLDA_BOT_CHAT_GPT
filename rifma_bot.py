import telebot
import random
import re

# создаем экземпляр бота
bot = telebot.TeleBot('your_bot_token')

# функция для получения рифмы
def get_rhyme(word):
    # если слово заканчивается на "да", возвращаем "ампылда"
    if word.endswith('да'):
        return 'ампылда'
    # else:
    #     # здесь можно использовать сторонние библиотеки для получения рифм, например, pymorphy2 или rhymes
    #     # но для примера, просто будем генерировать случайную рифму
    #     vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    #     if len(word) > 2:
    #         last_vowel_index = max([i for i, char in enumerate(word) if char in vowels])
    #         rhyme_part = word[last_vowel_index:]
    #         rhyme = rhyme_part + ''.join(random.sample(vowels, k=2))
    #         return rhyme
    #     else:
    #         return word

# функция для обработки сообщений
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    # получаем текст сообщения
    text = message.text.lower()
    # используем регулярное выражение, чтобы удалить знаки препинания и лишние пробелы
    text = re.sub(r'[^\w\s]', '', text).strip()
    # разбиваем текст на слова
    words = text.split()
    # генерируем рифму для последнего слова
    rhyme = get_rhyme(words[-1])
    # формируем ответ
    response = ''
    for i, word in enumerate(words):
        # если это последнее слово и оно заканчивается на "да", добавляем "ампылда"
        if i == len(words) - 1 and word.endswith('да'):
            response += 'ампылда'
        else:
            response += word
        # добавляем пробел между словами
        response += ' '
    # отправляем ответ
    bot.send_message(message.chat.id, response)

# запускаем бота
bot.polling()
