op_time = False
op_random = False
op_os = False
op_sys = False
os_line_jump = 50
import_errors = []

def time_error():
    global op_time
    op_time = "NA"
def random_error():
    global op_random
    op_random = "NA"
def os_error():
    global op_os
    op_os = "NA"
def sys_error():
    global op_sys
    op_sys = "NA"

try:
    import time
except Exception as e:
    import_errors.append(f"\033[91mLe module 'time' n'a pas pu être importé.\033[96m {e}\033[0m")
    time_error()
try:
    import random
except Exception as e:
    import_errors.append(f"\033[91mLe module 'random' n'a pas pu être importé.\033[96m {e}\033[0m")
    random_error()
try:
    import os
except Exception as e:
    import_errors.append(f"\033[91mLe module 'os'a pas pu être importé.\033[96m {e}\033[0m")
    os_error()
try:
    import sys
except Exception as e:
    import_errors.append(f"\033[91mLe module 'sys' n'a pas pu être importé.\033[96m {e}\033[0m")
    sys_error()

def error_recap():
    global import_errors
    if len(import_errors) > 0:
        print("\033[95mRécapitulatif des erreurs survenues :\033[0m\n")
        for erreurs in import_errors:
            print(f"\n\033[95m- Erreur d'importation : {erreurs}\033[0m")
        print("\n\n\033[41mLes options liées aux erreurs ci-dessus ont étées désactivées\033[0m")
        input("\n\033[93mPressez \033[92m-ENTRÉE-\033[93m pour continuer.")
    else:
        pass

def init_modules():
    global op_time, op_random, op_os, op_tty, op_termios, op_sys
    print("\033[95mInitialisation des modules...\033[0m")

    op_time = True
    op_random = True
    op_os = True
    op_tty = True
    op_termios = True
    op_sys = True

    try:
        time.sleep(1)
    except Exception:
        op_time = "NA"
    try:
        random.randint(1, 2)
    except Exception:
        op_random = "NA"
    try:
        os.system('cls' if os.name == 'nt' else 'clear')
    except Exception:
        op_os = "NA"
    try:
        print(sys.version)
    except Exception:
        op_sys = "NA"

def cl():
    global op_os, os_line_jump
    if op_os == "NA":
        print("\n"*os_line_jump)
    elif op_os == True:
        os.system('cls' if os.name == 'nt' else 'clear')

def pause(temps):
    global op_time
    if op_time == "NA":
        pass
    elif op_time == True:
        time.sleep(temps)

def cl_settings():
    global os_line_jump, op_os
    while True:
        os_status = None
        os_command = None
        if op_os == True:
            os_status = "\033[41m activé \033[0m"
            os_command = "\033[95mdésactiver\033[0m"
        elif op_os == "NA":
            os_status = "\033[41m désactivé \033[0m"
            os_command = "\033[95mtenter d'activer\033[0m"
        else:
            os_status = "\033[41m inconnu \033[0m"
            os_command = "\033[91maucune action possible\033[0m"
        cl()
        print("\033[96m=== Paramètres fonctionnalité 'os' ===\033[0m")
        print(f"\n\033[91mStatus 'os' : {os_status}")
        print(f"\n\n{os_command} : \033[92m-1-\033[0m")
        if op_os != True:
            print(f"\n\033[95mChanger le nombre de saut de ligne : \033[92m-2-\033[91m (actuel : {os_line_jump})")
        print("\n\033[95mRevenir : \033[92m-0-\033[0m")
        choix = input("\n\033[93m->\033[0m")
        if choix == "1":
            if op_os == True:
                op_os = "NA"
            else:
                init_modules()
        elif choix == '2':
            while True:
                cl()
                print(f"\033[91mNombre de sauts de lignes actuel : {os_line_jump}\033[0m")
                try:
                    choix_bis = int(input("\033[93mNouveau nombre de sauts de linges : \033[0m"))
                except ValueError:
                    print("\033[41mSaisi invalide, veuillez reessayer.\033[0m")
                    continue
                os_line_jump = choix_bis
                break
        elif choix == '0':
            break

def time_setting():
    global op_time
    while True:
        time_status = None
        time_command = None
        if op_time == "NA":
            time_status = "\033[41m désactivé \033[0m"
            time_command = "\033[95mtenter d'activer\033[0m"
        elif op_time == True:
            time_status = "\033[41m activé \033[0m"
            time_command = "\033[95mdésactiver\033[0m"
        else:
            time_status = "\033[41m inconnu \033[0m"
            time_command = "\033[91maucune action possible\033[0m"
        
        cl()
        print("\033[96m=== Paramètres fonctionnalité 'time' ===\033[0m")
        print(f"\n\033[91mStatus 'time' : {time_status}")
        print(f"\n\n{time_command} : \033[92m-1-\033[0m")
        print("\n\033[95mRevenir : \033[92m-0-\033[0m")
        choix = input("\n\033[93m->\033[0m")
        if choix == "1":
            if op_time == True:
                op_time = "NA"
            else:
                init_modules()
        elif choix == "0":
            break

def barre_de_chargement(total, temps):
    for p in range(total+1):
        barre = "[" + "#" * p + "-" * (total-p) + "]"
        sys.stdout.write("\r" + barre + f" {p*2.5}%")
        sys.stdout.flush()
        pause(temps)
        cl()
    for o in range(5):
        cl()
        print("[########################################] 100%")
        pause(0.15)
        cl()
        print("\033[32m[######## BYTE #### . ### ARCADE ########] 100%\033[0m")
        pause(0.15)

