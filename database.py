import json

class Database():

    def __init__(self):
        # 
        f=open("pokedex.json", "r")
        pokedex=f.read()
        f.close()
        del f
        self.__pokedex=json.loads(pokedex)
        del pokedex
        # 
        f=open("types.json", "r")
        types=f.read()
        f.close()
        del f
        self.__types=json.loads(types)
        del types
        #
        f=open("player.json", "r")
        player=f.read()
        f.close()
        del f
        self.__player=json.loads(player)
        del player

    @property
    def pokedex(self):
        return self.__pokedex
    
    @property
    def types(self):
        return self.__types

    @property
    def player(self):
        return self.__player