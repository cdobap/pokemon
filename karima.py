gros exo
class pokemon():
    
    name=""
    hp=""
    
    def get_name(self):
        return self.name
    
    def set_name(self, var_name):
        self.name = var_name
    
    def attack(self):
        print(self.name + " attaque")


    pikachu=pokemon()


        
print(pikachu.name)
print(pikachu.hp)

pikachu.set_name("Pikachu")

pikachu.get_name()

pikachu.attack()

salameche=pokemon()

salameche.attack()

salameche.set_name("Salameche")