def animation_acceuil():
    cl()
    print("=== Byte.Arcade ===")
    pause(2)
    cl()
    print("Un jeu original de Byte.Games Studios")
    pause(2)
    cl()
    print("© 2025 Byte.Games Studios")
    pause(2)
    cl()
    print("Version du jeu : 6.0")
    pause(2)
    cl()
    print("Emplacement d'execution : ", os.getcwd())
    pause(2)
    cl()

def didactitiel():
    cl()
    while True:
        cl()
        print("\t\t\t\t\033[91m=== INFORMATION ===\033[0m")
        print("\n\033[95mDans ce jeu, pour séléctionner une option, vous devez saisir le numéro associé à cette option,\n" \
        "puis, pressez \033[92m-ENTRÉE-.\033[0m\n\n" \
        "\033[95mComme vous aurez l'occasion de le constater, les numéros saisissables sont colorés en \033[92mvert\033[95m, les action réalisables, elles,\n" \
        "sont colorés en \033[93mjaune.\033[0m")
        choix = input("\n\033[93mPour continuer, séléctionnez \033[92m-1-\n\n\033[93m->\033[0m")
        if choix == "1":
            break
        else:
            print("\n\033[41mSaisi invalide, veuillez saisir le numéro demandé.\033[0m")
            pause(1.5)

def changelog():
    cl()
    print("\033[41m=== ATTENTION ===\033[91m\n\nLe changelog n'as pas encore bénéficié de mise a jour récente,\nil se peut donc que certaines informations manque a l'appelle." \
    "\nMerci de votre compréhension.\n\tL'équipe Byte.Aracde")
    print("""
          
\033[96m- Version original du jeu : 28/07/2025
\033[96m- Version 2.0 : 29/07/2025\033[95m
	Ajout du jeu ROULETTE RUSSE
	Possibilitée de revenir au menu sans redémarrer le jeu
\033[96m- Version 2.1 : 30/07/2025\033[95m
	Optimisation du code (Plus lisible, moins complexe et modification de la boucle pricipal du jeu)
	Commencement du code du futur jeu ROULETTE RUSSE MULTIJOUEUR
\033[96m- Version 3.0 : 30/07/2025\033[95m
	Ajout du jeu ROULETTE RUSSE MULTIJOUEUR
\033[96m- Version 3.1 : 31/07/2025\033[95m
	Correction d'un bug dans le jeu ROULETTE RUSSE MULTIJOUEUR [ ligne 323 ]
	Ajout de la posibilitée de choisir son propre pseudo dans ROULETTE RUSSE MULTIJOUEUR
\033[96m- Version 3.2 : 31/07/2025\033[95m
	Correction d'un bug dans le jeu JUSTE PRIX MULTIJOUEUR
 	Ajout du Copyright de Code'n'Play games provisoire
\033[96m- Version 3.3 : 31/07/2025\033[95m
    Version définitive modifiable du Copyright de Byte.Arcade Games et ajout du contact mail // ***@********.se //
\033[96m- Version 3.4 : 31/07/2025\033[95m
    Ajout de la FAQ
\033[96m- Version 3.5 : 31/07/2025\033[95m
    Ajout du changelog dans le jeu
\033[96m- version 3.6 : 31/07/2025\033[95m
    Nouvelle animation d'accueil
	Ajout du système de suspense dans le jeu ROULETTE RUSSE
\033[96m- version 4.0 : 01/07/\033[95m
	Ajout du jeu BLACK JACK
	Ajout des règles des jeux en tant que fonction
\033[96m- version 4.1 : 01/07/2025\033[95m
	Ajout de la fin du code de BLACK JACK
	Correction du bug dans le jeu BLACK JACK {entré = menu jeu != continuer la partie}
\033[96m- version 4.2 : 25/08/2025\033[95m
	Clarification des règle du jeu et amélioration de la compréhension du code source au niveau de l'affichage des règle intra code
\033[96m- version 5.0 : 24/09/2025\033[95m
	Refonte complète du code source
	Amélioration de l'interface
	Nouvelle version du jeu ROULETTE RUSSE
	Jeu BLACK JACK indisponible
	Encore plus de suspense
\033[96m- version 5.1 :\033[95m
	Ajouts des couleurs dans l'interface
	Correction du bug au niveau des erreurs de saisis\033[0m

    """)
    input("\033[93mPressez \033[92m-ENTRÉE-\033[93m pour revenir au menu.\033[95m")
    cl()

