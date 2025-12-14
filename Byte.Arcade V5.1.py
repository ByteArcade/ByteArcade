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



# V 5.1

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
            print("\n" * 15, "\t\t\033[41;97m=== ATTENTION ===\033[0;91m\n\nLa fonction 'rafraîchir la fenetre' est indisponible !\n" \
            "Sans cette fonction, la fenêtre ne pourra pas être rafraîchi.")
            try:
                choix_erreur_generale = int(input("\n\nTapez -1- pour continuer sans ou -2- pour quitter le jeu.\033[0m"))
            except ValueError:
                print("\033[41mSaisi invalide\033[0m")
                choix_erreur_generale = -1
                pause(1)
                continue
            if choix_erreur_generale not in [1, 2]:
                print("\033[41mSaisi invalide\033[0m")
                choix_erreur_generale = -1
                pause(1)
                continue
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
    print("\033[0mChargement du jeu", end="", flush=True)
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
    print("\033[0mByte.Arcade : Renaissance")
    pause(2)
    if fnc_cl == True:
        cl()
    else:
        pass
    print("\033[0mby Byte.Games Studios")
    pause(2)
    if fnc_cl == True:
        cl()
    else:
        pass
    print("\033[0m© 2025 Byte.Arcade Studios")
    pause(2)
    if fnc_cl == True:
        cl()
    else:
        pass
    print("\033[0mVersion du jeu : 5.0")
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
    print("\t\t\033[41m=== INFORMATION ===\033[0m\n\n\nPour séléctionner une option, veuillez rentrer le nombre correspondant,\npuis appuyer sur \033[32mENTRÉE\033[0m pour valider.\n\n")
    pause(0.1)
    print("\033[33mSelectionnez \033[32m-1-\033[0m si vous avez pris en compte l'information.\033[0m\n")
    while True:
        try:
            menu_ok = int(input("->"))
        except ValueError:
            menu_ok = -1
            print("\033[41mATTENTION\033[91m : pour séléctionner une option,\n veuillez rentrer le nombre correspondant,\n puis appuyer sur \033[32mENTRÉE\033[91m pour valider.\n\n")
            pause(0.1)
        if menu_ok == 1:
            if fnc_cl == True:
                cl()
            else:
                pass
            break
        else:
            print("\033[41mVeuillez saisir le caractère demandé.\033[0m")
            time.sleep(2)
            cl()
            print("\033[41mATTENTION\033[91m : pour séléctionner une option,\n veuillez rentrer le nombre correspondant,\n puis appuyer sur \033[32mENTRÉE\033[91m pour valider.\033[0m\n\n")
            pause(0.1)
            print("\033[33mTapez \033[32m-1-\033[33m si vous avez pris en compte l'information.\033[0m\n")

def information():
    if fnc_cl == True:
        cl()
    else:
        pass
    pause(0.1)
    print("\033[45;97m=== A VOTRE ATTENTION ===\033[0m\n\n\n")
    print("\033[95mPour signaler un bug,")
    print("poser une question ou partager vos suggestions,")
    pause(0.1)
    print("merci de contacter l’équipe Byte.Games Studios à")
    print("l’adresse suivante : \n\n\033[34mbyte.arcadestudios.dev@gmail.com\033[95m\n")
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
    input("\n\n\n\033[33mPressez \033[32m-ENTRÉE-\033[33m pour continuer.\033[0m")

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
        print("\n\033[91m========== BYTE.ARCADE FAQ ==========\033[0m\n\n")
        for i, (q, _) in enumerate(faq, 1):
            print(f"\033[35m{i}.\033[34m {q}")
        print("\n\n\033[91m=====================================\033[0m")
        print("\n\033[32m-0-\033[33m pour revenir au menu principal.\033[0m\n")

        try:
            choix = int(input("\033[33mEntrez le numéro de la question pour voir la réponse :\033[0m "))
            if choix == 0:
                break
            elif 1 <= choix <= len(faq):
                if fnc_cl == True:
                    cl()
                else:
                    pass
                print(f"\nQ: {faq[choix-1][0]}")
                print(f"R: {faq[choix-1][1]}")
                input("\nPressez \033[32mENTRÉE\033[33m lorsque vous avez terminé.")
            else:
                print("\n\033[41mNuméro invalide, réessayez.\033[0m")
                pause(1.2)
        except ValueError:
            print("\n\033[41mVeuillez entrer un numéro valide.\033[0m")
            pause(1.2)

