##### TEST SERVEUR PYTHON ##############



########## import
import socket
import threading
import player
import game



# define socket => pokesocket
pokeSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# localhost set for test, use only '' next
ipServer=''
# configure socket
pokeSocket.bind((ipServer, 1443))
pokeSocket.listen(5)


def sendToPlayer(var:str):
    try:
        playerSocket.send(var.encode())
    except BrokenPipeError:
        print("Client unreachable")
        pass

# definitions of the distant players for the pokeserver
while True:

    # accept connections from players, closes after 2mn without connection
    try:
        pokeSocket.settimeout(120)
        (playerSocket, playerIP)=pokeSocket.accept()
    except TimeoutError:
        print("No connected client: server closes")
        exit()
    #playerSocket.setblocking(0)

    # Now, use the socket
    # print players adress
    print(f"Le joueur {playerIP} s'est connecté")
    # size buffer of 8K, TODO estimate size to be used

    err=""
    try:
        # set 10s of timeout
        playerSocket.settimeout(10)
        # if msgOk[0]:
        playerMsg=playerSocket.recv(8192)
    # if timeout is reached
    # TODO treat other errors
    except TimeoutError:
        print(f"Request from {playerIP} unavailable")
        # set error flag to true
        err="Timeout"


    # Treat program
    if err != "":
        playerSocket.send(err.encode())
    else:
        print(f"{playerMsg}")     
        sendToPlayer("pong")
        print("pong sent")

        # TODO start poke game and player interactions

        # exemple:
        # stop = game.start()
        # if stop == False:

        if game.start(playerSocket) == False:
            sendToPlayer("Game Stop")

    
    print("Looking for a new connection")
