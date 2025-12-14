# ===================================================

# P*_T*r**n*l – * 20** by L**  
# T**s d**i** r***r**s.
# *e **u, a**si que *on ***e ***rc*, **s ***s***c*s et son i*e**it* v*s*e**e,
# *o*t p*o**é**s par le d***t d’****ur s***n les *isp**iti**s du C*** de la p***ri*** i***l*e***el*e (F*a**e, U***n ***op***ne).
# Toute *ep**d**ti**, **st***u***n, mo****ca***n ou u***is***on non a**or***e, même p*rti***e, est *n**rd**e sans *'a***r* p*é**a*le de l’a*t*ur.
# Contact développeur : lou@tingvall.se

# ===================================================




import time
import random
import os
print("\n" * 15)
print("Dossier d'exécution :", os.getcwd())
print("\nChargement de la borne d’arcade", end="", flush=True)

for _ in range(3):
    time.sleep(0.5)
    print(".", end="", flush=True)
print("\n")

time.sleep(1)
os.system('cls' if os.name == 'nt' else 'clear')
print("=== BIENVENUE DANS P*_*E*M*N*L ===", "\n" * 5)
time.sleep(2)
os.system('cls' if os.name == 'nt' else 'clear')
time.sleep(0.2)
print("Un jeu o**g**** c**é par L**.*")
time.sleep(2)
os.system('cls' if os.name == 'nt' else 'clear')
time.sleep(0.2)
print("**.*e****al – * 20** by L**.*\n")
time.sleep(2)

print("Chargement des scripts", end="", flush=True)

for _ in range(3):
    time.sleep(0.5)
    print(".", end="", flush=True)
print("\n")
os.system('cls' if os.name == 'nt' else 'clear')

print("P**Te**i*a* – * 2025 by L**.*\n")
print("Chargement des scripts", end="", flush=True)

for _ in range(3):
    time.sleep(0.5)
    print(".", end="", flush=True)
print("\n")
os.system('cls' if os.name == 'nt' else 'clear')

