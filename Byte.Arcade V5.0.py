# =============================================================

# INFORMATION A L'UTILISATEUR :
# pour pouvoir profiter de ce jeu, vous devez
# installer python 3 sur votre ordinateur, ensuite
# rennommez ce fichier comme bon vous semble en
# prenant garde a utiliser l'extention ".py"
# a la fin du nom de votre fichier.
# Ensuite, il vous suffit de double cliquer sur
# le fichier, et de prefiter de l'experience !

# ATTENTION : il est possible que console
# d'execution ne support pas certaine fonctionnalité
# du jeu, surtout si la console était pré-installé.
# si c'est le cas, nous vous recommandons d'istaller
# un executeur python qui support "python3".
# Si ce n'est pas possible, il vous est quand même
# possible de jouer, mais nous ne vous garrantissons
# pas la meuilleur expérience de jeu que nous vous
# avons imaginé.


#  cordialement,
#                                Byte.Games Studios

# ===============================================================

# ---------------------------------------------------------------

# ===============================================================
#                  © 2025 Byte.Games Studios                   
# ===============================================================
# Titre du jeu : Byte.Arcade
# Développé par : Byte.Games Studios
# Auteur principal : Lou.T
# Contact : byte.arcadestudios.dev@gmail.com
# ---------------------------------------------------------------
# Tous droits réservés. Ce jeu et son contenu, incluant mais ne
# se limitant pas au code source, graphismes, sons, textes et
# mécaniques de jeu, sont protégés par les lois européennes et
# internationales relatives à la propriété intellectuelle.
# ---------------------------------------------------------------
# Toute reproduction, distribution, modification ou exploitation
# partielle ou totale de ce logiciel sans l’autorisation écrite
# préalable de Byte.Games Studios est strictement interdite et
# poursuivie conformément au Code de la Propriété Intellectuelle
# et aux directives de l’Union Européenne en vigueur.
# ---------------------------------------------------------------
# Byte.Arcade est une marque déposée de Byte.Games Studios.
# ---------------------------------------------------------------
# Crédits :
# - Développement & conception : Lou.T
# - Test & optimisation : Byte.Games Studios
# - Support technique : Byte.Games Studios
# ---------------------------------------------------------------
# Toute utilisation commerciale non autorisée est interdite.
# Toute violation pourra donner lieu à des poursuites civiles et
# pénales conformément aux lois applicables.
# ---------------------------------------------------------------
# Pour signaler un bug,
# poser une question ou partager vos suggestions,
# merci de contacter l’équipe Byte.Games Studios à
# l’adresse suivante : ###.
# Chaque retour est pris en compte afin de perfectionner
# Byte.Arcade et offrir la meilleure expérience à tous.
# ===============================================================
# Merci d’avoir choisi Byte.Arcade — Un projet Byte.Games Studios
# ===============================================================



# V 5.0

import time
import random
import os

game = True
fnc_cl = True

def cl():
    global game
    global fnc_cl
    try:
        os.system('csl' if os.name == 'nt' else 'clear')
    except Exception:
        while True:
            print("\n" * 15, "=== ATTENTION ===\n\nLa fonction 'rafraîchir la fenetre' est indisponible !\n" \
            "Sans cette fonction, la fenêtre ne pourra pas être rafraîchi.")
            try:
                choix_erreur_generale = int(input("\n\nTapez -1- pour continuer sans ou -2- pour quitter le jeu."))
            except ValueError:
                print("Saisi invalide")
                choix_erreur_generale = -1
                pause(1)
            if choix_erreur_generale not in [1, 2]:
                print("Saisi invalide")
                choix_erreur_generale = -1
                pause(1)
            elif choix_erreur_generale == 1:
                fnc_cl = False
                break
            else:
                game = False
                break

def pause(temps):
    time.sleep(temps)

def chargement_du_jeu():
    global fnc_cl
    if fnc_cl == True:
        cl()
    else:
        pass
    pause(1)
    print("Chargement du jeu", end="", flush=True)
    for p in range(random.randint(3, 5)):
        for o in range(3):
            pause(0.3)
            print(".", end="", flush=True)
            if o >= 2:
                pause(0.3)
                if fnc_cl == True:
                    cl()
                else:
                    pass
                print("Chargement du jeu", end="", flush=True)

def animation():
    global fnc_cl
    if fnc_cl == True:
        cl()
    else:
        pass
    pause(0.5)
    print("Byte.Arcade : Renaissance")
    pause(2)
    if fnc_cl == True:
        cl()
    else:
        pass
    print("by Byte.Games Studios")
    pause(2)
    if fnc_cl == True:
        cl()
    else:
        pass
    print("© 2025 Byte.Arcade Studios")
    pause(2)
    if fnc_cl == True:
        cl()
    else:
        pass
    print("Version du jeu : 5.0")
    pause(2)
    if fnc_cl == True:
        cl()
    else:
        pass

