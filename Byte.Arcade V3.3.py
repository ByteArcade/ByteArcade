



# ===================================================

# Py_Terminal – © 2025 by Lou  
# Tous droits réservés.
# Ce jeu, ainsi que son code source, ses ressources et son identité visuelle,
# sont protégés par le droit d’auteur selon les dispositions du Code de la propriété intellectuelle (France, Union européenne).
# Toute reproduction, distribution, modification ou utilisation non autorisée, même partielle, est interdite sans l'accord préalable de l’auteur.
# Contact développeur : lou@tingvall.se

# ===================================================




print("\n" * 15, "Code'n'play – © 2025 by Lou\n")
print("=== BIENVENUE DANS PY_TERMINAL ===", "\n" * 5)

import time
import random

import os
print("Dossier d'exécution :", os.getcwd())

print("Chargement de la borne d’arcade", end="", flush=True)
for _ in range(3):
    time.sleep(0.5)
    print(".", end="", flush=True)
print("\n")

time.sleep(1)

while True:

    print("A quel jeu voulez-vous jouer ?\n")
    print("Sélectionner un jeu pour voir les règles", "\n" * 5)
    print("=== JUSTE PRIX ===      TAPEZ 1\n")
    print("=== JUSTE PRIX MULTIJOUEUR === TAPEZ 2\n")
    print("=== ROULETTE RUSSE ===      TAPEZ 3\n")
    print("== ROULETTE RUSSE MULTIJOUEUR ===      TAPEZ 4\n")
    print("=== QUITTER === TAPEZ 0\n")
    print("=== COPYRIGHT === TAPEZ 9\n")

    while True:
        try:
            game = int(input("-> "))
        except ValueError:
            game = -1

        if game in [0, 1, 2, 3,4, 9]:
            break
        else:
            print("Veuillez entrer 0, 1, 2 ou 3.")

    if game == 0:
        print("Merci d'avoir joué ! À bientôt !")
        break

    elif game == 9:
        print("\n\n===================================================\n")
        print("Py_Terminal – © 2025 by Lou")
        print("Tous droits réservés.")
        print("Py_Terminal, ainsi que son code source, ses ressources et son identité visuelle, sont protégés par le droit d’auteur selon les dispositions du Code de la propriété intellectuelle (France, Union européenne).")
        print("Toute reproduction, distribution, modification ou utilisation non autorisée, même partielle, est interdite sans l'accord préalable de l’auteur.")
        print("Contact développeur : lou@tingvall.se")
        print("© 2025 by Lou.T. Tous droits réservés.\n")
        print("===================================================\n\n")

    elif game == 1:

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

        elif rpd == 2:

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

                print("\nAppuyez sur Entrée pour tirer...")
                input()
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

    elif game == 4:

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
