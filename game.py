import database
import player
import pokemon
from random import choice

class Game():
    
    def __init__(self):
        print("New game")

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
        return p1 if p1.activ_pokemon.speed > p2.activ_pokemon.speed else p2

g = Game()

p1 = player.Player()
print(p1.name)
print(g.show_pokemons(p1))


p2 = player.Player()
print(p2.name)
print(g.show_pokemons(p2))


print(g.init_battle(p1, p2).name + " begins the battle")

while p2.activ_pokemon.hp > 0 and p1.activ_pokemon.hp > 0:
    p1.activ_pokemon.attack_target(p2.activ_pokemon)
    p2.activ_pokemon.attack_target(p1.activ_pokemon)
