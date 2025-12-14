# V 4.2

# ===================================================
# Byte.Arcade Games – © 2025 by Lou
# Tous droits réservés.

# Ce jeu est une création originale de Byte.Games Studios.
# Il est protégé par les dispositions du Code de la propriété intellectuelle (France et Union européenne).

# Cela inclut notamment :
# – le code source
# – les visuels et interfaces
# – le nom, le logo et l’univers du jeu

# Toute reproduction, modification, distribution ou utilisation, même partielle, sans l’accord écrit de l’auteur est strictement interdite.

# Ce projet est à but éducatif et non commercial.

# Contact développeur : lou@tingvall.se
#© 2025 Lou T. – Byte.Games Studios
# ===================================================





import time
import random
import os
print("\n" * 15)
print("Dossier d'exécution :", os.getcwd())
print("\nImportation des dossier.txt", end="", flush=True)

for _ in range(3):
    time.sleep(0.5)
    print(".", end="", flush=True)
print("\n")

time.sleep(1)
os.system('cls' if os.name == 'nt' else 'clear')
print("=== BIENVENUE DANS BYTE.ARCADE ===", "\n" * 5)
time.sleep(2)
os.system('cls' if os.name == 'nt' else 'clear')
time.sleep(0.2)
print("Un jeu original créé par Lou.T")
time.sleep(2)
os.system('cls' if os.name == 'nt' else 'clear')
time.sleep(0.2)
print("Byte.Arcade Games – © 2025 by Lou.T")
time.sleep(2)
os.system('cls' if os.name == 'nt' else 'clear')
time.sleep(0.2)
print("Un jeu original de Byte.Games Studios – © 2025 by Lou.T")
time.sleep(2)
os.system('cls' if os.name == 'nt' else 'clear')
time.sleep(0.2)
print("Version du jeu : V 4.0\n")

print("Chargement des scripts", end="", flush=True)

for _ in range(3):
    time.sleep(0.5)
    print(".", end="", flush=True)

os.system('cls' if os.name == 'nt' else 'clear')
print("Version du jeu : V 4.0\n")
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
    print("=== ROULETTE RUSSE MULTIJOUEUR ===      TAPEZ 4\n")
    print("=== BLACK JACK REMASTERED === TAPEZ 5\n")
    print("=== CHANGELOG === TAPEZ 7\n")
    print("=== FAQ === TAPEZ 8\n")
    print("=== COPYRIGHT === TAPEZ 9\n")
    print("=== QUITTER === TAPEZ 0\n\n")