def didactitiel():
    global fnc_cl
    if fnc_cl == True:
        cl()
    else:
        pass
    print("INFORMATION : pour séléctionner une option,\n veuillez rentrer le nombre correspondant,\n puis appuyer sur ENTRÉE pour valider.\n\n")
    pause(0.1)
    print("Selectionnez 1 si vous avez pris en compte l'information.\n")
    while True:
        try:
            menu_ok = int(input("->"))
        except ValueError:
            menu_ok = -1
            print("ATTENTION : pour séléctionner une option,\n veuillez rentrer le nombre correspondant,\n puis appuyer sur ENTRÉE pour valider.\n\n")
            pause(0.1)
        if menu_ok == 1:
            if fnc_cl == True:
                cl()
            else:
                pass
            break
        else:
            print("Veuillez saisir le caractère demandé ")
            time.sleep(2)
            cl()
            print("ATTENTION : pour séléctionner une option,\n veuillez rentrer le nombre correspondant,\n puis appuyer sur ENTRÉE pour valider.\n\n")
            pause(0.1)
            print("Tapez 1 si vous avez pris en compte l'information.\n")

def information():
    if fnc_cl == True:
        cl()
    else:
        pass
    pause(0.1)
    print("=== A VOTRE ATTENTION ===\n\n\n")
    print("Pour signaler un bug,")
    print("poser une question ou partager vos suggestions,")
    pause(0.1)
    print("merci de contacter l’équipe Byte.Games Studios à")
    print("l’adresse suivante : \n\nbyte.arcadestudios.dev@gmail.com\n")
    pause(0.1)
    print("\nChaque retour est pris en compte afin de perfectionner")
    print("Byte.Arcade et offrir la meilleure expérience à tous.")
    pause(0.1)
    print("\nServices disponible entre 17h50 et 21h10, 12h/24 les samedis et dimanches, 7j/7.")
    print("Nos délais de réponses sont inferieurs à 10h.")
    pause(0.1)
    print("\n\nMerci de votre attention,")
    print("\n\n\t\t\tL'équipe Byte.Games Studios.")
    pause(0.1)
    input("\n\n\nPressez ENTRÉE pour continuer.")

def FAQ():
    global fnc_cl
    if fnc_cl == True:
        if fnc_cl == True:
            cl()
        else:
            pass
    else:
        pass
    faq = [
        ("Qu'est-ce que Byte.Arcade ?", 
        "Byte.Arcade est une collection de mini-jeux originaux en texte, conçue pour l'amusement et le suspense."),
        ("Qui a créé Byte.Arcade ?", 
        "Byte.Arcade a été entièrement créé et développé par Lou."),
        ("Quels jeux sont inclus ?", 
        "Pour l'instant : Juste Prix (solo et multijoueur) et Roulette Russe (solo). D'autres jeux viendront dans les futures mises à jour."),
        ("Comment lancer un jeu ?", 
        "Choisissez le jeu depuis le menu principal en entrant le numéro correspondant."),
        ("Peut-on jouer à plusieurs ?", 
        "Oui, certains jeux ont des modes multijoueur, comme le Juste Prix et bientôt la Roulette Russe."),
        ("Peut-on sauvegarder ses scores ?", 
        "Pour le moment, les scores ne sont pas sauvegardés automatiquement, mais ils s'affichent à la fin de chaque partie."),
        ("Comment revenir au menu principal ?", 
        "Après chaque partie, le programme propose de retourner au menu ou de rejouer."),
        ("Comment signaler un bug ?", 
        "Envoyez un email à contact@loudev.com avec une description du problème."),
        ("Byte.Arcade fonctionne sur quel système ?", 
        "Byte.Arcade fonctionne sur tout système où Python est installé (Windows, Mac, Linux)."),
        ("Quels modules Python sont nécessaires ?", 
        "Modules standard : random, time. Pas besoin d'installations supplémentaires pour la version textuelle."),
        ("Puis-je modifier les jeux ?", 
        "Oui, le code est libre pour modification personnelle. Merci de ne pas redistribuer sans autorisation."),
        ("Pourquoi certains jeux sont en solo ?", 
        "Pour simplifier le développement et tester la logique avant d'ajouter le multijoueur."),
        ("Peut-on tricher ?", 
        "Le jeu est basé sur des nombres aléatoires, donc aucune méthode simple de triche intégrée."),
        ("Byte.Arcade sera-t-il mis à jour ?", 
        "Oui, de nouvelles fonctionnalités, jeux et améliorations sont prévues dans les futures versions."),
        ("Est-ce qu'il y a des effets sonores ?", 
        "Pour la version textuelle, non. Les sons seront ajoutés dans une future version graphique."),
        ("Peut-on jouer sans clavier ?", 
        "Non, la version textuelle nécessite le clavier pour entrer les commandes."),
        ("Comment fonctionne la Roulette Russe ?", 
        "Le barillet contient une seule balle. Chaque joueur tire à tour de rôle jusqu'à ce qu'une balle sorte."),
        ("Comment sont générés les nombres dans le Juste Prix ?", 
        "Les nombres sont générés aléatoirement avec la fonction random.randint() de Python."),
        ("Est-ce que Byte.Arcade consomme beaucoup de ressources ?", 
        "Non, la version textuelle est très légère et fonctionne sur n'importe quel ordinateur avec Python."),
        ("Puis-je proposer mes idées de jeu ?", 
        "Oui ! Envoyez vos suggestions à contact@loudev.com et elles pourront être intégrées dans les futures versions."),
    ]

    while True:
        if fnc_cl == True:
            cl()
        else:
            pass
        print("\n========== BYTE.ARCADE FAQ ==========")
        for i, (q, _) in enumerate(faq, 1):
            print(f"{i}. {q}")
        print("=====================================")
        print("\n-0- pour revenir au menu principal.\n")

        try:
            choix = int(input("Entrez le numéro de la question pour voir la réponse : "))
            if choix == 0:
                break
            elif 1 <= choix <= len(faq):
                if fnc_cl == True:
                    cl()
                else:
                    pass
                print(f"\nQ: {faq[choix-1][0]}")
                print(f"R: {faq[choix-1][1]}")
                input("\nPressez ENTRÉE lorsque vous avez terminé.")
            else:
                print("\nNuméro invalide, réessayez.")
                pause(1)
        except ValueError:
            print("\nVeuillez entrer un numéro valide.")
            pause(1)