def copyright():
    cl()
    print("""
          
 \033[91m===============================================================
                  © 2025 Byte.Games Studios                   
 ===============================================================
 \033[95mTitre du jeu : Byte.Arcade
 Développé par : Byte.Games Studios
 Auteur principal : Lou.T
 Contact : byte.arcadestudios.dev@gmail.com
 ---------------------------------------------------------------
 Tous droits réservés. Ce jeu et son contenu, incluant mais ne
 se limitant pas au code source, graphismes, sons, textes et
 mécaniques de jeu, sont protégés par les lois européennes et
 internationales relatives à la propriété intellectuelle.
 ---------------------------------------------------------------
 Toute reproduction, distribution, modification ou exploitation
 partielle ou totale de ce logiciel sans l’autorisation écrite
 préalable de Byte.Games Studios est strictement interdite et
 poursuivie conformément au Code de la Propriété Intellectuelle
 et aux directives de l’Union Européenne en vigueur.
 ---------------------------------------------------------------
 Byte.Arcade est une marque déposée de Byte.Games Studios.
 ---------------------------------------------------------------
 Crédits :
 - Développement & conception : Lou.T
 - Test & optimisation : Byte.Games Studios
 - Support technique : Byte.Games Studios
 ---------------------------------------------------------------
 Toute utilisation commerciale non autorisée est interdite.
 Toute violation pourra donner lieu à des poursuites civiles et
 pénales conformément aux lois applicables.
 ---------------------------------------------------------------
 Pour signaler un bug,
 poser une question ou partager vos suggestions,
 merci de contacter l’équipe Byte.Games Studios à
 l’adresse suivante : ###.
 Chaque retour est pris en compte afin de perfectionner
 Byte.Arcade et offrir la meilleure expérience à tous.
 ===============================================================
 Merci d’avoir choisi Byte.Arcade — Un projet Byte.Games Studios
 \033[91m===============================================================

    """)
    input("\033[93mPressez \033[92m-ENTRÉE-\033[93m pour revenir au menu.\033[0m")

def affichage_menu_information():
    cl()
    print("\033[91m======================================")
    print("============ \033[93mBYTE.ARCADE\033[91m =============")
    print("======================================\033[0m")
    print("\n\033[93m=== MENU ===")
    print("\n\033[95mCopyrights : \033[92m-1-")
    print("\n\033[95mChangelog : \033[92m-2-")
    print("\n\033[95mMise à Jour a venir : \033[92m-3-")
    print("\n\033[91mRetour : -0-\033[0m")
    print("\t\t\t\t\t\t\033[93mby Byte.Games Studios © 2025\033[0m")

def menu_information():
    while True:
        affichage_menu_information()
        choix = input("\033[93m->\033[0m")
        if choix == "1":
            copyright()
        elif choix == "2":
            changelog()
        elif choix == "3":
            pass
        elif choix == "0":
            break
        else:
            print("\n\033[0;41mSaisi invalide, veuillez saisir un nombre entre 1, 2, 3 et 0.\033[0m")
            pause(1.2)

def affichage_menu_aide():
    cl()
    print("\033[91m======================================")
    print("============ \033[93mBYTE.ARCADE\033[91m =============")
    print("======================================\033[0m")
    print("\n\033[93m=== MENU AIDE ===")
    print("\n\033[95mFAQ : \033[92m-1-")
    print("\n\033[95mAssistance : \033[92m-2-")
    print("\n\033[95mRefaire le didactitiel : \033[92m-3-")
    print("\n\033[91mRetour : -0-\033[0m")
    print("\t\t\t\t\t\t\033[93mby Byte.Games Studios © 2025\033[0m")

def menu_aide():
    while True:
        affichage_menu_aide()
        choix = input("\033[93m->\033[0m")
        if choix == "1":
            FAQ()
        elif choix == "2":
            pass
        elif choix == "3":
            didactitiel()
        elif choix == "0":
            break
        else:
            print("\n\033[0;41mSaisi invalide, veuillez saisir un nombre entre 1, 2, 3 et 0.\033[0m")
            pause(1.2)

def affichage_menu_jeu():
    cl()
    print("\033[91m======================================")
    print("============ \033[93mBYTE.ARCADE\033[91m =============")
    print("======================================\033[0m")
    print("\n\033[93m=== JEUX ===")
    print("\n\033[95mJuste Prix original : \033[92m-1-\t\033[95mRoulette Russe : \033[92m-4-")
    print("\n\033[95mJuste Prix remake : \033[92m-2-\t\t\033[95mRoulette Russe multijoueur : -5- \033[92m-5-")
    print("\n\033[95mJuste Prix multijoueur : \033[92m-3-\t\033[95mPile ou Face casino : -6-\033[92m-6-")
    print("\n\033[91mRetour : -0-\033[95m")
    print("\t\t\t\t\t\t\033[93mby Byte.Games Studios © 2025\033[0m")

def menu_jeux():
    while True:
        affichage_menu_jeu()
        choix = input("\033[93m->\033[0m")
        if choix == "1":
            juste_prix_original()
        if choix == "2":
            juste_prix_remake()
        if choix == "3":
            juste_prix_multijoueur()
        if choix == "4":
            Roulette_Russe()
        if choix == "5":
            roulette_russe_multijoueur()
        if choix == "6":
            pile_ou_face()
        if choix == "0":
            break

def affichage_menu_parametres():
    cl()
    print("\033[91m======================================")
    print("============ \033[93mBYTE.ARCADE\033[91m =============")
    print("======================================\033[0m")
    print("\n\033[93m=== MENU PARAMÈTRES ===")
    print("\n\033[95mParamètres fonction 'cl()' : \033[92m-1-")
    print("\n\033[95mParamètre fonction 'pause()' : \033[92m-2-")
    print("\n\033[91mRetour : -0-\033[0m")
    print("\t\t\t\t\t\t\033[93mby Byte.Games Studios © 2025\033[0m")

def menu_parametres():
    while True:
        affichage_menu_parametres()
        choix = input("\033[93m->\033[0m")
        if choix == "1":
            cl_settings()
        elif choix == "2":
            time_setting()
        elif choix == "0":
            break
        else:
            print("\n\033[0;41mSaisi invalide, veuillez saisir un nombre entre 1, 2, 3 et 0.\033[0m")
            pause(1.2)