def copyright():
    if fnc_cl == True:
        cl()
    else:
        pass
    pause(0.02)
    print("\033[95m===============================================================\033[96m")
    pause(0.02)
    print("                  © 2025 Byte.Games Studios                   ")
    pause(0.02)
    print("\033[95m===============================================================")
    pause(0.02)
    print("Titre du jeu : Byte.Arcade")
    print("Développé par : Byte.Games Studios")
    pause(0.02)
    print("Auteur principal : Lou.T")
    print("Contact :\033[94m byte.arcadestudios.dev@gmail.com\033[95m")
    pause(0.02)
    print("---------------------------------------------------------------")
    pause(0.02)
    print("Tous droits réservés. Ce jeu et son contenu, incluant mais ne")
    print("se limitant pas au code source, graphismes, sons, textes et")
    pause(0.02)
    print("mécaniques de jeu, sont protégés par les lois européennes et")
    print("internationales relatives à la propriété intellectuelle.")
    pause(0.02)
    print("---------------------------------------------------------------")
    pause(0.02)
    print("Toute reproduction, distribution, modification ou exploitation")
    print("partielle ou totale de ce logiciel sans l’autorisation écrite")
    pause(0.02)
    print("préalable de Byte.Games Studios est strictement interdite et")
    pause(0.02)
    print("poursuivie conformément au Code de la Propriété Intellectuelle")
    print("et aux directives de l’Union Européenne en vigueur.")
    pause(0.02)
    print("---------------------------------------------------------------")
    pause(0.02)
    print("\033[95mByte.Arcade est une marque déposée de Byte.Games Studios.")
    pause(0.02)
    print("---------------------------------------------------------------")
    pause(0.02)
    print("Crédits :")
    print("- Développement & conception : Lou.T")
    pause(0.02)
    print("- Test & optimisation : Byte.Games Studios")
    print("- Support technique : Byte.Games Studios")
    pause(0.02)
    print("---------------------------------------------------------------")
    pause(0.02)
    print("\033[95mToute utilisation commerciale non autorisée est interdite.")
    pause(0.02)
    print("Toute violation pourra donner lieu à des poursuites civiles et")
    print("pénales conformément aux lois applicables.")
    pause(0.02)
    print("---------------------------------------------------------------")
    pause(0.02)
    print("Pour signaler un bug,")
    print("poser une question ou partager vos suggestions,")
    pause(0.02)
    print("merci de contacter l’équipe Byte.Games Studios à")
    print("l’adresse suivante :\033[94m byte.arcadestudios.dev@gmail.com")
    pause(0.02)
    print("\033[95mChaque retour est pris en compte afin de perfectionner")
    print("Byte.Arcade et offrir la meilleure expérience à tous.")
    pause(0.02)
    print("===============================================================")
    pause(0.02)
    print("Merci d’avoir choisi Byte.Arcade — Un projet Byte.Games Studios")
    pause(0.02)
    print("===============================================================")
    pause(0.02)
    input("\n\033[93mPressez \033[32m-ENTRÉE-\033[93m pour revenir au menu.")

