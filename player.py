import database
import pokemon
from random import randrange
import json

class Player():

    def __init__(self):
        db = database.Database()  
        player_in_db = False
        name=input("your name: ")
        for i in range(len(db.player)):
            if name == db.player[i]["name"]:
                player_in_db = True
                j = i

        if player_in_db:
            self.__name = db.player[j]["name"]
            self.__pokedex = db.player[j]["pokedex"]
            self.__initiative = False
        else:
            self.__name = name
            self.__pokedex = [ randrange(1, len(db.pokedex)) for i in range(3) ]
            self.__initiative = False
            
   
    @property
    def initiative(self):
        return self.__initiative

    @initiative.setter
    def initiative(self, value):
        self.__initiative = value

    @property
    def name(self):
        return self.__name

    @property
    def pokedex(self):
        return self.__pokedex
    
    @pokedex.setter
    def pokedex(self, id_pokemon):
        self.__pokedex.append(id_pokemon)
    
    def get_pokemon(self, pkmn_id):
        return [i for i in self.__pokemons if i.id == pkmn_id][0]

    def get_pokemons(self):
        return self.__pokemons

    def set_pokemons(self):   
        self.__pokemons = []
        for i in self.__pokedex:            
            self.__pokemons.append(pokemon.Pokemon(i))          

    @property
    def activ_pokemon(self):
        return self.__activ_pokemon
    
    @activ_pokemon.setter
    def activ_pokemon(self, activ_pokemon):
        self.__activ_pokemon = activ_pokemon