# REGLES DE TOUS LES JEUX :

    def regles_juste_prix():
            print("\n=== RÈGLES DU JUSTE PRIX ===\n")
            print("Le but du jeu est de deviner un nombre mystère choisi aléatoirement par l’ordinateur.")
            print("Ce nombre est compris entre 1 et 100 (ou plus selon la configuration).")
            print("À chaque tentative, le jeu vous indique si le nombre à deviner est plus grand ou plus petit.")
            print("Le jeu continue jusqu’à ce que vous trouviez le bon nombre.")
            print("Essayez de trouver le juste prix en un minimum d’essais !\n")

    def regles_juste_prix_multi():
        print("\n=== RÈGLES DU JUSTE PRIX – MULTIJOUEUR ===\n")
        print("Chaque joueur devra, à tour de rôle, deviner le nombre mystère généré par l’ordinateur.")
        print("Le nombre est compris entre 1 et 100.")
        print("Le jeu vous indique à chaque fois si le nombre est plus grand ou plus petit.")
        print("Le joueur qui trouve le juste prix en premier remporte la partie.")
        print("Tous les joueurs ont les mêmes chances, à vous d’être le plus malin !\n")

    def regles_roulette_russe():
        print("\n=== RÈGLES DE LA ROULETTE RUSSE – SOLO ===\n")
        print("Vous êtes seul face à un robot et un revolver virtuel contenant une seule balle")
        print("placée aléatoirement dans l'une des 6 chmabres du braillet.")
        print("À chaque tour, vous tirez sur le robot, puis, sur vous.")
        print("Si vous tirez sur le robot et que la balle est dans la chambre, vous gagnez.")
        print("Sinon… Vous êtes mort* et vous perdez!\n")
        print("*virtuellement")

    def regles_roulette_russe_multi():
        print("\n=== RÈGLES DE LA ROULETTE RUSSE – MULTIJOUEUR ===\n")
        print("Les joueurs se passent un revolver virtuel contenant une seule balle, placée aléatoirement dans l'une des x chambre.")
        print("Chaque joueur tire à son tour. Si la chambre est vide, le jeu continue normalement.")
        print("Si une balle est tirée, le joueur concerné est éliminé, et la partie continue sans le joueur éliminé.")
        print("Le suspense augmente à chaque tour !")
        print("Jouez prudemment… ou pas !\n")

    def regles_blackjack_simplifie():
        print("\n=== RÈGLES DU BLACKJACK SIMPLIFIÉ ===\n")
        print("Le but du jeu est d’obtenir un total de points le plus proche possible de 21 sans le dépasser.")
        print("Chaque joueur reçoit au départ deux nombres entre 1 et 11 et une cagnotte de 100 jetons.")
        print("Vous pouvez ensuite choisir de tirer un nouveau nombre, ou de vous arrêter.")
        print("Chaque nouveau nombre tiré est aussi compris entre 1 et 11.")
        print("Si votre total dépasse 21, vous perdez automatiquement la partie ainsi que votre mise en jetons.")
        print("Si vous gagnez, vous remportez votre mise x 2.")
        print("Le croupier n'a plus le droit de tirer si il dépasse 17.")
        print("Une fois que vous vous arrêtez, le jeu affiche votre total de jetons final.")
        print("Essayez d’atteindre exactement 21… ou de vous en approcher le plus possible sans dépasser !\n")