def copyright():
    if fnc_cl == True:
        cl()
    else:
        pass
    pause(0.5)
    print("===============================================================")
    print("                  © 2025 Byte.Games Studios                   ")
    print("===============================================================")
    pause(0.2)
    print("Titre du jeu : Byte.Arcade")
    print("Développé par : Byte.Games Studios")
    print("Auteur principal : Lou.T")
    print("Contact : byte.arcadestudios.dev@gmail.com")
    pause(0.1)
    print("---------------------------------------------------------------")
    pause(0.1)
    print("Tous droits réservés. Ce jeu et son contenu, incluant mais ne")
    print("se limitant pas au code source, graphismes, sons, textes et")
    print("mécaniques de jeu, sont protégés par les lois européennes et")
    print("internationales relatives à la propriété intellectuelle.")
    pause(0.1)
    print("---------------------------------------------------------------")
    pause(0.1)
    print("Toute reproduction, distribution, modification ou exploitation")
    print("partielle ou totale de ce logiciel sans l’autorisation écrite")
    print("préalable de Byte.Games Studios est strictement interdite et")
    print("poursuivie conformément au Code de la Propriété Intellectuelle")
    print("et aux directives de l’Union Européenne en vigueur.")
    pause(0.1)
    print("---------------------------------------------------------------")
    pause(0.1)
    print("Byte.Arcade est une marque déposée de Byte.Games Studios.")
    pause(0.1)
    print("---------------------------------------------------------------")
    pause(0.1)
    print("Crédits :")
    print("- Développement & conception : Lou.T")
    print("- Test & optimisation : Byte.Games Studios")
    print("- Support technique : Byte.Games Studios")
    pause(0.1)
    print("---------------------------------------------------------------")
    pause(0.1)
    print("Toute utilisation commerciale non autorisée est interdite.")
    print("Toute violation pourra donner lieu à des poursuites civiles et")
    print("pénales conformément aux lois applicables.")
    pause(0.1)
    print("---------------------------------------------------------------")
    pause(0.1)
    print("Pour signaler un bug,")
    print("poser une question ou partager vos suggestions,")
    print("merci de contacter l’équipe Byte.Games Studios à")
    print("l’adresse suivante : ###.")
    pause(0.1)
    print("Chaque retour est pris en compte afin de perfectionner")
    print("Byte.Arcade et offrir la meilleure expérience à tous.")
    pause(0.1)
    print("===============================================================")
    print("Merci d’avoir choisi Byte.Arcade — Un projet Byte.Games Studios")
    print("===============================================================")
    pause(0.1)
    input("\nPressez ENTRÉE pour revenir au menu.")

def Juste_Prix_original_regle():
        print("========== RÈGLES DU JUSTE PRIX ORIGINAL ==========")
        pause(0.1)
        print("""
Bienvenue dans le Juste Prix Original !

1. Le jeu choisit un nombre mystère fixe selon le niveau choisi.
2. Vous devez deviner ce nombre.
3. Après chaque essai, un indice vous sera donné :
   - "Plus GRAND" si le nombre mystère est plus élevé,
   - "Plus PETIT" si le nombre mystère est plus bas.
4. Le score est calculé selon le nombre d'essais.
5. Si vous saisissez une valeur non numérique, vous devrez ressaisir un nombre valide.
6. Après chaque partie, vous pouvez rejouer ou retourner au menu principal.

Bonne chance !
""")
        pause(0.1)
        input("Appuyez sur ENTRÉE pour continuer...")

