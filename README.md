### Bienvenue sur le jeu de combat pokemon : ###

1# Introduction:

Il y a deux joueurs, chaque joueur possède au depart 3 pokemons aléatoires.

un pokemon pour chaque joueur est choisit aléatoirement
Le combat commence et il se déroule tour par tour



2# Lancer le jeu:

    - Executer serveurJeuPokemon.py sur une machine
    - Dans le fichier client.py, modifier : 
        serverIP = "192.168.1.15"
            -> Mettre l'ip de la machine qui execute serveurJeuPokemon.py
        playerPort = 1443
            -> Note: Le port 1443 est normalement utilisé par défaut dans
            serveurJeuPokemon.py, sinon modifier ce fichier pour utiliser un
            port disponible : pokeSocket.bind((ipServer, 1443))
    - Executer client.py

L'option threading n'est pas encore utilisé, les joueurs seront amenés à
jouer sur une seule machine.


3# Combat mode d'emploi:

A chaque tour d'un joueur,
Les statistiques du pokemon actif et de celles de son adversaire sont affichées.

3 choix lui sont proposés "Attaquer", "Changer de pokemon" ou "Fuir":

  - Attaquer:
    Le pokemon actif du joueur attaque le pokemon adverse

  - Changer de pokemons
    Liste des pokemons disponibles du joueur est affichée.
    Il peut changer de pokemon actif

  - Fuir
    Le joueur a 1 chance sur 4 de fuir le combat.
    La partie est terminé si il fuit

Lorsqu'un pokemon est K.O (quand ses "HP" sont a 0), il ne peut plus combattre.

Le combat continue tant qu'il reste 2 pokemons en combat et qu'aucun joueur n'a fuit le combat.

La partie est terminé quand un joueur n'a plus aucun pokemon qui peut se battre

#4 NOTES IMPORTANTES


Pour l'instant les commandes du joueurs n'ont pas été implémentées sur le client, il faut utiliser la console du serveur.

La connexion au serveur se ferme automatiquement lorsqu'aucun client ne s'est connecté dans un intervalle de 2mn.
La connexion au serveur se ferme automatiquement au bout de 10 seconde sans recevoir de message de la part du client.