def affichage_menu_principal():
    cl()
    print("\033[91m======================================")
    print("============ \033[93mBYTE.ARCADE\033[91m =============")
    print("======================================\033[0m")
    print("\n\033[93m=== MENU ===")
    print("\n\033[95mAcceder au jeu : \033[92m-1-")
    print("\n\033[95mAide : \033[92m-2-")
    print("\n\033[95mInformations : \033[92m-3-")
    print("\n\033[95mParamètres : \033[92m-4-\n\t\t\t\t\t\t\033[93mby Byte.Games Studios © 2025\033[0m")
    print("\033[91mQuitter : -0-\033[0m")
    
def menu_principal():
    while True:
        affichage_menu_principal()
        choix = input("\n\033[93m->\033[0m")
        if choix == "1":
            menu_jeux()
        elif choix == "2":
            menu_aide()
        elif choix == "3":
            menu_information()
        elif choix == "3":
            pass
        elif choix == "4":
            menu_parametres()
        elif choix == "0":
            sys.exit()
        else:
            print("\n\033[0;41mSaisi invalide, veuillez saisir un nombre entre 1, 2, 3, 4 et 0.\033[0m")
            pause(1.2)

def logo_juste_prix():
    print("\033[91m======================================")
    print("============ \033[93mJUSTE  PRIX\033[91m =============")
    print("======================================\033[0m")

def FAQ():
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
            cl()
            print("\n\033[91m========== BYTE.ARCADE FAQ ==========\033[0m\n")
            for i, (q, _) in enumerate(faq, 1):
                print(f"\033[92m-{i}- \033[95m{q}")
            print("\n\033[91m=====================================\033[0m")
            print("\n\033[92m-0-\033[93m pour revenir au menu principal.\033[0m\n")
            try:
                choix = int(input("\033[93mEntrez le numéro de la question pour voir la réponse : \033[0m"))
                if choix == 0:
                    break
                elif 1 <= choix <= len(faq):
                    cl()
                    print(f"\n\033[96mQ: {faq[choix-1][0]}")
                    print(f"\033[95mR: {faq[choix-1][1]}\033[0m")
                    input("\n\033[93mPressez \033[92m-ENTRÉE-\033[93m lorsque vous avez terminé.\033[0m")
                else:
                    print("\n\033[0;41mNuméro invalide, réessayez.\033[0m")
                    pause(1)
            except ValueError:
                print("\n\033[0;41mVeuillez entrer un numéro valide.\033[0m")
                pause(1)

def juste_prix_original():
    game = True
    cl()
    barre_de_chargement(40, 0.03)
    cl()
    logo_juste_prix()
    print("""\033[95m
    Bienvenue dans le Juste Prix Original !

    1. Le jeu choisit un nombre mystère fixe selon le niveau choisi.
    2. Vous devez deviner ce nombre.
    3. Après chaque essai, un indice vous sera donné :
    - "Plus GRAND" si le nombre mystère est plus élevé,
    - "Plus PETIT" si le nombre mystère est plus bas.
    4. Le score est calculé selon le nombre d'essais.
    5. Si vous saisissez une valeur non numérique, vous devrez ressaisir un nombre valide.
    6. Après chaque partie, vous pouvez rejouer ou retourner au menu principal.

    Bonne chance !\033[0m
    """)
    input("\033[93mPressez \033[92m-ENTRÉE-\033[93m pour continuer.\033[0m")
    while game == True:
        while True:
            cl()
            logo_juste_prix()
            print("\n\033[93mChoisissez votre niveau :")
            print("\n\n\033[92m-1-\033[95m : le nombre a trouver est compris en 1 et 10")
            print("\n\033[92m-2-\033[95m : entre 1 et 20")
            print("\n\033[92m-3-\033[95m : entre 1 et 50")
            print("\n\033[92m-4-\033[95m : entre 1 et 100")
            print("\n\033[92m-5-\033[95m : entre 1 et 150")
            print("\n\033[92m-6-\033[95m : entre 1 et 200")
            print("\n\033[92m-7-\033[95m : entre 1 et 300")
            print("\n\033[92m-8-\033[95m : entre 1 et 500")
            print("\n\033[92m-9-\033[95m : entre 1 et 1000\033[0m")
            choix = input("\n\033[93m->")
            if choix == "1":
                maxx = 10
                break
            elif choix == "2":
                maxx = 20
                break
            elif choix == "3":
                maxx = 50
                break
            elif choix == "4":
                maxx = 100
                break
            elif choix == "5":
                maxx = 150
                break
            elif choix == "6":
                maxx = 200
                break
            elif choix == "7":
                maxx = 300
                break
            elif choix == "8":
                maxx = 500
                break
            elif choix == "9":
                maxx = 1000
                break
            else:
                print("\n\033[0;41mSaisi invalide, veuillez sasir un nombre entre 1 et 9.\033[0m")
                pause(1.2)
        nombre_mystere = random.randint(1, maxx)
        tour = 0
        while True:
            tour += 1
            cl()
            logo_juste_prix()
            print(f"\n\033[95mLe nombre mystère est compris entre 1 et {maxx}.")
            try:
                pari = int(input("\n\033[93mVotre pari ->"))
            except ValueError:
                print("\033[97;41mSaisi invalide, veuillez saisir uniquement le nombre que vous choisissez de parier.\033[0m")
                tour -= 1
                pause(1.2)
                continue
            if pari > maxx:
                print(f"\033[97;41mSaisi invalide, veuillez saisir un nombre en dessous de {maxx}.\033[0m")
                tour -= 1
                pause(1.3)
                continue
            elif pari < 1:
                print(f"\033[97;41mSaisi invalide, veuillez saisir un nombre au dessus de 0.\033[0m")
                tour -= 1
                pause(1.2)
                continue
            else:
                pass
            if pari > nombre_mystere:
                print("\n\033[95mLe nombre mystère est plus \033[91m-PETIT-\033[0m")
                pause(0.7)
            elif pari < nombre_mystere:
                print("\n\033[95mLe nombre mystère est plus \033[91m-GRAND-\033[0m")
                pause(0.7)
            elif pari == nombre_mystere:
                cl()
                logo_juste_prix()
                print(f"\n\033[91m-BRAVO-\033[95m tu as trouvé le nombre mystère au tour {tour} !\033[0m")
                score = maxx / tour * 100
                print(f"\033[95mTu as terminé la partie avec un score de {int(score)} points.")
                input("\n\033[93mPressez \033[92m-ENTRÉE-\033[93m pour continuer.\033[0m")
                break
        while True:
            cl()
            logo_juste_prix()
            print("\n\033[93mSéléctionnez \033[92m-1-\033[93m pour rejouer ou \033[92m-2-\033[93m pour revenir au menu.\033[0m")
            choix = input("\n\033[93m->\033[0m")
            if choix == "1":
                break
            elif choix == "2":
                game = False
                break
            else:
                print("\033[41mSaisi invalide, veuillez saisir un nombre entre 1 et 2.\033[0m")
                pause(1.3)

