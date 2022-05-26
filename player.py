import database
from random import randrange

class Player():


    def __init__(self):
        db = database.Database()

        name=input("your name: ")
        for i in range(len(db.player)):
            if name == db.player[i]["name"]:
                exist = True

        if name == db.player[i]["name"]:
            self.__name = db.player[i]["name"]
            self.__pokedex = db.player[i]["pokedex"]
        else:
            self.__name = name
            self.__pokedex = [ randrange(1, len(db.pokedex)) for i in range(3) ]

   
    @property
    def name(self):
        return self.__name

    @property
    def pokedex(self):
        return self.__pokedex
    
    @pokedex.setter
    def pokedex(self, id_pokemon):
        self.__pokedex.append(id_pokemon)

    
p=Player()

print(p.name) 
print(p.pokedex)
p.pokedex = 4
print(p.pokedex)