def juste_prix_original():
    global fnc_cl
    if fnc_cl == True:
            cl()
    else:
        pass
    Juste_Prix_original_regle()
    if fnc_cl == True:
            cl()
    else:
        pass

    Juste_Prix_original_end = False

    while Juste_Prix_original_end == False:
        while True:
            if fnc_cl == True:
                cl()
            else:
                pass
            print("Niveau 1 (NOUVEAU) = 1 - 10")
            print("Niveau 2 (NOUVEAU) = 1 - 20")
            print("Niveau 3 = 1 - 50")
            print("Niveau 4 = 1 - 100")
            print("Niveau 5 = 1 - 150")
            print("Niveau 6 = 1 - 200")
            print("Niveau 7 (NOUVEAU) = 1 - 250")
            print("Niveau 8 = 1 - 300")
            print("Niveau 9 (NOUVEAU) = 1 - 500")

            try:
                Juste_Prix_original_choix  = int(input("->"))
            except ValueError:
                print("Veuillez saisir uniquement le nombre correspondant au niveau désiré.")
                time.sleep(2.5)
            if Juste_Prix_original_choix == 1:
                Juste_Prix_original_max = 10
                break
            elif Juste_Prix_original_choix == 2:
                Juste_Prix_original_max = 20
                break
            elif Juste_Prix_original_choix == 3:
                Juste_Prix_original_max = 50
                break
            elif Juste_Prix_original_choix == 4:
                Juste_Prix_original_max = 100
                break
            elif Juste_Prix_original_choix == 5:
                Juste_Prix_original_max = 150
                break
            elif Juste_Prix_original_choix == 6:
                Juste_Prix_original_max = 200
                break
            elif Juste_Prix_original_choix == 7:
                Juste_Prix_original_max = 250
                break
            elif Juste_Prix_original_choix == 8:
                Juste_Prix_original_max = 300
                break
            elif Juste_Prix_original_choix == 9:
                Juste_Prix_original_max = 500
                break
            

        nombre_mystere = random.randint(1, Juste_Prix_original_max)
        print("La partie va commencer", end="", flush=True)
        for t in range(3):
            pause(1)
            print(".", end="", flush=True)
            if t >= 2:
                pause(1)
        Juste_Prix_original_tour = 0
        while True:
            Juste_Prix_original_tour += 1
            if fnc_cl == True:
                cl()
            else:
                pass
            print("Votre pari", end="", flush=True)
            try:
                pari = int(input("->"))
            except ValueError:
                print(f"Veuillez saisir un nombre entre 1 et {Juste_Prix_original_max}.")
                continue
            if pari > nombre_mystere:
                print("Le nombre mystère est plus -PETIT-")
                time.sleep(1.5)
            elif pari < nombre_mystere:
                print("Le nombre mystère est plus -GRAND-")
                time.sleep(1.5)
            else:
                print("-BRAVO-, tu as trouvé le nombre mystère !")
                time.sleep(1)
                break

        score = Juste_Prix_original_choix * Juste_Prix_original_max / Juste_Prix_original_tour
        if fnc_cl == True:
            cl()
        else:
            pass
        print(f"Tu as fini la partie avec un score de {score} points !")
        time.sleep(1.5)
        print("\nTapez -1- pour rejouer ou -2- pour retourner au menu.")
        while True:
            try:
                retour_menu = int(input("\n->"))
            except ValueError:
                print("Saisi invalide, veuillez reessayer en tapant 1 ou 2")
                pause(2)
                if fnc_cl == True:
                    cl()
                else:
                    pass
                continue
            if retour_menu not in [1, 2]:
                print("Saisi invalide, veuillez reessayer en tapant 1 ou 2")
                pause(2)
                cl()
                continue
            elif retour_menu == 1:
                pass
            else:
                break
        if retour_menu == 2:
            break

def Juste_Prix_remake_regle():
        print("========== RÈGLES DU JUSTE PRIX REMAKE ==========")
        pause(0.1)
        print("""
Bienvenue dans le Juste Prix Remake !

1. Choisissez votre niveau de difficulté. Le nombre choisi sera le maximum que l'ordinateur pourra tirer au sort.
2. Devinez le nombre mystère choisi par l'ordinateur.
3. Après chaque essai, vous recevrez un indice : 
   - "Plus GRAND" si le nombre mystère est plus élevé,
   - "Plus PETIT" si le nombre mystère est plus bas.
4. Votre score dépendra de la rapidité avec laquelle vous trouvez le nombre.
5. Soyez stratégique : moins vous faites d'essais, meilleur sera votre score.
6. Si vous saisissez une valeur non numérique, vous devrez ressaisir un nombre valide.
7. Après chaque partie, vous pouvez rejouer ou retourner au menu principal.

Bonne chance ! Essayez de battre votre record !
""")
        pause(0.1)
        input("Appuyez sur ENTRÉE pour continuer...")