def juste_prix_remake():
    game = True
    while game == True:
        cl()
        barre_de_chargement(40, 0.05)
        cl()
        logo_juste_prix()
        print("""\n\033[95m
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

        Bonne chance ! Essayez de battre votre record !\033[0m
        """)
        input("\n\033[93mPressez \033[92m-ENTRÉE-\033[93m pour continuer.")
        while True:
            cl()
            logo_juste_prix()
            print("\n\033[93mChoisissez le nombre maximum tirable au sort par l'ordinateur.")
            try:
                maxx = int(input("\n->\033[0m"))
            except ValueError:
                print("\033[0;41mSaisi invalide, veuillez saisir un nombre.\033[0m")
                pause(1.1)
                continue
            if maxx < 2:
                print("\033[0;41mSaisi invalide, veuillez saisir un nombre plus grand que 1.\033[0m")
                pause(1.1)
                continue
            else:
                break
        nombre_mystere = random.randint(1, maxx)
        tour = 0
        while True:
            tour += 1
            cl()
            logo_juste_prix()
            print(f"\033[93mPariez un nombre entre 1 et {maxx}\033[0m")
            try:
                pari = int(input("\n\033[93m->\033[0m"))
            except ValueError:
                print(f"\033[0;41mSaisi invalide, veuillez saisir un nombre compris entre 1 et {maxx}\033[0m")
                pause(1.3)
                continue
            if pari > maxx:
                print(f"\033[0;41mSaisi invalide, veuillez saisir un nombre compris entre 1 et {maxx}\033[0m")
                pause(1.3)
                continue
            elif pari < 1:
                print(f"\033[0;41mSaisi invalide, veuillez saisir un nombre compris entre 1 et {maxx}\033[0m")
                pause(1.3)
                continue
            elif pari > nombre_mystere:
                print("\n\033[95mLe nombre mystère est plus \033[91m-PETIT-\033[0m")
                pause(1)
            elif pari < nombre_mystere:
                print("\n\033[95mLe nombre mystère est plus \033[91m-GRAND-\033[0m")
                pause(1)
            else:
                print(f"\033[91m-BRAVO-\033[95m vous avez trouvé le nombre mystère en {tour} tour !\033[0m")
                score = maxx / tour * 100
                print(f"\033[95mVous avez obtenu un score de {int(score)}\033[0m")
                input("\n\033[93mPressez \033[92m-ENTRÉE-\033[93m pour continuer.")
                break
        while True:
            cl()
            logo_juste_prix()
            print("\n\033[93mSéléctionnez \033[92m-1-\033[93m pour rejouer ou \033[92m-2-\033[93m pour revenir au menu.\033[0m")
            choix = input("\n\033[93m->\033[0m")
            if choix == "1":
                break
            elif choix == "2":
                game = False
                break
            else:
                print("\033[41mSaisi invalide, veuillez saisir un nombre entre 1 et 2.\033[0m")
                pause(1.3)