while True:

    print("A quel jeu voulez-vous jouer ?\n")
    print("Sélectionner un jeu pour voir les règles", "\n" * 5)
    print("=== JUSTE PRIX ===      TAPEZ 1\n")
    print("=== JUSTE PRIX MULTIJOUEUR === TAPEZ 2\n")
    print("=== ROULETTE RUSSE ===      TAPEZ 3\n")
    print("== ROULETTE RUSSE MULTIJOUEUR ===      TAPEZ 4\n")
    print("=== QUITTER === TAPEZ 0\n")
    print("=== COPYRIGHT === TAPEZ 9\n")
    print("=== FAQ === TAPEZ 8\n")
    print("=== CHANGELOG === TAPEZ 7\n\n")

    while True:
        try:
            game = int(input("-> "))
        except ValueError:
            game = -1

        if game in [0, 1, 2, 3,4, 7, 8, 9]:
            break
        else:
            print("Veuillez entrer 0, 1, 2 ou 3.")

    if game == 0:
        print("Merci d'avoir joué ! À bientôt !")
        break

    elif game == 9:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n\n===================================================\n")
        print("P***er***al – * 20** by Lou")
        print("T**s ***its *és****s.")
        print("***T******l, ainsi que son **de s**rce, ses ress****es et son id**tité v***elle, sont pr***g*s par le ***it d’***eur s***n les disp****ions du Code de la propriété intellectuelle (France, Union européenne).")
        print("**ute *epr***ct**n, **st****t**n, **d***cat*** ou **ili***ion n*n ***orisée, **me part***le, est int***ite sans l'ac**rd pr**lable de l’a****r.")
        print("Contact développeur : lou@tingvall.se")
        print("* 2*** by L**.*. Tous d***ts r*se***s.\n")
        print("===================================================\n\n")
        print("Appuyez sur ENTRÉE pour quitter.")
        input()

    elif game == 8:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Q : Comment lancer un jeu dans P***er***al ?")
        print("R : Depuis le menu principal, tapez le numéro correspondant au jeu souhaité puis validez avec Entrée.\n")
        print("Q : Que faire si je me trompe en entrant un nombre ?")
        print("R : Le jeu vous demandera de ressaisir votre réponse tant que la donnée entrée n’est pas valide.\n")
        print("Q : Comment fonctionne le mode multijoueur ?")
        print("R : Vous devez entrer le nombre de joueurs, puis chaque joueur choisit son pseudo et participe à son tour.\n")
        print("Q : Puis-je sauvegarder mes scores ?")
        print("R : Pour le moment, le jeu ne sauvegarde pas automatiquement les scores. Vous pouvez noter vos résultats manuellement.\n")
        print("Q : Comment signaler un bug ou faire une suggestion ?")
        print("R : Envoyez un mail à // l****ing****.** // avec une description claire du problème ou de votre idée.\n")
        print("Q : Ce jeu est-il gratuit ?")
        print("R : Oui, C****n***ay est un projet personnel gratuit, à but éducatif et ludique.\n")
        print("Q : Est-ce que mes données personnelles sont collectées ?")
        print("R : Non, le jeu ne collecte aucune donnée personnelle.\n")
        time.sleep(10)

    elif game == 7:

        os.system('cls' if os.name == 'nt' else 'clear')
        file_path = os.path.join(os.path.dirname(__file__), "changelog.txt")

        with open(file_path, "r", encoding="utf-8") as f:

            print("\n===== CHANGELOG =====\n")
            print(f.read())
            print("======================\n")

    
    elif game == 1:

        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n=== LE JUSTE PRIX ===")
        print("Devinez un nombre aléatoire entre 1 et le niveau choisi, en un minimum d'essais.")
        print("\nChoisissez un niveau de difficulté (1 à 5) :")
        print("1 = 1 à 50 | 2 = 1 à 100 | 3 = 1 à 150 | 4 = 1 à 200 | 5 = 1 à 300")

        while True:
            try:
                lvl = int(input("-> "))
            except ValueError:
                lvl = -1

            if lvl == 1:
                max_val = 50
                break
            elif lvl == 2:
                max_val = 100
                break
            elif lvl == 3:
                max_val = 150
                break
            elif lvl == 4:
                max_val = 200
                break
            elif lvl == 5:
                max_val = 300
                break
            else:
                print("Choix invalide. Réessayez.")

        essais = 0
        juste_prix = random.randint(1, max_val)
        print("\nC'est parti ! Devinez le bon nombre :")

        while True:

            essais += 1
            try:
                guess = int(input("-> "))
            except ValueError:
                print("Veuillez entrer un nombre.")
                continue

            if guess < juste_prix:
                print("C'est plus grand !")

            elif guess > juste_prix:
                print("C'est plus petit !")

            elif guess == juste_prix:
                print("=== BRAVO ! Tu as trouvé le bon nombre ! ===")
                break

        score = (max_val * (lvl if lvl != 1 else 1.5) * 40) / essais
        print(f"Tu as fini avec un score de {int(score)} points.")

        input("Appuie sur Entrée pour revenir au menu...")

    elif game == 2:

        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n=== JUSTE PRIX MULTIJOUEUR ===")
        print("Chaque joueur choisit un nombre. Celui qui est le plus proche du nombre mystère gagne.")
        print("Tapez Entrée pour continuer...")
        input()
        print("\nChoisissez le nombre le plus haut possible (max 9999) :")

        while True:

            try:
                maxx = int(input("-> "))
            except ValueError:
                maxx = -1

            if 1 <= maxx <= 9999:
                break

            else:
                print("Erreur : entrez un nombre entre 1 et 9999.")

        print("\nCombien de joueurs ?")

        while True:
            try:
                nbr = int(input("-> "))
            except ValueError:
                nbr = -1

            if 1 <= nbr <= 19:
                break

        print("\nJoueur 1 commence :")

        players_choices = {}
        mystere = random.randint(1, maxx)

        for i in range(nbr):

           while True:
           
            try:
                choix = int(input(f"Joueur {i+1}, choisissez un nombre entre 1 et {maxx} -> "))
                if 1 <= choix <= maxx:
                    players_choices[i] = choix
                    break
                else:
                    print("Erreur : hors limites.")
            except ValueError:
                print("Erreur : veuillez entrer un nombre.")

        ecarts = {joueur: abs(choix - mystere) for joueur, choix in players_choices.items()}
        joueur_plus_proche = min(ecarts, key=ecarts.get)
        valeur_plus_proche = players_choices[joueur_plus_proche]

        print("\n=== RÉSULTATS ===")
        print(f"Le nombre mystère était {mystere}")
        print(f"Le joueur le plus proche est : Joueur {joueur_plus_proche + 1}")
        print(f"Il avait choisi {valeur_plus_proche}, avec un écart de {ecarts[joueur_plus_proche]}.")
        input("\nAppuyez sur Entrée pour revenir au menu...")

    elif game == 3:

        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n=== ROULETTE RUSSE ===")
        print("Survivrez-vous au robot ? Choisissez la difficulté.")
        print("1 chance sur combien de se faire éliminer ?")
        
        while True:

            try:
                proba = int(input("-> "))
            except ValueError:
                print("Erreur : veuillez entrer un nombre.")

            if proba >= 1:
                break

            else:
                print("Erreur : la probabilité doit être au moins 1.")

        os.system('cls' if os.name == 'nt' else 'clear')
        print("\nChoisissez le nombre malchanceux entre 1 et", proba)

        while True:

            try:
                nombre_malchanceux = int(input("-> "))
            except ValueError:
                print("Erreur : veuillez entrer un nombre.")

            if 1 <= nombre_malchanceux <= proba:
                break
            else:
                print("Erreur : ce nombre doit être entre 1 et", proba)

        os.system('cls' if os.name == 'nt' else 'clear')
        print("\nActiver le mode rapide ?")
        print("1 = OUI     2 = NON")

        while True:

            try:
                rpd = int(input("-> "))
            except ValueError:
                print("Erreur : veuillez entrer un nombre.")

            if rpd in [1, 2]:
                break

            else:
                print("Erreur : tapez 1 ou 2.")

        if rpd == 1:

            while True:

                xxxr = random.randint(1, proba)
                if xxxr == nombre_malchanceux:
                    print("\nLe robot est éliminé !")
                    robot = 1
                    human = 2
                    break

                else:
                    print("Le robot a survécu.")
                    robot = 2

                print("\nÀ votre tour...")
                xxx = random.randint(1, proba)

                if xxx == nombre_malchanceux:
                    print("Vous vous êtes fait éliminer...")
                    human = 1
                    break

                else:
                    print("Vous avez survécu !")

            print("\n=== FIN DE LA PARTIE ===")
            if human == 2:
                print("Vous avez gagné ! Félicitations !")

            else:
                print("Vous avez perdu. Le robot a gagné.")
                
            input("\nAppuyez sur Entrée pour revenir au menu...")
            os.system('cls' if os.name == 'nt' else 'clear')

        elif rpd == 2:

            os.system('cls' if os.name == 'nt' else 'clear')
            while True:

                xxxr = random.randint(1, proba)
                print("Appuyez sur ENTRÉE pour tirez sur le robot.")
                input()
                for _ in range(3):
                    time.sleep(0.5)
                    print(".", end="", flush=True)
                time.sleep(1.5)
                print("\n")
                if xxxr == nombre_malchanceux:
                    print("\nVous avez tué le robot!")
                    robot = 1
                    human = 2
                    break

                else:
                    print("Le robot a survécu.")
                    robot = 2

                print("\nAppuyez sur ENTRÉE pour tirer...")
                input()
                xxx = random.randint(1, proba)
                for _ in range(3):
                    time.sleep(0.5)
                    print(".", end="", flush=True)
                print("\n")

                if xxx == nombre_malchanceux:
                    print("Vous êtes mort.")
                    time.sleep(1.5)
                    human = 1
                    break

                else:
                    print("Vous avez survécu !")
                    time.sleep(1.5)

            print("\n=== FIN DE LA PARTIE ===")

            if human == 2:
                print("Vous avez gagné ! Félicitations !")

            else:
                print("Vous avez perdu. Le robot a gagné.")

            input("\nAppuyez sur Entrée pour revenir au menu...")

    elif game == 4:

        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n=== ROULETTE RUSSE MULTIJOUEUR ===")
        print("\nQui sera le dernier survivant ?")
        print("\nCombien de joueur êtes-vous ?")

        while True:

                try:
                    rrnbr = int(input("->"))
                except ValueError:
                    rrnbr = -1

                if rrnbr >= 2:
                    break

                else:
                    print("\nVeuillez saisir un nombre supérieur ou égal à 2.")
                    print(f"\nInsérez votre prénom ou un pseudo de votre choix.")

        players_name = []
        tour = 0

        for i in range(rrnbr):

                namerr = input("->")
                players_name.append(namerr)
                os.system('cls' if os.name == 'nt' else 'clear')

                while len(players_name) > 1:

                    irr = players_name[tour % len(players_name)]

                    print(f"Au tour de {irr} de connaître son sort.")
                    go = input("Pressez ENTRÉE pour connaître votre sort\n")

                    if go == "":

                        if random.randint(1, 6) == 1:
                                print(f"{irr} n'as pas survécu...")
                                players_name.remove(irr)

                        else:
                                print(f"{irr} a survécu !")
                        tour += 1

                    else:
                        print("erreur : veuillez supprimer tout caractère dans les champs et appuyez sur ENTRÉE.")

                    print(f"Le gagnant de la partie est {players_name[0]} !")
                    input("Pressez ENTRÉE pour revenir au menu.")
                
                    break
