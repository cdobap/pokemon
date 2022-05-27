##### TEST SERVEUR PYTHON ##############



########## import
import socket
import select

# define socket => pokesocket
pokeSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# localhost set for test, use only '' next
ipServer=''
# configure socket
pokeSocket.bind((ipServer, 1443))
pokeSocket.listen(5)

# definitions of the distant players for the pokeserver
while True:

    # accept connections from players
    (playerSocket, playerIP)=pokeSocket.accept()
    #playerSocket.setblocking(0)

    # Now, use the socket
    # print players adress
    print(f"Le joueur {playerIP} s'est connecté")
    # size buffer of 8K, TODO estimate size to be used

    err=False
    try:
        # set 5s of timeout
        playerSocket.settimeout(5.0)
        # if msgOk[0]:
        playerMsg=playerSocket.recv(8192)
    # if timeout is reached
    except TimeoutError:
        print(f"Request from {playerIP} unavailable")
        # set error flag to true
        err=True
        pass

    # Treat program
    if err:
        playerSocket.send("ERROR in data sent".encode())
    else:
        print(f"{playerMsg}")     
        playerSocket.send("pong".encode())
        print("pong sent")
    
    
    print("end while")