def juste_prix_multijoueur():
    liste_des_joueurs = []
    game = True
    cl()
    barre_de_chargement(40, 0.02)
    cl()
    logo_juste_prix()
    print("""\n\033[95m
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
    input("\033[93mPressez \033[92m-ENTRÉE-\033[93m pour continuer.\033[0m")
    while game == True:
        while True:
            cl()
            logo_juste_prix()
            print("\n\033[93mCombien êtes vous ?")
            try:
                choix = int(input("\n\033[93m->\033[0m"))
            except ValueError:
                print("\n\033[0;41mSaisi invalide, veuillez saisir un nombre.\033[0m")
                pause(1.2)
                continue
            if choix > 1:
                break
        cl()
        logo_juste_prix()
        print()
        for i in range(choix):
            joueur = input(f"\033[93mJoueur {i+1}, choisissez un pseudo : \033[0m")
            liste_des_joueurs.append(joueur)
        while True:
            cl()
            logo_juste_prix()
            print("\n\033[93mChoisissez le nombre maximum tirable au sort.")
            try:
                maxx = int(input("\n\033[93m->\033[0m"))
            except ValueError:
                print("\033[0;41mSaisi invalide, veuillez saisir un nombre.\033[0m")
                pause(1.2)
                continue
            if choix > 1:
                break
            else:
                print("\033[0;41mSaisi invalide, veuillez saisir un nombre plus grand que 1.\033[0m")
                pause(1.2)
        nombre_mystere = random.randint(1, maxx)
        cl()
        logo_juste_prix()
        print("\n\033[96mLa partie va commencer", end="", flush=True)
        for u in range(3):
            pause(0.5)
            print(".", end="", flush=True)
            if u >= 2:
                pause(0.5)
                "\033[0m"
        gagnant = ""
        while gagnant == "":
            for t in range(len(liste_des_joueurs)):
                cl()
                logo_juste_prix()
                while True:
                    cl()
                    logo_juste_prix()
                    try:
                        choix = int(input(f"\n\033[93m{liste_des_joueurs[t]}, à vous de parier : \033[0m"))
                    except ValueError:
                        print("\n\033[0;41mSaisi invalide, veuillez saisir un nombre.\033[0m")
                        pause(1.2)
                        continue
                    if choix > maxx:
                        print(f"\n\033[0;41mSaisi invalide, veuillez saisir un nombre plus petit que {maxx}.\033[0m")
                        pause(1.2)
                        continue
                    elif choix < 1:
                        print(f"\n\033[0;41mSaisi invalide, veuillez saisir un nombre plus grand que 1.\033[0m")
                        pause(1.2)
                        continue
                    break
                if choix > nombre_mystere:
                    print("\n\033[95mLe nombre mystère est plus \033[91m-PETIT-\033[0m")
                    pause(1)
                elif choix < nombre_mystere:
                    print("\n\033[95mLe nombre mystère est plus \033[91m-GRAND-\033[0m")
                    pause(1)
                else:
                    print("\n\033[91m-BRAVO-")
                    pause(1)
                    gagnant = liste_des_joueurs[t]
                    break
        cl()
        logo_juste_prix()
        pause(0.5)
        print(f"\n\033[95mLe gagnant est {gagnant} !")
        print(f"\nLe nombre mystère était {nombre_mystere}.")
        pause(1)
        input("\n\033[93mPressez \033[92m-ENTRÉE-\033[93m pour continuer.\033[0m")
        while True:
            cl()
            logo_juste_prix()
            print("\n\033[93mSéléctionnez \033[92m-1-\033[93m pour rejouer ou \033[92m-2-\033[93m pour revenir au menu.\033[0m")
            choix = input("\n\033[93m->\033[0m")
            if choix == "1":
                break
            elif choix == "2":
                game = False
                break
            else:
                print("\033[91mSaisi invalide, veuillez saisir un nombre entre 1 et 2.\033[0m")
                pause(1.3)

def roulette_russe_regle():
    print("\033[91m========== RÈGLES DE LA ROULETTE RUSSE ==========\033[0m")
    print("""\033[95m
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
    input("\033[93mAppuyez sur \033[92m-ENTRÉE-\033[93m pour continuer.\033[0m")
    
def Roulette_Russe():
    barre_de_chargement(40, 0.03)
    roulette_russe_regle()
    Roulette_Russe_end = False
    while Roulette_Russe_end == False:
        cl()
        print("\033[36mLe robot insère la balle dans le barillet", end="", flush=True)
        for z in range(3):
            pause(0.5)
            print(".", end="", flush=True)
        pause(1)
        cl()
        print("\033[36mLe robot a mis la balle...")
        pause(1.5)
        cl()
        print("\033[33mÀ vous maintenant de tourner le barillet...\033[0m")
        pause(1)
        print("\033[33mPour tourner le barillet, pressez \033[32m-ENTRÉE-\033[33m...")
        input()
        Roulette_Russe_barillet = [False, False, False, False, False, True]
        random.shuffle(Roulette_Russe_barillet)
        cl()
        print("\033[33mVous avez mélangé le barillet, puis vous tendez le pistolet au robot pour qu'il puisse commencer\033[0m", end="", flush=True)
        for t in range(3):
            pause(0.7)
            print(".", end="", flush=True)
        pause(0.7)
        cl()
        pause(1)
        Roulette_Russe_scripts_robot_tour = [
            "\033[95mLe robot place le canon du pistolet sur sa tempe",
            "\033[95mLe robot dépose la pointe du canon entre ses deux yeux", 
            "\033[95mLe robot vise le fond de sa gorge", 
            "\033[95mLe robot vise un point, derrière lequel se trouve son cœur"
        ]
        Roulette_Russe_scripts_robot_mort = [
            "\033[91m*BANG!*, vous ouvrez les yeux, vous regardez le robot, sanglant, la tête qui pend sur le côté...\033[0m",
            "\033[91m*BANG!*, vos yeux se dirigent vers le robot... Rouge... C'est le seul mot qui vous vient à la tête...\033[0m",
            "\033[91m*BANG!*, vous vous levez, vous vous retournez et courez vers la porte de sortie, vous jetez un dernier regard sur le robot, inerte, sanglant...\033[0m"
        ]
        Roulette_Russe_scripts_robot_survie = [
            "\033[94m*CLIC!*, le robot s'en sort pour cette fois... À vous maintenant...\033[0m", 
            "\033[94m*CLIC!*, dommage, le robot est encore debout, à votre tour, bonne chance ! Ou pas...\033[0m", 
            "\033[94m*CLIC!*, c'est le seul petit bruit que produit le pistolet, le robot reste... À vous maintenant de connaître votre sort...\033[0m"
        ]
        Roulette_Russe_script_humain_survie = [
            "\n\033[92m*CLIC!*, vous n'êtes pas passé loin d'un destin tragique... Au tour du robot maintenant !\033[0m", 
            "\n\033[92m*CLIC!*, ce bruit vous rassure bien plus que n’importe quoi... Au tour du robot !\033[0m", 
            "\n\033[92m*CLIC!*, vous n'avez jamais eu autant goût à la vie... Au tour du robot !\033[0m"
        ]
        Roulette_Russe_humain = True
        while Roulette_Russe_humain and len(Roulette_Russe_barillet) > 0:
            cl()
            print("\033[95m--- TOUR DU ROBOT ---\033[0m")
            print("\n\n", random.choice(Roulette_Russe_scripts_robot_tour), end="", flush=True)
            for t in range(3):
                pause(0.5)
                print(".", end="", flush=True)
            pause(0.5)
            cl()
            pause(random.randint(1,3))
            print("\n\033[96mIl presse de plus en plus la détente et\033[0m", end="", flush=True)
            for t in range(3):
                pause(0.5)
                print("\033[96m.\033[0m", end="", flush=True)
            pause(0.5)
            Roulette_Russe_tir = Roulette_Russe_barillet.pop()
            pause(random.randint(1, 2))
            if Roulette_Russe_tir:
                cl()
                print("\033[95m--- TOUR DU ROBOT ---\033[0m")
                pause(random.randint(1,3))
                print("\n\n", random.choice(Roulette_Russe_scripts_robot_mort))
                pause(2)
                break
            else:
                cl()
                print(random.choice(Roulette_Russe_scripts_robot_survie))
                print(f"\n\033[93mIl reste {len(Roulette_Russe_barillet)} chambres à tirer...\033[0m")
                pause(2)
            cl()
            print("\033[95m--- VOTRE TOUR ---\033[0m")
            print("\n\n\033[93mPressez \033[92m-ENTRÉE-\033[93m pour tirer...\033[0m")
            input()
            if len(Roulette_Russe_barillet) == 0:
                Roulette_Russe_barillet = [False, False, False, False, False, True]
                random.shuffle(Roulette_Russe_barillet)
            Roulette_Russe_tir = Roulette_Russe_barillet.pop()
            if Roulette_Russe_tir:
                cl()
                print("\033[95m--- VOTRE TOUR ---\033[0m")
                pause(0.1)
                print("\n\n\033[91m*BANG!*, vous êtes MORT...\033[0m")
                pause(1.5)
                Roulette_Russe_humain = False
                break
            else:
                cl()
                print(random.choice(Roulette_Russe_script_humain_survie))
                print(f"\n\033[94mIl reste {len(Roulette_Russe_barillet)} chambres à tirer\033[0m")
                pause(5)
                print("\033[95m--- VOTRE TOUR ---\033[0m")
                print("\n\033[93mPressez ENTRÉE pour donner le pistolet au robot.\033[0m")
                input()
        if Roulette_Russe_humain:
            cl()
            print("\033[91mBravo ! Vous avez survécu à cette partie !\033[0m")
        else:
            cl()
        while True:
            cl()
            print("\n\n\033[93mTapez \033[32m-1-\033[93m pour rejouer ou \033[92m-2-\033[33m pour retourner au menu.\033[0m")
            try:
                choix_retour_menu = int(input("\n\033[33m->\033[0m"))
            except ValueError:
                print("\033[0;41mSaisi invalide, veuillez saisir un nombre entre 1 et 2.\033[0m")
                pause(1.5)
                continue
            if choix_retour_menu in [1,2]:
                break
        Roulette_Russe_end = choix_retour_menu != 1

def roulette_russe_multijoueur_regle():
    print("\033[91m========== RÈGLES DE LA ROULETTE RUSSE MULTIJOUEURS ==========\033[0m")
    print("""\033[95m
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
    input("\033[93mAppuyez sur \033[92m-ENTRÉE-\033[33m pour continuer.\033[0m")

def roulette_russe_multijoueur():
    barre_de_chargement(40, 0.03)
    joueurs_r_r = []
    cl()
    roulette_russe_multijoueur_regle()
    while True:
        cl()
        print("\033[93mCombien de joueurs êtes-vous ?\033[0m")
        try:
            nbr_de_joueur = int(input("\n\033[93m->\033[0m"))
        except ValueError:
            print("\033[0;41mSaisi invalide, veuillez saisir un nombre.\033[0m")
            pause(2)
            continue
        if nbr_de_joueur > 1:
            break
        else:
            print("\033[0;41mVous devez être plus de 1 joueur à participer.\033[0m")
            pause(2)
    for e in range(nbr_de_joueur):
        joueurs_r_r.append(input(f"\033[93mJoueur {e + 1}, choisissez votre pseudo : \033[0m"))
    while len(joueurs_r_r) > 1:
        roulette_russe_multijoueur_barillet = [True, False, False, False, False, False]
        random.shuffle(roulette_russe_multijoueur_barillet)

        for joueur_index in range(len(joueurs_r_r)):
            cl()
            joueur = joueurs_r_r[joueur_index]
            print(f"\033[96m{joueur}, à vous de connaître votre destin.\033[0m")
            print("\n\033[93mPour tirer, pressez \033[92m-ENTRÉE-\033[93m\033[0m")
            input()

            if len(roulette_russe_multijoueur_barillet) == 0:
                roulette_russe_multijoueur_barillet = [True, False, False, False, False, False]
                random.shuffle(roulette_russe_multijoueur_barillet)

            tir = roulette_russe_multijoueur_barillet.pop()
            if tir:
                print(f"\033[91m{joueur}, vous êtes mort.\033[0m")
                joueurs_r_r.pop(joueur_index)
                pause(1.5)
                break
            else:
                print(f"\033[95m{joueur}, vous êtes encore en vie.\033[0m")
                pause(1.2)

def logo_pile_ou_face():
    print("\033[91m======================================")
    print("==========\033[93m PILE  OU  FACE \033[91m============")
    print("======================================\033[0m")

def pile_ou_face_regle():
    print("""\n\033[95m
Bienvenue dans le Pile ou Face Casino !

1. Vous commencez la partie avec 100 jetons.
2. À chaque tour, vous jouez contre le robot.
3. Vous choisissez combien de jetons vous souhaitez miser.
4. Vous choisissez Pile ou Face.
5. Le robot lance la pièce :
    - Si vous devinez correctement, vous gagnez la mise du robot.
    - Si vous vous trompez, vous perdez votre mise.
6. Le jeu continue tant que vous avez des jetons et souhaitez jouer.
7. Si vous n'avez plus de jetons, vous avez perdu.
8. Après chaque partie, possibilité de rejouer ou de retourner au menu.

Bonne chance et que la chance soit avec vous !
    """)
    input("\033[93mPressez \033[92m-ENTRÉE-\033[93m pour continuer.\033[0m")

def pile_ou_face():
    tour = 0
    barre_de_chargement(40, 0.03)
    cl()
    pile_ou_face_regle()
    cl()
    print("\033[95mVous commencez avec une cagnotte de \033[96m100\033[95m jetons.\033[0m")
    input("\n\033[93mPressez \033[92m-ENTRÉE-\033[93m pour continuer.")
    cl()
    cagnotte = 100
    while cagnotte > 0:
        cl()
        logo_pile_ou_face()
        if tour > 0:
            choix = input("\033[93mSaisissez \033[92m-1-\033[93m si vous voulez continuer a jouer ou \033[92m-2-\033[93m pour retourner au menu.")
            if choix == "1":
                cl()
            elif choix == "2":
                break
            else:
                cl()
        while True:
            cl()
            logo_pile_ou_face()
            print(f"\n\033[93mCombien pariez vous sur cette partie ? \033[95m(cagnotte actuelle : \033[96m{cagnotte}\033[95m)\033[0m")
            try:
                pari = int(input("\n\033[93m->\033[0m"))
            except ValueError:
                print("\n\033[0;41mSasi invalide, veuillez saisir un nombre.\033[0m")
                pause(1.2)
                continue
            if pari > cagnotte:
                print(f"\n\033[0;41mVous ne pouvez pas parier plus que le contenue de votre cagnotte. (cagnotte actuelle : {cagnotte})\033[0m")
                pause(2)
            elif pari < 0:
                print(f"\n\033[0;41mVous ne pouvez pas parier un nombre plus petit que 0")
                pause(1.2)
            else:
                break
        cl()
        logo_pile_ou_face()
        pari_adverse = random.randint(1, 200)
        print(f"\n\033[95mVotre adversaire a parié \033[96m{pari_adverse}\033[0m")
        input("\n\033[93mPressez \033[92m-ENTRÉE-\033[93m pour commencer la partie.\033[0m")
        cl()
        logo_pile_ou_face()
        while True:
            cl()
            logo_pile_ou_face()
            try:
                pileouface = int(input("\n\033[93mSaisissez \033[92m-1-\033[93m pour pariez sur pile ou \033[92m-2-\033[93m pour pariez sur face.\n\n->\033[0m"))
            except ValueError:
                print("\n\033[0;41mSaisi invaide, veuillez saisir 1 ou 2.\033[0m")
                pause(1.2)
                continue
            if pileouface not in [1, 2]:
                print("\n\033[0;41mSaisi invaide, veuillez saisir 1 ou 2.\033[0m")
                pause(1.2)
                continue
            else:
                break
        piece = random.randint(1, 2)
        if piece == pileouface:
            cl()
            logo_pile_ou_face()
            print("\n\033[91m-BRAVO- vous avez gagné la partie !")
            print(f"\n\033[95mVous avez gagné \033[96m{pari_adverse}\033[95m jetons !")
            cagnotte += pari_adverse
            print(f"Votre cagnotte actuelle s'élève à \033[96m{cagnotte}\033[95m jetons !\033[0m")
            input("\033[93mPressez \033[92m-ENTRÉE-\033[93m pour continuer.\033[0m")
        else:
            cl()
            logo_pile_ou_face()
            print(f"\n\033[91m-PERDU-, vous perdez {pari} jetons.")
            cagnotte -= pari
            input("\n\033[93mPressez \033[92m-ENTRÉE-\033[93m pour continuer.")
        tour += 1
    if cagnotte <= 0:
        cl()
        logo_pile_ou_face()
        print("\n\033[95mDommage, vous aurez peut-être plus de chance la prochaine fois !\033[0m")
        pause(2)
    else:
        pass

def chargement():
    cl()
    init_modules()
    cl()
    barre_de_chargement(40, 0.07)
    cl()
    error_recap()
    cl()
    pause(0.5)
    animation_acceuil()
    cl()

def jeu():
    chargement()
    didactitiel()
    menu_principal()

jeu()