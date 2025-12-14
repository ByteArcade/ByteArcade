while True:


    import time



    print("     ")
    print("     ")
    print("     ")
    print("     ")
    print("                                                                             === BIENVENUE ===")
    print("     ")
    print("Nous vous souhaitons la bienvenu.")
    print("     ")

    time.sleep(1.5)

    print("A quel jeu voulez vous jouer ?")
    print("     ")

    time.sleep(1.5)

    print("selctionner un jeu pour voir les règles")
    print("     ")

    time.sleep(1.5)

    print("     ")
    print("     ")
    print("        === JUSTE PRIX ===      TAPEZ 1         === JUSTE PRIX === (multijouer eddition)       TAPEZ 2")
    print("     ")
    print("     ")
    print("     ")


    while True:

        try:
            game = int(input("->"))
        except ValueError:
            game = -1

        if game == 1:

            print("=== LE JUSTE PRIX ===")
            print("                                                                                     ")
            print("Le but du jeu : avoir le plus de points possible a la fin de la partie.")
            print("Pour y arriver vous aller devoir, en le moins d'essais possible,")
            print("deviner un nombre aleatoire entre 1 et le niveau selectionné.")
            print("     ")
            print("=== POUR SÉLÉCTIONNER CE JEU, TAPEZ 888 ===")


        elif game == 2:

            print("=== ATTENTION ! POUR JOUER A CE JEU VOUS DEVEZ ÊTRE PLUSIEURS ! ===")
            print("     ")
            print("=== LE JUSTE PRIX === (multijoueur eddition)")
            print("     ")
            print("Le but du jeu : être le plus près possible du nombre mystère à la fin de la manche.")
            print("     ")
            print("=== POUR SÉLÉCTIONNER CE JEU, TAPEZ  777 ===")


        elif game == 777:

            break


        elif game == 888:

            break



        print("     ")
        print("Vous avez choisis le jeu du just prix.")
        print("     ")
        time.sleep(1)
        print("Avez-vous compris les règles du jeu ?")
        print("     ")
        print("1 OUI        2 NON")


        while True:
            try:
                yesno = int(input())
            except ValueError:
                yesno = -1

            if yesno == 1:

                break


            elif yesno == 2:

                pass


            else:

                print("Veuillez taper 1 ou 2")
        

        if yesno == 1:

            print("     ")
            print("choisissez votre niveau entre 1 et 5, du plus facil au plus dure.")
            print("     ")
            print("niveau 1 = 1-50 /// niveau 2 = 1-100 /// niveau 3 = 1-150 /// niveau 4 = 1-200 /// niveau 5 = 1-300")


            while True:


                try:
                    lvl = int(input())
                except ValueError:
                    lvl = -1


                if lvl == 1:
                    max = 50
                    break

                elif lvl == 2:
                    max = 100
                    break

                elif lvl == 3:
                    max = 150
                    break

                elif lvl == 4:
                    max = 200
                    break

                elif lvl == 5:
                    max = 300
                    break

                else:
                    print("ERROR")



            print("     ")
            print("     ")
            print("     ")
            print("C'est parti ! Bonne chance !")
            print("     ")


            import random


            essais = 0


            Juste_Prix = random.randint(1, max)


            while True:
                

                print("trouve le bon nombre.")
                print("        ")

                essais += 1

                try:
                    choix = int(input("->"))
                except ValueError:
                    choix = -1

                if choix < Juste_Prix:
                    
                    print("c'est plus grand !")
                    print("       ")


                elif choix > Juste_Prix:
                    
                    print("C'est plus petit !")
                    print("       ")


                elif choix == Juste_Prix:
                    print("=== BRAVO ===")
                    print("Tu as trouvé le bon nombre !")
                    break
                

                else:
                    
                    print("ERROR")


            lvll = lvl * 1.5


            if lvl == 1:
                score = max * lvll * 40 / essais


            else:
                score = max * lvl * 40 / essais


            print("        ")
            print(f"Tu as fini la partie avec un score de {score}")
            print("     ")


        print("Appuyez sur Entrée pour revenir au menu...")

        while True:
            try:
                return_menu = input("->")
            except ValueError:
                return_menu = ""

            if return_menu == "":
                pass

            else:
                print("=== ERROR ===")

        




            print("     ")
            print("Choisissez le nombre le plus haut en partant de 1 (max 9 999)")
            
            while True:

                try:
                    maxx = int(input("->"))
                except ValueError:
                    maxx = -1


                if maxx >= 10000:
                    
                    print("     ")
                    print("=== ERROR ===")
                    print("     ")
                

                elif maxx <= 9999:

                    break


                else:

                    print("     ")
                    print("=== ERROR ===")
                    print("     ")


            print("     ")
            print("Nombre de joueur :")

            while True:

                try:
                    nbr = int(input("->"))
                except ValueError:
                    nbr = -1

                if nbr <= 19:
                    break
                    
                else:
                    print("=== ERROR ===")
                
            players_choices = {}


            import random


            mystere = random.randint(1, maxx)
                
                
                
            for player in range(nbr):

                try:
                    players_choices[player] = int(input(f"joueur {player + 1}, choisissez votre nombre ->"))
                except ValueError:
                    print("=== ERROR ===")


            ecarts = {}

            for joueur, choix in players_choices.items():
                ecarts[joueur] = abs(choix - mystere)


            joueur_plus_proche = min(ecarts, key=ecarts.get)
            valeur_plus_proche = players_choices[joueur_plus_proche]

            print("     ")
            print(f"Le nombre mystère était {mystere} !")
            print(f"Le joueur le plus proche est : Joueur {joueur_plus_proche + 1} ")
            print(f"Il avait choisi {valeur_plus_proche}, avec un écart de {ecarts[joueur_plus_proche]} par rapport au nombre mystère.")