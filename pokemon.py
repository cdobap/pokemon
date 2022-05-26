import json

class Pokemon():

    def __init__(self, id):
        f=open("pokedex.json", "r")
        pokedex=f.read()
        f.close()
        del f
        pokedex=json.loads(pokedex)
        id=id-1
        self.__id = pokedex[id]["id"]
        self.__name = pokedex[id]["name"]["french"]
        self.__type = pokedex[id]["type"]
        self.__hp = pokedex[id]["base"]["HP"]
        self.__attack = pokedex[id]["base"]["Attack"]//5
        self.__attackSp = pokedex[id]["base"]["Sp. Attack"]//5
        self.__speed = pokedex[id]["base"]["Speed"]        
        del pokedex
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
        print(self.attack)
        print(target.hp)
        target.hp -= self.attack



a = Pokemon(1)

# print(a.id)
# print(a.name)
# print(a.type)
# print(a.hp)
# print(a.attack)
# print(a.attackSp)
# print(a.speed)

b = Pokemon(2)

a.attack_target(b)

a.attack_target(b)
a.attack_target(b)
a.attack_target(b)
