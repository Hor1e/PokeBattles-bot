import telebot 
from config import token

from logic import Pokemon
from plohoilogic import Pokemonvrag

bot = telebot.TeleBot(token) 
w = None
h = None
coins = 0
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Приветствуем на арене покемонов! Для получения покемона введите /go, для начала битвы /battle и для просмотра баланса с магазином /bal")

@bot.message_handler(commands=['go'])
def go(message):
    global w, h
    if message.from_user.username not in Pokemon.pokemons.keys():
        pokemon = Pokemon(message.from_user.username)
        bot.send_message(message.chat.id, pokemon.info())
        bot.send_photo(message.chat.id, pokemon.show_img())
        bot.send_message(message.chat.id, pokemon.show_abilki())
        bot.send_message(message.chat.id, pokemon.show_weight())
        bot.send_message(message.chat.id, pokemon.show_height())
        w = pokemon.weight
        h = pokemon.height
        
        print(w)
    else:
        bot.reply_to(message, "Ты уже создал себе покемона")

@bot.message_handler(commands=['battle'])
def battle(message):
    global w, h,coins
    
    
    pokemon1 = Pokemonvrag(message.from_user.username)
    bot.send_message(message.chat.id, pokemon1.info1())
    bot.send_photo(message.chat.id, pokemon1.show_img1())
    bot.send_message(message.chat.id, pokemon1.show_abilki1())
    bot.send_message(message.chat.id, pokemon1.show_weight1())
    bot.send_message(message.chat.id, pokemon1.show_height1())
    bot.reply_to(message, "Покемоны обмениваются ударами, ваш использует способность:")
    bot.reply_to(message, "и...")
    print(pokemon1.weight1)
            
    print(w)
            
    if w > pokemon1.weight1 and h > pokemon1.height1:
        bot.send_message(message.chat.id, "Вы выйграли! Абсолютное превосходство! + 500 монет, для просмотра баланса введите /bal")
        coins += 500
    elif w < pokemon1.weight1 and h > pokemon1.height1:
        bot.send_message(message.chat.id, "Вы выйграли! Благодаря росту! + 250 монет, для просмотра баланса введите /bal")
        coins += 250
    elif w > pokemon1.weight1 and h < pokemon1.height1:
        bot.send_message(message.chat.id, "Вы выйграли! Благодаря массе! + 250 монет, для просмотра баланса введите /bal")
        coins += 250
    else:
        bot.send_message(message.chat.id, "Вы проиграли(")
        
@bot.message_handler(commands=['bal'])
def bal(message):
    global coins
    bot.send_message(message.chat.id, f"Ваш баланс {coins}")
    bot.send_message(message.chat.id, f"Магазин пока пуст...")

bot.infinity_polling(none_stop=True)