def Juste_Prix_original_regle():
        print("\033[31m========== RÈGLES DU JUSTE PRIX ORIGINAL ==========\033[35m")
        pause(0.09)
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
        pause(0.09)
        input("\033[33mAppuyez sur \033[32m-ENTRÉE-\033[33m pour continuer...\033[0m")

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
            print("\033[91m=============================")
            pause(0.05)
            print("\n\033[95mNiveau 1 (NOUVEAU) = 1 - 10")
            pause(0.05)
            print("\nNiveau 2 (NOUVEAU) = 1 - 20")
            pause(0.05)
            print("\nNiveau 3 = 1 - 50")
            pause(0.05)
            print("\nNiveau 4 = 1 - 100")
            pause(0.05)
            print("\nNiveau 5 = 1 - 150")
            pause(0.05)
            print("\nNiveau 6 = 1 - 200")
            pause(0.05)
            print("\nNiveau 7 (NOUVEAU) = 1 - 250")
            pause(0.05)
            print("\nNiveau 8 = 1 - 300")
            pause(0.05)
            print("\nNiveau 9 (NOUVEAU) = 1 - 500")
            pause(0.05)
            print("\n\033[91m=============================\033[0m")

            try:
                Juste_Prix_original_choix  = int(input("\n\033[33m->\033[0m"))
            except ValueError:
                print("\n\033[41mVeuillez saisir uniquement le nombre correspondant au niveau désiré.\033[0m")
                time.sleep(1.5)
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
            else:
                print("\n\033[41mVeuillez saisir uniquement le nombre correspondant au niveau désiré.\033[0m")
                time.sleep(1.5)

        nombre_mystere = random.randint(1, Juste_Prix_original_max)
        if fnc_cl == True:
            cl()
        else:
            pass
        print("La partie va commencer", end="", flush=True)
        for t in range(3):
            pause(0.5)
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
            print("\033[93mVotre pari", end="", flush=True)
            try:
                pari = int(input("->\033[0m"))
            except ValueError:
                print(f"Veuillez saisir un nombre entre 1 et {Juste_Prix_original_max}.")
                continue
            if pari > nombre_mystere:
                print("\n\033[35mLe nombre mystère est plus -PETIT-\033[0m")
                time.sleep(1.5)
            elif pari < nombre_mystere:
                print("\n\033[35mLe nombre mystère est plus -GRAND-\033[0m")
                time.sleep(1.5)
            else:
                print("\n\033[91m-BRAVO-, tu as trouvé le nombre mystère !\033[0m")
                time.sleep(1)
                break

        score = Juste_Prix_original_choix * Juste_Prix_original_max / Juste_Prix_original_tour
        if fnc_cl == True:
            cl()
        else:
            pass
        print(f"\033[35mTu as fini la partie avec un score de {int(score)} points !\033[0m")
        time.sleep(1.5)
        print("\n\033[33mTapez \033[32m-1-\033[33m pour rejouer ou \033[32m-2-\033[33m pour retourner au menu.\033[0m")
        while True:
            try:
                retour_menu = int(input("\n\033[33m->\033[0m"))
            except ValueError:
                print("\033[41mSaisi invalide, veuillez reessayer en tapant -1- ou -2-\033[0m")
                pause(2)
                if fnc_cl == True:
                    cl()
                else:
                    pass
                continue
            if retour_menu not in [1, 2]:
                print("\033[41mSaisi invalide, veuillez reessayer en tapant -1- ou -2-\033[0m")
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
        print("\033[91m========== RÈGLES DU JUSTE PRIX REMAKE ==========\033[0m")
        pause(0.1)
        print("""\033[35m
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
        input("\033[33mAppuyez sur \033[32m-ENTRÉE-\033[33m pour continuer.\033[0m")

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
                print("\033[33mChoisissez le niveau de difficulté,\nle nombre inséré correspondera\nau nombre maximum que l'ordinateur pourra tirer au sort.\n\n\033[31mATTENTION, nombre max : 99 999\033[0m")
                try:
                    choix = int(input("\n\033[33m->"))
                except ValueError:
                    print("\033[0;41mVeuillez saisir uniquement le nombre de votre choix.\033[0m")
                    pause(1.5)
                    continue
                if 0 < choix < 99999:
                    return choix
                else:
                    print("\033[0;41mErreur : veuillez saisir un nombre entre 1 et 99 999.\033[0m")
                    pause(1.5)

        Juste_Prix_remake_choix_niveau = Juste_Prix_remake_niveau()
        Juste_Prix_remake_max = Juste_Prix_remake_choix_niveau
        Juste_Prix_remake_nombre = random.randint(1, Juste_Prix_remake_max)
        if fnc_cl == True:
            cl()
        else:
            pass
        print("La partie va commencer", end="", flush=True)
        for t in range(3):
            pause(0.5)
            print(".", end="", flush=True)
            if t == 2:
                pause(0.5)

        Juste_Prix_remake_tour = 0

        while True:
            Juste_Prix_remake_tour += 1
            if fnc_cl == True:
                cl()
            else:
                pass
            print("\033[33mVotre pari\033[0m", end="", flush=True)
            try:
                Juste_Prix_remake_paris = int(input("\033[33m->\033[0m"))
            except ValueError:
                print(f"\033[41mVeuillez saisir un nombre entre 1 et {Juste_Prix_remake_choix_niveau}.\033[0m")
                continue
            if Juste_Prix_remake_paris > Juste_Prix_remake_nombre:
                print("\n\033[35mLe nombre mystère est plus -PETIT-\033[0m")
                time.sleep(1.5)
            elif Juste_Prix_remake_paris < Juste_Prix_remake_nombre:
                print("\n\033[35mLe nombre mystère est plus -GRAND-\033[0m")
                time.sleep(1.5)
            else:
                print("\n\033[31m-BRAVO-, tu as trouvé le nombre mystère !\033[0m")
                time.sleep(1.5)
                break

        Juste_Prix_remake_score = Juste_Prix_remake_choix_niveau * Juste_Prix_remake_max / Juste_Prix_remake_tour
        if fnc_cl == True:
            cl()
        else:
            pass
        print(f"\033[35mTu as fini la partie avec un score de {int(Juste_Prix_remake_score)} points !\033[0m")
        time.sleep(1.5)
        print("\n\033[33mTapez \033[32m-1-\033[33m pour rejouer ou \033[32m-2-\033[33m pour retourner au menu.\033[0m")
        while True:
            try:
                retour_menu = int(input("\n->"))
            except ValueError:
                print("\033[41mSaisi invalide, veuillez reessayer en tapant 1 ou 2\033[0m")
                pause(2)
                if fnc_cl == True:
                    cl()
                else:
                    pass
                continue
            if retour_menu not in [1, 2]:
                print("\033[41mSaisi invalide, veuillez reessayer en tapant 1 ou 2\033[0m")
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
        print("\033[91m========== RÈGLES DU JUSTE PRIX MULTIJOUEUR ==========\033[35m")
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
        input("\033[33mAppuyez sur \033[32m-ENTRÉE-\033[33m pour continuer...\033[0m")

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
        joueur1 = input("\033[33mPseudo du joueur 1 -> ")
        joueur2 = input("Pseudo du joueur 2 -> \033[0m")
        while True:
            if fnc_cl == True:
                cl()
            else:
                pass
            print("\033[33mChoisissez le niveau (nombre le plus haut qui peut-êtres tiré au sort):")
            try:
                niveau = int(input("->\033[0m"))
            except ValueError:
                print("\033[0;41mVeuillez entrer un nombre valide.\033[0m")
                continue
            if 0 < niveau < 99999:
                break
            else:
                print("\033[0;41mErreur : nombre entre 1 et 99 999 uniquement.\033[0m")
        nombre_mystere = random.randint(1, niveau)
        print("La partie va commencer", end="", flush=True)
        for t in range(3):
            time.sleep(0.5)
            print(".", end="", flush=True)
            if t == 2:
                time.sleep(0.5)
        tour = 0
        joueur_actuel = 1
        while True:
            tour += 1
            if fnc_cl == True:
                cl()
            else:
                pass
            pseudo = joueur1 if joueur_actuel == 1 else joueur2
            print(f"\033[35mC'est au tour de {pseudo}", end="", flush=True)
            try:
                pari = int(input("\n\n\033[33mVotre pari -> "))
            except ValueError:
                print(f"\033[0;41mVeuillez saisir un nombre entre 1 et {niveau}.")
                continue
            if pari > nombre_mystere:
                print("\n\033[35mLe nombre mystère est plus -PETIT-\033[0m")
                pause(0.7)
            elif pari < nombre_mystere:
                print("\n\033[35mLe nombre mystère est plus -GRAND-\033[0m")
                pause(0.7)
            else:
                print(f"\n\033[91m-BRAVO-, {pseudo} a trouvé le nombre mystère !\033[0m")
                pause(1.5)
                break
            joueur_actuel = 2 if joueur_actuel == 1 else 1
            time.sleep(1.5)
        score = niveau * niveau / tour
        cl()
        print(f"\033[35m{pseudo} a terminé la partie avec un score de {int(score)} points !\033[0m")
        time.sleep(2)
        while True:
            print("\n\033[33mTapez \033[32m-1-\033[33m pour rejouer ou \033[32m-2-\033[33m pour retourner au menu.\033[0m")
            try:
                retour_menu = int(input("\n->"))
            except ValueError:
                print("\033[0;41mSaisi invalide, veuillez reessayer en tapant -1- ou -2-\033[0m")
                pause(2)
                if fnc_cl == True:
                    cl()
                else:
                    pass
                continue
            if retour_menu not in [1, 2]:
                print("\033[0;41mSaisi invalide, veuillez reessayer en tapant -1- ou -2-\033[0m")
                pause(2)
                if fnc_cl == True:
                    cl()
                else:
                    pass
                continue
            elif retour_menu == 1:
                break
            else:
                break
        if retour_menu == 2:
            break
        else:
            pass

def Roulette_Russe_regle():
        global fnc_cl
        print("\033[91m========== RÈGLES DE LA ROULETTE RUSSE ==========\033[0m")
        pause(0.1)
        print("""\033[35m
        Bienvenue dans la Roulette Russe !

        1. Le jeu se déroule avec un revolver virtuel contenant 6 chambres.
        2. Une seule balle est placée aléatoirement dans l'une des chambres.
        3. À chaque tour :
        - Le joueur qui tire appuie sur la détente.
        4. Si la chambre est vide, le joueur survit et c’est au tour suivant.
        5. Si la balle est tirée... la partie est immédiatement perdue pour ce joueur.
        6. Le gagnant est celui qui survit quand l’autre succombe.
        7. Vous pouvez rejouer une nouvelle partie ou retourner au menu principal après chaque manche.

        Faites vos choix avec prudence… et bonne chance !
        """)
        pause(0.1)
        input("\033[33mAppuyez sur \033[32m-ENTRÉE-\033[33m pour continuer.\033[0m")

def Roulette_Russe():
    global fnc_cl
    Roulette_Russe_regle()
    Roulette_Russe_end = False

    while Roulette_Russe_end == False:
        if fnc_cl == True:
            cl()
        else:
            pass
        print("\033[36mLe robot insère la balle dans le barillet", end="", flush=True)
        for z in range(3):
            time.sleep(1)
            print(".", end="", flush=True)
            if z >= 2:
                time.sleep(1)
        if fnc_cl == True:
            cl()
        else:
            pass
        print("\033[36mLe robot a mis la balle...")
        time.sleep(2)
        print("\033[33mÀ vous maintenant de tourner le barillet...\033[0m")
        time.sleep(2.5)
        if fnc_cl == True:
            cl()
        else:
            pass
        print("\033[33mPour tourner le barillet, pressez \033[32m-ENTRÉE-\033[33m...")
        input()
        Roulette_Russe_barillet = [False, False, False, False, False, True]
        random.shuffle(Roulette_Russe_barillet)
        if fnc_cl == True:
            cl()
        else:
            pass
        print("\033[33mVous avez mélangé le barillet, puis vous tendez le pistolet au robot pour qu'il puisse commencer\033[0m", end="", flush=True)
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
        "\033[35mLe robot place le canon du pistolet sur sa tempe",
        "\033[35mLe robot dépose la pointe du canon entre ses deux yeux", 
        "\033[35mLe robot vise le fond de sa gorge", 
        "\033[35mLe robot vise un point, derrière lequel se trouve son cœur"
        ]
        Roulette_Russe_scripts_robot_mort = [
            "\033[31m*BANG!*, vous ouvrez les yeux, vous regardez le robot, sanglant, la tête qui pend sur le côté...\033[0m",
            "\033[31m*BANG!*, vos yeux se dirigent vers le robot... Rouge... C'est le seul mot qui vous vient à la tête...\033[0m",
            "\033[31m*BANG!*, vous vous levez, vous vous retournez et courez vers la porte de sortie, vous jetez un dernier regard sur le robot, inerte, sanglant...\033[0m"
        ]
        Roulette_Russe_scripts_robot_survie = [
            "\033[34m*CLIC!*, le robot s'en sort pour cette fois... À vous maintenant...\033[0m", 
            "\033[34m*CLIC!*, dommage, le robot est encore debout, à votre tour, bonne chance ! Ou pas...\033[0m", 
            "\033[34m*CLIC!*, c'est le seul petit bruit que produit le pistolet, le robot reste... À vous maintenant de connaître votre sort...\033[0m"
        ]
        Roulette_Russe_script_humain_survie = [
            "\n\033[32m*CLIC!*, vous n'êtes pas passé loin d'un destin tragique... Au tour du robot maintenant !\033[0m", 
            "\n\033[32m*CLIC!*, ce bruit vous rassure bien plus que n’importe quoi... Au tour du robot !\033[0m", 
            "\n\033[32m*CLIC!*, vous n'avez jamais eu autant goût à la vie... Au tour du robot !\033[0m"
        ]
        Roulette_Russe_humain = True
        while True:
            print("\033[35m--- TOUR DU ROBOT ---\033[0m")
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
            print("\n\033[36mIl presse de plus en plus la détente et\033[0m", end="", flush=True)
            for t in range(3):
                pause(0.7)
                print("\033[36m.\033[0m", end="", flush=True)
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
                print("\033[35m--- TOUR DU ROBOT ---\033[0m")
                time.sleep(random.randint(2, 5))
                print("\n\n", random.choice(Roulette_Russe_scripts_robot_mort))
                time.sleep(2)
                break
            else:
                cl()
                print(random.choice(Roulette_Russe_scripts_robot_survie))
                print(f"\n\033[33mIl reste {len(Roulette_Russe_barillet)} chambres à tirer...\033[0m")
                time.sleep(5)
                if fnc_cl == True:
                    cl()
                else:
                    pass
            print("\033[35m--- VOTRE TOUR ---\033[0m")
            print("\n\n\033[33mPressez \033[32m-ENTRÉE-\033[33m pour tirer...")
            input()
            Roulette_Russe_tir = Roulette_Russe_barillet.pop()
            if Roulette_Russe_tir == True:
                if fnc_cl == True:
                    cl()
                else:
                    pass
                print("\033[35m--- VOTRE TOUR ---\033[0m")
                time.sleep(0.1)
                print("\n\n\033[91m*BANG!*, vous êtes MORT...\033[0m")
                time.sleep(2)
                Roulette_Russe_humain = False
                break
            else:
                if fnc_cl == True:
                    cl()
                else:
                    pass
                print("\033[35m--- VOTRE TOUR ---")
                time.sleep(0.2)
                print(random.choice(Roulette_Russe_script_humain_survie))
                print(f"\n\033[34mIl reste {len(Roulette_Russe_barillet)} chambres à tirer\033[0m")
                time.sleep(5)
                if fnc_cl == True:
                    cl()
                else:
                    pass
                print("\033[35m--- VOTRE TOUR ---\033[0m")
                print("\n\033[33mPressez ENTRÉE pour donner le pistolet au robot.\033[0m")
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
            print("\033[91mBravo ! Vous avez survécu à cette partie !\033[0m")
        else:
            if fnc_cl == True:
                cl()
            else:
                pass
        while True:
            if fnc_cl == True:
                cl()
            else:
                pass
            print("\n\n\033[33mTapez \033[32m-1-\033[33m pour rejouer ou \033[32m-2-\033[33m pour retourner au menu.\033[0m")
            try:
                choix_retour_menu = int(input("\n\033[33m->\033[0m"))
            except ValueError:
                print("\033[41mSaisi invalide, veuillez saisir un nombre entre 1 et 2.\033[0m")
                pause(1.5)
                continue
            if choix_retour_menu == 1:
                break
            else:
                break
        if choix_retour_menu == 1:
            Roulette_Russe_end = False
        else:
            Roulette_Russe_end = True  

def roulette_russe_multijoueur_regle():
    print("\033[91m========== RÈGLES DE LA ROULETTE RUSSE MULTIJOUEURS ==========\033[0m")
    pause(0.1)
    print("""\033[35m
    Bienvenue dans la Roulette Russe Multijoueurs !

    1. Le jeu se déroule avec un revolver virtuel contenant 6 chambres.
    2. Une seule balle est placée aléatoirement dans l'une des chambres.
    3. Chaque joueur (jusqu’à 6 maximum) choisit son pseudo avant le début de la partie.
    4. Les joueurs jouent à tour de rôle dans l’ordre établi :
    - Le joueur courant appuie sur la détente.
    - Si la chambre est vide, il survit et passe la main au joueur suivant.
    - Si la balle est tirée, le joueur est éliminé immédiatement.
    5. La manche se termine dès qu’un joueur est touché.
    6. Les autres joueurs sont déclarés survivants et donc gagnants de la partie.
    7. Après chaque manche, vous pouvez recommencer une nouvelle partie ou retourner au menu principal.

    La tension monte à chaque tour… Qui survivra ?
    """)
    pause(0.1)
    input("\033[33mAppuyez sur \033[32m-ENTRÉE-\033[33m pour continuer.\033[0m")

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
        print("\033[33mCombien de joueurs êtes vous ?\033[0m")
        try:
            nbr_de_joueur = int(input("\n\033[33m->\033[0m"))
        except ValueError:
            print("\033[41mSaisi invalide, veuillez saisir un nombre.\033[0m")
            pause(2)
            if fnc_cl == True:
                cl()
            else:
                pass
            continue
        if nbr_de_joueur > 1:
            break
        else:
            print("\033[41mVous devez être plus de 1 joueur a participer.\033[0m")
            pause(2)
            if fnc_cl == True:
                cl()
            else:
                pass
            continue
    for e in range(nbr_de_joueur):
        joueurs_r_r.append(input(f"\033[33mJoueur {e + 1}, choisissez votre pseudo : \033[0m"))
    random.shuffle(roulette_russe_multijoueur_barillet)
    while len(joueurs_r_r) > 1:
        roulette_russe_multijoueur_barillet = [True, False, False, False, False, False]
        for joueur in range(len(joueurs_r_r)):
            if fnc_cl == True:
                cl()
            else:
                pass
            print(f"\033[36mJoueur {joueurs_r_r[joueur]}, a vous de connaître votre destint.\033[0m")
            print("\n\033[33mPour tirer, pressez \033[32m-ENTRÉE-\033[0m")
            input()
            if roulette_russe_multijoueur_barillet[joueur] == True:
                print(f"\033[91mJoueur {joueur}, vous êtes mort.\033[0m")
                joueurs_r_r.pop(joueur)
                roulette_russe_multijoueur_barillet.pop(joueur)
                pause(1.5)
                break
            else:
                print(f"\033[35mJoueur {joueur}, vous êtes encore en vie.\033[0m")
                roulette_russe_multijoueur_barillet.pop(joueur)
                pause(1.2)

def affichage_menu_aide():
    global fnc_cl
    if fnc_cl == True:
        cl()
    else:
        pass
    pause(0.05)
    print("\033[91m=========================================")
    pause(0.05)
    print("======= BYTE.ARCADE : RENAISSANCE =======")
    pause(0.05)
    print("=========================================\033[0m")
    pause(0.05)
    print("\n\n\033[36m=== MENU ===")
    pause(0.05)
    print("\n\n\033[35mFAQ : -1-")
    pause(0.05)
    print("\nCopyright : -2-")
    pause(0.05)
    print("\nMenu erreurs (beintôt disponible) : -3-")
    pause(0.05)
    print("\nRetour : -0-\033[0m")

def menu_aide():
    global fnc_cl
    while True:
        affichage_menu_aide()
        try:
            choix_menu_aide = int(input("\n\033[35m->\033[0m"))
        except ValueError:
            print("\033[41mSaisi invalide, veuillez reessayer en tapant 1, 2, 3 ou 0\033[0m")
            pause(2)
            if fnc_cl == True:
                cl()
            else:
                pass
            continue
        if choix_menu_aide not in [1, 2, 3, 0]:
            print("\033[41mSaisi invalide, veuillez reessayer en tapant 1, 2, 3 ou 0\033[0m")
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
    pause(0.05)
    print("\033[91m=========================================")
    pause(0.05)
    print("======= BYTE.ARCADE : RENAISSANCE =======")
    pause(0.05)
    print("=========================================\033[0m")
    pause(0.05)
    print("\n\n\033[36m=== MENU JEUX ===\033[0m")
    pause(0.05)
    print("\n\n\033[35mJuste Prix original : -1-\t\tRoulette Russe : -4-")
    pause(0.05)
    print("\nJuste Prix remake : -2-\t\t\tRoulette Russe multijoueur : -5-")
    pause(0.05)
    print("\nJuste Prix multijoueur : -3-")
    pause(0.05)
    print("\nRetour : -0-\033[0m")

def menu_jeu():
    while True:
        if fnc_cl == True:
            cl()
        else:
            pass
        affichage_menu_jeu()
        try:
            choix_menu_jeu = int(input("\n\033[35m->\033[0m"))
        except ValueError:
            print("\033[41mSaisi invalide, veuillez reessayer en tapant 1, 2, 3, 4 ou 0\033[0m")
            pause(2)
            if fnc_cl == True:
                cl()
            else:
                pass
            continue
        if choix_menu_jeu not in [1, 2, 3, 4, 5, 0]:
            print("\033[41mSaisi invalide, veuillez reessayer en tapant 1, 2, 3, 4, 5 ou 0\033[0m")
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
    pause(0.05)
    print("\033[91m=========================================")
    pause(0.05)
    print("======= BYTE.ARCADE : RENAISSANCE =======")
    pause(0.05)
    print("=========================================\033[0m")
    pause(0.05)
    print("\n\n\033[36m=== MENU ===\033[0m")
    pause(0.05)
    print("\n\n\033[35mAcceder au jeu : -1-")
    pause(0.05)
    print("\nAide : -2-")
    pause(0.05)
    print("\nQuitter : -0-\033[0m")

def menu_principal():
    while True:
        if fnc_cl == True:
            cl()
        else:
            pass
        affichage_menu_principal()
        try:
            choix_menu_principal = int(input("\n\033[35m->\033[0m"))
        except ValueError:
            print("\033[41mSaisi invalide, veuillez reessayer en tapant 1, 2, ou 0\033[0m")
            pause(2)
            if fnc_cl == True:
                cl()
            else:
                pass
            continue
        if choix_menu_principal not in [1, 2, 0]:
            print("\033[41mSaisi invalide, veuillez reessayer en tapant 1, 2, ou 0\033[0m")
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

menu_principal()