def Juste_Prix_remake():
    global fnc_cl
    if fnc_cl == True:
        cl()
    else:
        pass
    Juste_Prix_remake_regle()
    if fnc_cl == True:
        cl()
    else:
        pass

    Juste_Prix_remake_end = False

    while Juste_Prix_remake_end == False:

        def Juste_Prix_remake_niveau():
            while True:
                if fnc_cl == True:
                    cl()
                else:
                    pass
                print("Choisissez le niveau de difficulté,\nle nombre inséré correspondera\nau nombre maximum que l'ordinateur pourra tirer au sort.\nATTENTION, nombre max : 99 999")
                try:
                    choix = int(input("\n->"))
                except ValueError:
                    print("Veuillez saisir uniquement le nombre de votre choix.")
                    continue
                if 0 < choix < 99999:
                    return choix
                else:
                    print("Erreur : veuillez saisir un nombre entre 1 et 99 999.")

        Juste_Prix_remake_choix_niveau = Juste_Prix_remake_niveau()
        Juste_Prix_remake_max = Juste_Prix_remake_choix_niveau
        Juste_Prix_remake_nombre = random.randint(1, Juste_Prix_remake_max)

        print("La partie va commencer", end="", flush=True)
        for t in range(2):
            time.sleep(1)
            print(".", end="", flush=True)
            if t == 1:
                time.sleep(1)

        Juste_Prix_remake_tour = 0

        while True:
            Juste_Prix_remake_tour += 1
            if fnc_cl == True:
                cl()
            else:
                pass
            print("Votre pari", end="", flush=True)
            try:
                Juste_Prix_remake_paris = int(input("->"))
            except ValueError:
                print(f"Veuillez saisir un nombre entre 1 et {Juste_Prix_remake_choix_niveau}.")
                continue
            if Juste_Prix_remake_paris > Juste_Prix_remake_nombre:
                print("Le nombre mystère est plus -PETIT-")
                time.sleep(1.5)
            elif Juste_Prix_remake_paris < Juste_Prix_remake_nombre:
                print("Le nombre mystère est plus -GRAND-")
                time.sleep(1.5)
            else:
                print("-BRAVO-, tu as trouvé le nombre mystère !")
                time.sleep(1)
                break

        Juste_Prix_remake_score = Juste_Prix_remake_choix_niveau * Juste_Prix_remake_max / Juste_Prix_remake_tour
        if fnc_cl == True:
            cl()
        else:
            pass
        print(f"Tu as fini la partie avec un score de {Juste_Prix_remake_score} points !")
        time.sleep(1.5)
        print("\nTapez -1- pour rejouer ou -2- pour retourner au menu.")
        while True:
            try:
                retour_menu = int(input("\n->"))
            except ValueError:
                print("Saisi invalide, veuillez reessayer en tapant 1 ou 2")
                pause(2)
                if fnc_cl == True:
                    cl()
                else:
                    pass
                continue
            if retour_menu not in [1, 2]:
                print("Saisi invalide, veuillez reessayer en tapant 1 ou 2")
                pause(2)
                if fnc_cl == True:
                    cl()
                else:
                    pass
                continue
            elif retour_menu == 1:
                pass
            else:
                break
        if retour_menu == 2:
            break
        else:
            pass

def Juste_Prix_multijoueur_regle():
        print("========== RÈGLES DU JUSTE PRIX MULTIJOUEUR ==========")
        pause(0.1)
        print("""
Bienvenue dans le Juste Prix Multijoueur !

1. Chaque joueur choisit son pseudo.
2. Un nombre mystère est choisi par l'ordinateur selon le niveau défini.
3. Les joueurs jouent chacun leur tour pour deviner le nombre mystère.
4. Après chaque essai, un indice est donné :
- "Plus GRAND" si le nombre mystère est plus élevé,
- "Plus PETIT" si le nombre mystère est plus bas.
5. Le joueur qui trouve le nombre mystère marque un score.
6. Le jeu continue sur plusieurs tours ou jusqu'à ce que les joueurs décident d'arrêter.
7. Après chaque partie, possibilité de rejouer ou de retourner au menu.

Bonne chance à tous !
""")
        pause(0.1)
        input("Appuyez sur ENTRÉE pour continuer...")

