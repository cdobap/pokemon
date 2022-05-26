class Player():

    def __init__(self):
        name=input("your name: ")
        self.__name=name

    
    @property
    def name(self):
        return self.__name

    
p=Player()

print(p.name)