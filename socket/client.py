########### imports
import socket

# player information -> on BDD ?
playerIP = "192.168.1.15"
playerPort = 1443

toto=0
# define socket
playerSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# connect to server
playerSocket.connect((playerIP, playerPort))
print(f"Connection on {playerPort}")
# always send "a_string".encode() to server
#playerSocket.send("ping".encode())
# if var is int user str(intvariable).encode
#playerSocket.send(str(toto).encode())
userInput=input("Veuiller entrer quelque chose: ")
playerSocket.send(str(userInput).encode())
# revceive msg from server buffer
print("ping")
pokeMsg=playerSocket.recv(8192)
print(f"{pokeMsg}")
# close connection
print("Closing connection")
playerSocket.close()