def Juste_Prix_multijoueur():
    global fnc_cl
    if fnc_cl == True:
        cl()
    else:
        pass
    Juste_Prix_multijoueur_regle()
    if fnc_cl == True:
        cl()
    else:
        pass
    Juste_Prix_multijoueur_end = False
    while Juste_Prix_multijoueur_end == False:
        if fnc_cl == True:
            cl()
        else:
            pass
        joueur1 = input("Pseudo du joueur 1 -> ")
        joueur2 = input("Pseudo du joueur 2 -> ")
        while True:
            if fnc_cl == True:
                cl()
            else:
                pass
            print("Choisissez le niveau (nombre maximum):")
            try:
                niveau = int(input("->"))
            except ValueError:
                print("Veuillez entrer un nombre valide.")
                continue
            if 0 < niveau < 99999:
                break
            else:
                print("Erreur : nombre entre 1 et 99 999 uniquement.")
        nombre_mystere = random.randint(1, niveau)
        print("La partie va commencer", end="", flush=True)
        for t in range(2):
            time.sleep(1)
            print(".", end="", flush=True)
            if t == 1:
                time.sleep(1)
        tour = 0
        joueur_actuel = 1
        while True:
            tour += 1
            if fnc_cl == True:
                cl()
            else:
                pass
            pseudo = joueur1 if joueur_actuel == 1 else joueur2
            print(f"C'est au tour de {pseudo}", end="", flush=True)
            try:
                pari = int(input("\nVotre pari -> "))
            except ValueError:
                print(f"Veuillez saisir un nombre entre 1 et {niveau}.")
                continue
            if pari > nombre_mystere:
                print("Le nombre mystère est plus -PETIT-")
            elif pari < nombre_mystere:
                print("Le nombre mystère est plus -GRAND-")
            else:
                print(f"-BRAVO-, {pseudo} a trouvé le nombre mystère !")
                break
            joueur_actuel = 2 if joueur_actuel == 1 else 1
            time.sleep(1.5)
        score = niveau * niveau / tour
        cl()
        print(f"{pseudo} a terminé la partie avec un score de {score} points !")
        time.sleep(2)
        print("\nTapez -1- pour rejouer ou -2- pour retourner au menu.")
        while True:
            try:
                retour_menu = int(input("\n->"))
            except ValueError:
                print("Saisi invalide, veuillez reessayer en tapant 1 ou 2")
                pause(2)
                if fnc_cl == True:
                    cl()
                else:
                    pass
                continue
            if retour_menu not in [1, 2]:
                print("Saisi invalide, veuillez reessayer en tapant 1 ou 2")
                pause(2)
                if fnc_cl == True:
                    cl()
                else:
                    pass
                continue
            elif retour_menu == 1:
                pass
            else:
                break
        if retour_menu == 2:
            break

def Roulette_Russe_regle():
        global fnc_cl
        if fnc_cl == True:
            cl()
        else:
            pass
        print("Un revolver, uits chambres, vous, un robot, une balle, un seul survivant,")
        pause(0.1)
        print("Tour à tour, tirez vous une chambre de revolver dessus,")
        pause(0.1)
        print("jusqu'a ce que l'unique balle des huits chambres termine l'un d'entre vous.")
        input("\nPressez ENTRÉE pour continuer.")
        if fnc_cl == True:
            cl()
        else:
            pass