# Fin des règles des jeux

    while True:
        try:
            game = int(input("-> "))
        except ValueError:
            game = -1

        if game in [0, 1, 2, 3,4, 5, 7, 8, 9]:
            break
        else:
            print("Veuillez entrer 0, 1, 2, 3, 4, 5, 7, 8, 9.")

    if game == 0:
        print("Merci d'avoir joué ! À bientôt !")
        break

    elif game == 9:
        os.system('cls' if os.name == 'nt' else 'clear')
        file_path = os.path.join(os.path.dirname(__file__), "Copyright.txt")

        with open(file_path, "r", encoding="utf-8") as f:

            print(f.read())
            input("\n\n\nAppuyez sur ENTRÉE pour quitter")
            os.system('cls' if os.name == 'nt' else 'clear')



    elif game == 8:
        os.system('cls' if os.name == 'nt' else 'clear')
        file_path = os.path.join(os.path.dirname(__file__), "faq.txt")

        with open(file_path, "r", encoding="utf-8") as f:

            print(f.read())
            input("\n\n\nAppuyez sur ENTRÉE pour quitter")
            os.system('cls' if os.name == 'nt' else 'clear')


    elif game == 7:

        os.system('cls' if os.name == 'nt' else 'clear')
        file_path = os.path.join(os.path.dirname(__file__), "changelog.txt")

        with open(file_path, "r", encoding="utf-8") as f:

            print("\n===== CHANGELOG =====\n")
            print(f.read())
            print("======================\n")
        input("\n\n\nAppuyez sur ENTRÉE pour quitter")
        os.system('cls' if os.name == 'nt' else 'clear')


    
    elif game == 1:

        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n=== LE JUSTE PRIX ===")
        regles_juste_prix()
        print("Appuyez sur ENTRÉE pour coninuer.")
        input()
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
        regles_juste_prix_multi()
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
        regles_roulette_russe()
        print("Appuyez sur ENTRÉE pour continuer.")
        input()
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
        regles_roulette_russe_multi()
        print("Appuyez sur ENTRÉE pour continuer.")
        input
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

    elif game == 5:

        os.system('cls' if os.name == 'nt' else 'clear')
        print("=== BLACK JACK REMASTERED ===")
        time.sleep(1.5)

        os.system('cls' if os.name == 'nt' else 'clear')
        print("Chargement des données du jeu", end="")
        for _ in range(3):
            time.sleep(0.5)
            print(".", end="", flush=True)

        os.system('cls' if os.name == 'nt' else 'clear')
        regles_blackjack_simplifie()
        input("Appuyez sur ENTRÉE pour continuer.")
        
        cagnotte = 100
        print(f"Votre cagnotte est de {cagnotte} jetons.")
                    
        while True:

            while True:
                try:
                    mise = int(input("Votre mise :\n-> "))
                    if 1 <= mise <= cagnotte:
                        break
                    else:
                        print("Mise invalide. Elle doit être entre 1 et votre cagnotte.")
                except ValueError:
                    print("Entrez un nombre entier.")


            time.sleep(1)
            print("Le croupier vous donne vos deux premières cartes...")
            
            cartes = [random.randint(1, 11), random.randint(1, 11)]
            croupier = [random.randint(1, 11), random.randint(1, 11)]

            print(f"Vos cartes : {cartes} (total = {sum(cartes)})")

            perdu = None

            if sum(cartes) == 21:
                print("Black Jack naturel !")
                time.sleep(1)
                print("Le croupier vérifie ses cartes...")
                print(f"Cartes du croupier : {croupier} (total = {sum(croupier)})")

                if sum(croupier) == 21:
                    print("Égalité, le croupier a aussi un Black Jack.")
                    perdu = "egalite"
                else:
                    print("Vous gagnez avec un Black Jack naturel !")
                    perdu = "non"
            else:
                while sum(cartes) < 21:
                    print(f"\nVos cartes : {cartes} (total = {sum(cartes)})")
                    print("Tirer une carte ? OUI = 1     NON = 2")
                    try:
                        choix = int(input("-> "))
                    except ValueError:
                        choix = -1

                    if choix == 1:
                        nouvelle = random.randint(1, 11)
                        cartes.append(nouvelle)
                        print(f"Vous tirez un {nouvelle} !")
                        if sum(cartes) > 21:
                            print(f"Total = {sum(cartes)}. Vous avez dépassé 21.")
                            perdu = "perdu"
                            break
                        elif sum(cartes) == 21:
                            print("Parfait ! Vous avez 21.")
                            break
                    elif choix == 2:
                        break
                    else:
                        print("Choix invalide.")

                if perdu != "perdu":
                    print("\nAu tour du croupier...")
                    print(f"Cartes du croupier : {croupier} (total = {sum(croupier)})")
                    while sum(croupier) < 17:
                        time.sleep(1)
                        tirage = random.randint(1, 11)
                        croupier.append(tirage)
                        print(f"Le croupier tire un {tirage} (total = {sum(croupier)})")

                    joueur_total = sum(cartes)
                    croupier_total = sum(croupier)
                    print(f"\nVotre total : {joueur_total}")
                    print(f"Total du croupier : {croupier_total}")

                    if croupier_total > 21 or joueur_total > croupier_total:
                        print("Vous gagnez la manche !")
                        perdu = "non"
                    elif joueur_total == croupier_total:
                        print("Égalité ! Personne ne gagne ni ne perd.")
                        perdu = "egalite"
                    else:
                        print("Le croupier gagne.")
                        perdu = "perdu"

            if perdu == "perdu":
                cagnotte -= mise
                print(f"Vous avez perdu {mise} jetons.")
            elif perdu == "non":
                cagnotte += mise
                print(f"Vous avez gagné {mise} jetons !")
            else:
                print("Votre cagnotte reste inchangée.")

            print(f"Cagnotte actuelle : {cagnotte}")
            rpdmenu = input("Appuyez sur ENTRÉE pour continuer ou tapez 1 pour revenir au menu.")
            if rpdmenu == 1:
                break
            else:
                pass