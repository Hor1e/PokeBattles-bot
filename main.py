import telebot 
from random import randint
from config import token

from logic import Pokemon
from logic import Warrior
from logic import Mage
from plohoilogic import Pokemonvrag
zifra = randint(0,1)

bot = telebot.TeleBot(token) 
w = None
h = None
pokemonchik = None
imaga = None
abilochka = None
coins = 0
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Приветствуем на арене покемонов! Для получения покемона введите /go, для начала битвы /battle и для просмотра баланса с магазином /bal")

@bot.message_handler(commands=['go'])
def go(message):
    global w, h, pokemonchik, abilochka, imaga
    if message.from_user.username not in Pokemon.pokemons.keys():
        pokemon = Pokemon(message.from_user.username)
        warrior = Warrior(message.from_user.username)
        mage = Mage(message.from_user.username)
        bot.send_message(message.chat.id, pokemon.info())
        pokemonchik = pokemon.name
        bot.send_photo(message.chat.id, pokemon.show_img())
        imaga = pokemon.img
        bot.send_message(message.chat.id, pokemon.show_abilki())
        abilochka = pokemon.abilities
        if zifra == 0:
            bot.send_message(message.chat.id, warrior.show_weight())
            bot.send_message(message.chat.id, warrior.show_height())
            w = warrior.weight/100*150
            h = warrior.height/100*110           
            print(w)
            print(h)
            
        elif zifra == 1:
            bot.send_message(message.chat.id, mage.show_weight())
            bot.send_message(message.chat.id, mage.show_height())
            w = mage.weight/100*110
            h = mage.height/100*150
            print(w)
            print(h) 
        
    else:
        bot.reply_to(message, "Ты уже создал себе покемона")

@bot.message_handler(commands=['info'])
def info(message):
    if message.from_user.username in Pokemon.pokemons.keys():
        pok = Pokemon.pokemons[message.from_user.username]
        bot.send_message(message.chat.id, pokemonchik)
        bot.send_message(message.chat.id, imaga)
        bot.send_message(message.chat.id, abilochka)
        bot.send_message(message.chat.id, f"Вес:{w}")
        bot.send_message(message.chat.id, f"Рост:{h}")

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