def Roulette_Russe():
    global fnc_cl
    Roulette_Russe_regle()
    Roulette_Russe_end = False

    while Roulette_Russe_end == False:
        print("Le robot insère la balle dans le barillet", end="", flush=True)
        for z in range(3):
            time.sleep(1)
            print(".", end="", flush=True)
            if z >= 2:
                time.sleep(1)
        if fnc_cl == True:
            cl()
        else:
            pass
        print("Le robot a mis la balle...")
        time.sleep(2)
        print("À vous maintenant de tourner le barillet...")
        time.sleep(2.5)
        if fnc_cl == True:
            cl()
        else:
            pass
        print("Pour tourner le barillet, pressez ENTRÉE...")
        input()
        Roulette_Russe_barillet = [False, False, False, False, False, True]
        random.shuffle(Roulette_Russe_barillet)
        if fnc_cl == True:
            cl()
        else:
            pass
        print("Vous avez mélangé le barillet, puis vous tendez le pistolet au robot pour qu'il puisse commencer", end="", flush=True)
        for t in range(3):
                pause(0.7)
                print(".", end="", flush=True)
                if t >= 2:
                    pause(0.7)
                    cl()
        time.sleep(1)
        if fnc_cl == True:
            cl()
        else:
            pass
        Roulette_Russe_scripts_robot_tour = [
        "Le robot place le canon du pistolet sur sa tempe",
        "Le robot dépose la pointe du canon entre ses deux yeux", 
        "Le robot vise le fond de sa gorge", 
        "Le robot vise un point, derrière lequel se trouve son cœur"
        ]
        Roulette_Russe_scripts_robot_mort = [
            "*BANG!*, vous ouvrez les yeux, vous regardez le robot, sanglant, la tête qui pend sur le côté...",
            "*BANG!*, vos yeux se dirigent vers le robot... Rouge... C'est le seul mot qui vous vient à la tête...",
            "*BANG!*, vous vous levez, vous vous retournez et courez vers la porte de sortie, vous jetez un dernier regard sur le robot, inerte, sanglant..."
        ]
        Roulette_Russe_scripts_robot_survie = [
            "*CLIC!*, le robot s'en sort pour cette fois... À vous maintenant...", 
            "*CLIC!*, dommage, le robot est encore debout, à votre tour, bonne chance ! Ou pas...", 
            "*CLIC!*, c'est le seul petit bruit que produit le pistolet, le robot reste... À vous maintenant de connaître votre sort..."
        ]
        Roulette_Russe_script_humain_survie = [
            "*CLIC!*, vous n'êtes pas passé loin d'un destin tragique... Au tour du robot maintenant !", 
            "*CLIC!*, ce bruit vous rassure bien plus que n’importe quoi... Au tour du robot !", 
            "*CLIC!*, vous n'avez jamais eu autant goût à la vie... Au tour du robot !"
        ]
        Roulette_Russe_humain = True
        while True:
            print("--- TOUR DU ROBOT ---")
            print("\n\n", random.choice(Roulette_Russe_scripts_robot_tour), end="", flush=True)
            for t in range(3):
                pause(0.7)
                print(".", end="", flush=True)
                if t >= 2:
                    pause(0.7)
                    if fnc_cl == True:
                        cl()
                    else:
                        pass
            time.sleep(random.randint(1,3))
            print("\nIl presse de plus en plus la détente et", end="", flush=True)
            for t in range(3):
                pause(0.7)
                print(".", end="", flush=True)
                if t >= 2:
                    pause(0.7)
                    if fnc_cl == True:
                        cl()
                    else:
                        pass
            Roulette_Russe_tir = Roulette_Russe_barillet.pop()
            time.sleep(random.randint(1, 4))
            if Roulette_Russe_tir == True:
                if fnc_cl == True:
                    cl()
                else:
                    pass
                print("--- TOUR DU ROBOT ---")
                time.sleep(random.randint(2, 5))
                print("\n\n", random.choice(Roulette_Russe_scripts_robot_mort))
                time.sleep(2)
                break
            else:
                cl()
                print(random.choice(Roulette_Russe_scripts_robot_survie))
                print(f"\nIl reste {len(Roulette_Russe_barillet)} chambres à tirer...")
                time.sleep(5)
                if fnc_cl == True:
                    cl()
                else:
                    pass
            print("--- VOTRE TOUR ---")
            print("\n\nPressez ENTRÉE pour tirer...")
            input()
            Roulette_Russe_tir = Roulette_Russe_barillet.pop()
            if Roulette_Russe_tir == True:
                if fnc_cl == True:
                    cl()
                else:
                    pass
                print("--- VOTRE TOUR ---")
                time.sleep(0.1)
                print("\n\n*BANG!*, vous êtes MORT...")
                time.sleep(2)
                Roulette_Russe_humain = False
                break
            else:
                if fnc_cl == True:
                    cl()
                else:
                    pass
                print("--- VOTRE TOUR ---")
                time.sleep(0.2)
                print(random.choice(Roulette_Russe_script_humain_survie))
                print(f"\nIl reste {len(Roulette_Russe_barillet)} chambres à tirer")
                time.sleep(5)
                if fnc_cl == True:
                    cl()
                else:
                    pass
                print("--- VOTRE TOUR ---")
                print("Pressez ENTRÉE pour donner le pistolet au robot.")
                input()
                if fnc_cl == True:
                    cl()
                else:
                    pass
        if Roulette_Russe_humain == True:
            if fnc_cl == True:
                cl()
            else:
                pass
            print("Bravo ! Vous avez survécu à cette partie !")
            print("\n\nTapez -1- pour rejouer ou -2- pour retourner au menu.")
        else:
            if fnc_cl == True:
                cl()
            else:
                pass
            print("Tapez -1- pour rejouer ou -2- pour retourner au menu.")

def roulette_russe_multijoueur_regle():
    print("6 joueurs max, un revolver, 6 chambres, 1 balle, un mort...")
    pause(0.1)
    print("Surviverz vous ?")
    input("\n\nPressez ENTRÉE pour continuer.")

def roulette_russe_multijoueur():
    global fnc_cl
    joueurs_r_r = []
    if fnc_cl == True:
        cl()
    else:
        pass
    roulette_russe_multijoueur_regle()
    while True:
        if fnc_cl == True:
            cl()
        else:
            pass
        print("Combien de joueurs êtes vous ?")
        try:
            nbr_de_joueur = int(input("\n->"))
        except ValueError:
            print("Saisi invalide, veuillez saisir un nombre.")
            pause(2)
            if fnc_cl == True:
                cl()
            else:
                pass
            continue
        if nbr_de_joueur > 1:
            break
        else:
            print("Vous devez être plus de 1 joueur a participer.")
            pause(2)
            if fnc_cl == True:
                cl()
            else:
                pass
            continue
    for e in range(nbr_de_joueur):
        joueurs_r_r.append(input(f"Joueur {e + 1}, choisissez votre pseudo : "))
    while len(joueurs_r_r) > 1:
        for joueur in len(joueurs_r_r):
            if fnc_cl == True:
                cl()
            else:
                pass
            print(f"Joueur {joueurs_r_r[joueur]}, a vous de connaître votre destint.")
            print("Pour tirer, pressez ENTRÉE")
            input()

