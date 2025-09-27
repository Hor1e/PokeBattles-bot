from random import randint
import requests



class Pokemon:
    pokemons = {}
    # Инициализация объекта (конструктор)
    def __init__(self, pokemon_trainer):

        self.pokemon_trainer = pokemon_trainer   

        self.pokemon_number = randint(1,1000)
        self.img = self.get_img()
        self.name = self.get_name()
        self.abilities = self.get_abilki()
        self.weight = self.get_weight()
        self.height = self.get_height()
        Pokemon.pokemons[pokemon_trainer] = self

    def get_abilki(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}/'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['abilities'][0]["ability"]['name'])
        else:
            return "Pikachu"


    # Метод для получения картинки покемона через API
    def get_img(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}/'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['sprites']['front_default'])
            return (data['sprites']['other']['front_shiny'])
        else:
            return "Pikachu"
        
    
    # Метод для получения имени покемона через API
    def get_name(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['forms'][0]['name'])
        else:
            return "Pikachu"

    def get_weight(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}/'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data["weight"])
        else:
            return "Pikachu"

    def get_height(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}/'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data["height"])
        else:
            return "Pikachu"

    # Метод класса для получения информации
    def info(self):
        return f"Имя твоего покеомона: {self.name}"

    # Метод класса для получения картинки покемона
    def show_img(self):
        return self.img
    
    def show_abilki(self):
        return f"Его способность:{self.abilities}"

    def show_abilkiz(self):
        return self.abilities


class Warrior(Pokemon):
    def show_height(self):
        return f"Его рост(бонус от класса 10%):{self.height/100*110}"
    def show_weight(self):
        return f"Его вес(бонус от класса 50%):{self.weight/100*150}"

class Mage(Pokemon):
    def show_weight(self):
        return f"Его вес(бонус от класса 10%):{self.weight/100*110}"
    def show_height(self):
        return f"Его рост(бонус от класса 50%):{self.height/100*150}"