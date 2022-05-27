import database
import json

class Pokemon():

    def __init__(self, id):
        db = database.Database()
        id=id-1
        self.__id = db.pokedex[id]["id"]
        self.__name = db.pokedex[id]["name"]["english"]
        self.__type = db.pokedex[id]["type"]
        self.__hp = db.pokedex[id]["base"]["HP"]
        self.__attack = db.pokedex[id]["base"]["Attack"]//4
        self.__attackSp = db.pokedex[id]["base"]["Sp. Attack"]//4
        self.__speed = db.pokedex[id]["base"]["Speed"]        
        del db
        del id

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def type(self):
        return self.__type
    @type.setter
    def type(self, value):
        self.__type = value
    
    @property
    def hp(self):
        return self.__hp
    @hp.setter
    def hp(self, value):
        self.__hp = value

    @hp.deleter
    def hp(self):
        del self.__hp

    @property
    def attack(self):
        return self.__attack
    @attack.setter
    def attack(self, value):
        self.__attack = value

    @property
    def attackSp(self):
        return self.__attackSp
    @attackSp.setter
    def attackSp(self, value):
        self.__attackSp = value

    @property
    def speed(self):
        return self.__speed
    @speed.setter
    def speed(self, value):
        self.__speed = value


    def attack_target(self, target):
        print(self.name + " attacks " + target.name)
        target.receive_damage(self.attack)

    def receive_damage(self, dmg):
        #self.hp -= dmg

        if self.hp - dmg < 0: 
            self.hp = 0
        else:
            self.hp -= dmg

        print(self.name + " receives " + str(dmg) + " damages")
        print(self.name + " hp: " + str(self.hp))
