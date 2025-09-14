from random import randint
import requests

class Pokemonvrag:
    pokemons = {}
    # Инициализация объекта (конструктор)
    def __init__(self, pokemon_trainer1):

        self.pokemon_trainer1 = pokemon_trainer1 

        self.pokemon_number = randint(1,1000)
        self.img1 = self.get_img1()
        self.name1 = self.get_name1()
        self.abilities1 = self.get_abilki1()
        self.weight1 = self.get_weight1()
        self.height1 = self.get_height1()
        Pokemonvrag.pokemons[pokemon_trainer1] = self

    def get_abilki1(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}/'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['abilities'][0]["ability"]['name'])
        else:
            return "Pikachu"


    # Метод для получения картинки покемона через API
    def get_img1(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}/'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['sprites']['front_default'])
            return (data['sprites']['other']['front_shiny'])
        else:
            return "Pikachu"
        
    
    # Метод для получения имени покемона через API
    def get_name1(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['forms'][0]['name'])
        else:
            return "Pikachu"

    def get_weight1(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}/'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data["weight"])
        else:
            return "Pikachu"

    def get_height1(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}/'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data["height"])
        else:
            return "Pikachu"

    # Метод класса для получения информации
    def info1(self):
        return f"Имя твоего врага: {self.name1}"

    # Метод класса для получения картинки покемона
    def show_img1(self):
        return self.img1
    
    def show_abilki1(self):
        return f"Его способность:{self.abilities1}"

    def show_weight1(self):
        return f"Его вес:{self.weight1}"
    
    def show_height1(self):
        return f"Его рост:{self.height1}"



