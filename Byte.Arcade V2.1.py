import time
import random

while True:
    print("\n" * 10)
    print("=== BIENVENUE DANS LA BORNE D'ARCADE ===\n")
    time.sleep(1.5)

    print("A quel jeu voulez-vous jouer ?\n")
    time.sleep(1.5)

    print("Sélectionner un jeu pour voir les règles\n")
    time.sleep(1.5)

    print("=== JUSTE PRIX ===      TAPEZ 1")
    print("=== JUSTE PRIX MULTIJOUEUR === TAPEZ 2")
    print("=== ROULETTE RUSSE ===      TAPEZ 3")
    print("=== QUITTER === TAPEZ 0\n")

    # Sélection du jeu
    while True:
        try:
            game = int(input("-> "))
        except ValueError:
            game = -1

        if game in [0, 1, 2, 3]:
            break
        else:
            print("Veuillez entrer 0, 1, 2 ou 3.")

    if game == 0:
        print("Merci d'avoir joué ! À bientôt !")
        break

    elif game == 1:  # Juste Prix (solo)
        print("\n=== LE JUSTE PRIX ===")
        print("Devinez un nombre aléatoire entre 1 et le niveau choisi, en un minimum d'essais.")
        print("Tapez Entrée pour continuer...")
        input()

        # Confirmation de compréhension des règles
        while True:
            print("\nAvez-vous compris les règles ?")
            print("1 = OUI / 2 = NON")
            try:
                yesno = int(input("-> "))
            except ValueError:
                yesno = -1

            if yesno == 1:
                break
            elif yesno == 2:
                print("Relisez les règles ci-dessus.")
            else:
                print("Veuillez taper 1 ou 2.")

        # Choix du niveau
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

        # Partie du jeu
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

        # Score final
        score = (max_val * (lvl if lvl != 1 else 1.5) * 40) / essais
        print(f"Tu as fini avec un score de {int(score)} points.")

        # Retour au menu
        input("Appuie sur Entrée pour revenir au menu...")
    elif game == 2:  # Juste Prix Multijoueur
        print("\n=== JUSTE PRIX MULTIJOUEUR ===")
        print("Chaque joueur choisit un nombre. Celui qui est le plus proche du nombre mystère gagne.")
        print("Tapez Entrée pour continuer...")
        input()

        # Choix du nombre maximum
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

        # Nombre de joueurs
        print("\nCombien de joueurs ? (max 19)")
        while True:
            try:
                nbr = int(input("-> "))
            except ValueError:
                nbr = -1

            if 1 <= nbr <= 19:
                break
            else:
                print("Erreur : entrez un nombre entre 1 et 19.")

        # Choix des joueurs
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

        # Calcul du plus proche
        ecarts = {joueur: abs(choix - mystere) for joueur, choix in players_choices.items()}
        joueur_plus_proche = min(ecarts, key=ecarts.get)
        valeur_plus_proche = players_choices[joueur_plus_proche]

        # Résultat
        print("\n=== RÉSULTATS ===")
        print(f"Le nombre mystère était {mystere}")
        print(f"Le joueur le plus proche est : Joueur {joueur_plus_proche + 1}")
        print(f"Il avait choisi {valeur_plus_proche}, avec un écart de {ecarts[joueur_plus_proche]}.")

        # Retour au menu
        input("\nAppuyez sur Entrée pour revenir au menu...")
    elif game == 3:  # Roulette Russe
        print("\n=== ROULETTE RUSSE ===")
        print("Survivrez-vous au robot ? Choisissez la difficulté.")
        print("1 chance sur combien de se faire éliminer ?")
        
        while True:
            try:
                proba = int(input("-> "))
                if proba >= 1:
                    break
                else:
                    print("Erreur : la probabilité doit être au moins 1.")
            except ValueError:
                print("Erreur : veuillez entrer un nombre.")

        print("\nChoisissez le nombre malchanceux entre 1 et", proba)
        while True:
            try:
                nombre_malchanceux = int(input("-> "))
                if 1 <= nombre_malchanceux <= proba:
                    break
                else:
                    print("Erreur : ce nombre doit être entre 1 et", proba)
            except ValueError:
                print("Erreur : veuillez entrer un nombre.")

        print("\nActiver le mode rapide ?")
        print("1 = OUI     2 = NON")
        while True:
            try:
                rpd = int(input("-> "))
                if rpd in [1, 2]:
                    break
                else:
                    print("Erreur : tapez 1 ou 2.")
            except ValueError:
                print("Erreur : veuillez entrer un nombre.")

        # MODE RAPIDE ACTIVÉ
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
        # MODE RAPIDE DÉSACTIVÉ
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
                print("🎉 Vous avez gagné ! Félicitations !")
            else:
                print("💀 Vous avez perdu. Le robot a gagné.")

            input("\nAppuyez sur Entrée pour revenir au menu...")
