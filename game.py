import database
import player
import pokemon
from random import choice, randrange

class Game():
    
    def __init__(self):
        print("New game")
        self.fight = True
    
    @property
    def fight(self):
        return self.__fight
    
    @fight.setter
    def fight(self, value):
        self.__fight = value

    def show_pokemons(self, player):
        player.set_pokemons()
        return [i.name for i in player.get_pokemons()]

    def init_battle(self, p1, p2):
        self.p1_id_first_pkmn = choice(p1.pokedex)
        self.p2_id_first_pkmn = choice(p2.pokedex)    
        p1.activ_pokemon = p1.get_pokemon(self.p1_id_first_pkmn)   
        p2.activ_pokemon = p2.get_pokemon(self.p2_id_first_pkmn)   
        print(p1.name + " invoks " + p1.activ_pokemon.name) 
        print(p2.name + " invoks " + p2.activ_pokemon.name) 

        print(p1.activ_pokemon.name + " speed: " + str(p1.activ_pokemon.speed))
        print(p2.activ_pokemon.name + " speed: " + str(p2.activ_pokemon.speed))

        if p1.activ_pokemon.speed > p2.activ_pokemon.speed:
            p1.initiative = True            
        else: 
            p2.initiative = True
        return 
        #return p1 if p1.activ_pokemon.speed > p2.activ_pokemon.speed else p2

    def show_menu(self, player):
        print("----------------------")
        print("player: " + player.name)
        print("my pokemon: " + player.activ_pokemon.name)
        print("hp: " + str(player.activ_pokemon.hp))
        print("choose: 1 - attack | 2 - swap | 3 - flee")
        print("----------------------")

    def choose_action(self, action, player, opponent):    
        if action == str(1):
            print("choix 1")
            player.activ_pokemon.attack_target(opponent.activ_pokemon)
           
        if action == str(2):
            print("choix 2")
        if action == str(3):
            self.exit()

    def exit(self):
        d = randrange(1,5)
        if d == 4:
            print("exit")
            self.fight = False            
        else:
            print("you can t exit")
     


g = Game()


p1 = player.Player()
print(p1.name)
print(g.show_pokemons(p1))


print("-----------")

p2 = player.Player()
print(p2.name)
print(g.show_pokemons(p2))

print("-----------")

g.init_battle(p1, p2)

if p1.initiative:
    print(p1.name + " begins the battle")

    while g.fight:
        g.show_menu(p1)
        action = input("choose an action: ")
        g.choose_action(action, p1, p2)

        if g.fight:
            g.show_menu(p2)
            action = input("choose an action: ")
            g.choose_action(action, p2, p1)


    

if p2.initiative:
    print(p2.name + " begins the battle")

    while g.fight:
        g.show_menu(p2)
        action = input("choose an action: ")
        g.choose_action(action, p2, p1)

        if g.fight:
            g.show_menu(p1)
            action = input("choose an action: ")
            g.choose_action(action, p1, p2)