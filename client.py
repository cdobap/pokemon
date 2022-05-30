########### imports
import socket
from player import Player
import pokemon

# player information -> on BDD ?
playerIP = "192.168.1.15"
playerPort = 1443

def show_menu(Rxdata:str,p1:Player):
    # TODO a couper
    print(f"rxdata: {Rxdata}")
    data=Rxdata.split("'")
    print(f"datasanssplit {data}")
    data=data[1].split(";")
    print(f"data {data}")
    
    pokemon=data[0][2:]
    pokemonhp=data[1]
    advpokemon=data[2]
    advpokemonhp=data[3]
    print("--------------------------------")
    print(f"player: {player1.name} ")    
    print(f"my pokemon: {pokemon} {pokemonhp} hp")
    print(f"opponent pokemon: {advpokemon} {advpokemonhp} hp")
    if int(pokemonhp) > 0:
        print("choose: 1 - attack | 2 - swap | 3 - flee")    
    else:
        print("choose: 2 - swap | 3 - flee")
    
    print(".........")


#### TODO : créer les inputs client 
#
# noms joueurs etc ...
#
player1=Player()
player2=Player()

# define socket
playerSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# connect to server

try:
    playerSocket.connect((playerIP, playerPort))
except ConnectionError:
    print("Connexion unavailable try later")
    exit()
    
print(f"Connection on {playerPort}")
# always send "a_string".encode() to server
playerSocket.send("ping".encode())
# if var is int user str(intvariable).encode
#playerSocket.send(str(toto).encode())
# userInput=input("Veuiller entrer quelque chose: ")
# playerSocket.send(str(userInput).encode())
# revceive msg from server buffer
print("ping")
pokeMsg=playerSocket.recv(8192)
print(f"{pokeMsg}")

while str(pokeMsg)!="b'Game Stop'" and str(pokeMsg)!="b''":
    pokeMsg=playerSocket.recv(8192)
    #print(pokeMsg)
    show_menu(str(pokeMsg),player1)

# close connection
print("Closing connection")
playerSocket.close()