def affichage_menu_aide():
    global fnc_cl
    if fnc_cl == True:
        cl()
    else:
        pass
    pause(0.3)
    print("=========================================")
    print("======= BYTE.ARCADE : RENAISSANCE =======")
    print("=========================================")
    pause(0.2)
    print("\n\n=== MENU ===")
    pause(0.1)
    print("\n\nFAQ : -1-")
    pause(0.1)
    print("\nCopyright : -2-")
    pause(0.1)
    print("\nMenu erreurs (beintôt disponible) : -3-")
    pause(0.1)
    print("\nRetour : -0-")

def menu_aide():
    global fnc_cl
    while True:
        affichage_menu_aide()
        try:
            choix_menu_aide = int(input("\n->"))
        except ValueError:
            print("Saisi invalide, veuillez reessayer en tapant 1, 2, 3 ou 0")
            pause(2)
            if fnc_cl == True:
                cl()
            else:
                pass
            continue
        if choix_menu_aide not in [1, 2, 3, 0]:
            print("Saisi invalide, veuillez reessayer en tapant 1, 2, 3 ou 0")
            pause(2)
            if fnc_cl == True:
                cl()
            else:
                pass
            continue
        elif choix_menu_aide == 1:
            FAQ()
        elif choix_menu_aide == 2:
            copyright()
        elif choix_menu_aide == 3:
            pass
        else:
            break

def affichage_menu_jeu():
    if fnc_cl == True:
        cl()
    else:
        pass
    pause(0.3)
    print("=========================================")
    print("======= BYTE.ARCADE : RENAISSANCE =======")
    print("=========================================")
    pause(0.2)
    print("\n\n=== MENU JEUX ===")
    pause(0.2)
    print("\n\nJuste Prix original : -1-\t\tRoulette Russe : -4-")
    pause(0.1)
    print("\nJuste Prix remake : -2-\t\t\tRoulette Russe multijoueur : -5-")
    pause(0.1)
    print("\nJuste Prix multijoueur : -3-")
    pause(0.1)
    print("\nRetour : -0-")

def menu_jeu():
    while True:
        if fnc_cl == True:
            cl()
        else:
            pass
        affichage_menu_jeu()
        try:
            choix_menu_jeu = int(input("\n->"))
        except ValueError:
            print("Saisi invalide, veuillez reessayer en tapant 1, 2, 3, 4 ou 0")
            pause(2)
            if fnc_cl == True:
                cl()
            else:
                pass
            continue
        if choix_menu_jeu not in [1, 2, 3, 4, 5, 0]:
            print("Saisi invalide, veuillez reessayer en tapant 1, 2, 3, 4, 5 ou 0")
            pause(2)
            if fnc_cl == True:
                cl()
            else:
                pass
            continue
        elif choix_menu_jeu == 1:
            juste_prix_original()
        elif choix_menu_jeu == 2:
            Juste_Prix_remake()
        elif choix_menu_jeu == 3:
            Juste_Prix_multijoueur()
        elif choix_menu_jeu == 4:
            Roulette_Russe()
        elif choix_menu_jeu == 5:
            roulette_russe_multijoueur()
        else:
            break

def affichage_menu_principal():
    if fnc_cl == True:
        cl()
    else:
        pass
    pause(0.3)
    print("=========================================")
    print("======= BYTE.ARCADE : RENAISSANCE =======")
    print("=========================================")
    pause(0.2)
    print("\n\n=== MENU ===")
    pause(0.1)
    print("\n\nAcceder au jeu : -1-")
    pause(0.1)
    print("\nAide : -2-")
    pause(0.1)
    print("\nQuitter : -0-")

def menu_principal():
    while True:
        if fnc_cl == True:
            cl()
        else:
            pass
        affichage_menu_principal()
        try:
            choix_menu_principal = int(input("\n->"))
        except ValueError:
            print("Saisi invalide, veuillez reessayer en tapant 1, 2, ou 0")
            pause(2)
            if fnc_cl == True:
                cl()
            else:
                pass
            continue
        if choix_menu_principal not in [1, 2, 0]:
            print("Saisi invalide, veuillez reessayer en tapant 1, 2, ou 0")
            pause(2)
            if fnc_cl == True:
                cl()
            else:
                pass
            continue
        elif choix_menu_principal == 1:
            menu_jeu()
        elif choix_menu_principal == 2:
            menu_aide()
        else:
            break

def jeu():
    chargement_du_jeu()
    didactitiel()
    information()
    menu_principal()

jeu()