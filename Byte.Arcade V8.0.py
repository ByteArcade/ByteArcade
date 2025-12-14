data = {}
op_functions = {
    "random": True,
    "time": True,
    "sys": True,
    "os": True,
    "json": True,
    "cl_os_line_jump" : 50,
    "ImportErrorRecap" : [],
    "InitErrorRecap" : []
}

try:
    import random
except Exception as e:
    op_functions["ImportErrorRecap"].append(f"Le mdoule 'random' n'a pas pus être importé : {e}")
    op_functions["random"] = False
try:
    import time
except Exception as e:
    op_functions["ImportErrorRecap"].append(f"Le mdoule 'time' n'a pas pus être importé : {e}")
    op_functions["time"] = False
try:
    import sys
except Exception as e:
    op_functions["ImportErrorRecap"].append(f"Le mdoule 'sys' n'a pas pus être importé : {e}")
    op_functions["sys"] = False
try:
    import os
except Exception as e:
    op_functions["ImportErrorRecap"].append(f"Le mdoule 'os' n'a pas pus être importé : {e}")
    op_functions["os"] = False
try:
    import json
except Exception as e:
    op_functions["ImportErrorRecap"].append(f"Le mdoule 'json' n'a pas pus être importé : {e}")
    op_functions["json"] = False

def init_modules():
    global op_functions
    try:
        random.randint(1, 2)
    except Exception as e:
        op_functions["InitErrorRecap"].append(f"Le mdoule 'random' a rencontré un problème : {e}")
        op_functions["random"] = False
    try:
        time.sleep(0.1)
    except Exception as e:
        op_functions["InitErrorRecap"].append(f"Le mdoule 'time' a rencontré un problème : {e}")
        op_functions["time"] = False
    try:
        sys.version
    except Exception as e:
        op_functions["InitErrorRecap"].append(f"Le mdoule 'sys' a rencontré un problème : {e}")
        op_functions["sys"] = False
    try:
        os.getcwd()
    except Exception as e:
        op_functions["InitErrorRecap"].append(f"Le mdoule 'os' a rencontré un problème : {e}")
        op_functions["os"] = False
    try:
        dumped = False
        loaded = False
        data_test = {}
        data_test = {"test" : 1}
        dumped = json.dumps(data_test)
        loaded = json.loads(dumped)
        if data_test != loaded:
            raise Exception("ModuleDoesntFunctionCorrectly")
    except Exception as e:
        op_functions["InitErrorRecap"].append(f"Le mdoule 'json' a rencontré un problème : {e}")
        op_functions["json"] = False

def import_errors_recap():
    if len(op_functions["ImportErrorRecap"]) > 0:
        for errors in op_functions["ImportErrorRecap"]:
            print("-", errors)
        input("\nPressez -ENTRÉE- pour continuer")
    else:
        pass

def init_error_recap():
    if len(op_functions["InitErrorRecap"]) > 0:
        for errors in op_functions["InitErrorRecap"]:
            print("-", errors)
        input("\nPressez -ENTRÉE- pour continuer")
    else:
        pass

def cl():
    if op_functions["os"] == True:
        os.system('cls' if os.name == 'nt' else 'clear')
    else:
        print("\n"*op_functions["cl_os_line_jump"])

def pause(temps):
    global op_functions
    if op_functions["time"] == True:
        time.sleep(temps)
    else:
        pass

def random_settings():
    global op_functions
    while True:
        cl()
        line_1 = "Tenter d'activer : -1-" if not op_functions["random"] else "Désactiver : -1-"
        random_status = "ACTIVÉ" if op_functions["random"] else "DÉSACTIVÉ"
        print(f"{line_1}\t\tRetour : -0-")
        print(f"\nStatus actuel : {random_status}")
        choix = input("\n\n->")
        if choix == "1":
            if op_functions["random"] == False:
                op_functions["random"] = True
                try:
                    import random
                    random.randint(1, 2)
                except Exception as e:
                    op_functions["random"] = False
                    print("Le module 'random' a rencontré un problème.")
                    pause(1.5)
            else:
                op_functions["random"] = False
        elif choix == "0":
            break
        else:
            print("Saisi invalide, veuillez reessayer.")
            pause(1.5)

def time_setting():
    global op_functions
    while True:
        cl()
        line_1 = "Tenter d'activer : -1-" if not op_functions["time"] else "Désactiver : -1-"
        time_status = "ACTIVÉ" if op_functions["time"] else "DÉSACTIVÉ"
        print(f"{line_1}\t\tRetour : -0-")
        print(f"\nStatus actuel : {time_status}")
        choix = input("\n\n->")
        if choix == "1":
            if op_functions["time"] == False:
                op_functions["time"] = True
                try:
                    import time
                    time.sleep(0.1)
                except Exception as e:
                    op_functions["time"] = False
                    print(f"Le mdodule 'time' n'a pas pu être importé : {e}")
                    time.sleep(1.5)
            else:
                op_functions["time"] = False
        elif choix == "0":
            break
        else:
            print("Saisi invalide, veuillez reessayer.")
            pause(1.5)

def os_settings():
    global op_functions
    while True:
        cl()
        line_1 = "Tenter d'activer : -1-" if not op_functions["os"] else "Désactiver : -1-"
        line_2 = "\t\tChanger le nombre de saut de ligne : -2-" if not op_functions["os"] else ""
        os_status = "ACTIVÉ" if op_functions["os"] else "DÉSACTIVÉ"
        print(f"{line_1}{line_2}\tRetour : -0-")
        print(f"\nStatus actuel : {os_status}")
        choix = input("\n->")
        if choix == "0":
            break
        elif choix == "1":
            if op_functions["os"] == False:
                op_functions["os"] = True
                try:
                    import os
                    os.getcwd()
                except Exception as e:
                    print(f"L'importation a échouée : {e}")
                    op_functions["os"] = False
                    pause(1.5)
                if op_functions["os"] == True:
                    try:
                        print(os.getcwd())
                    except Exception:
                        print("L'importation a échouée")
                        op_functions["os"] = False
                        pause(0.1)
            else:
                op_functions["os"] = False
        elif choix == "2":
            while True:
                cl()
                print(f"Nombre de sauts de ligne actuel : {op_functions["cl_os_line_jump"]}, Revenir : -0-")
                try:
                    choix = int(input("\n->"))
                except ValueError:
                    print("Saisi invalide, veuillez reessayer.")
                    pause(1.5)
                if choix > 0:
                    op_functions["cl_os_line_jump"] = choix
                    break
                elif choix == 0:
                    break
                else:
                    print("Saisi invalide veuillez reessayer.")
                    pause(1.5)
        else:
            print("Saisi invalide, veuillez reessayer.")
            pause(1.5)


def json_settings():
    global op_functions
    while True:
        cl()
        line_1 = "Tenter d'activer : -1-" if not op_functions["json"] else "Désactiver : -1-"
        json_status = "ACTIVÉ" if op_functions["json"] else "DÉSACTIVÉ"
        print(f"{line_1}\t\tRetour : -0-")
        print(f"\nStatus actuel : {json_status}")
        choix = input("\n\n->")
        if choix == "1":
            if op_functions["json"] == False:
                op_functions["json"] = True
                try:
                    import json
                    data_test = {"test" : 1}
                    dumped = False
                    loaded = False
                    dumped = json.dumps(data_test)
                    loaded = json.loads(dumped)
                    if loaded != data_test:
                        raise Exception("ModuleDoesntFunctionCorrectly")
                except Exception as e:
                    op_functions["json"] = False
                    print(f"L'importation a échoué : {e}")
                    pause(1.5)
            else:
                op_functions["json"] = False
        elif choix == "0":
            break
        else:
            print("Saisi incorrect, veuillez reessayer.")
            pause(1.5)

def download_saves():
    global data
    with open("sauvegardes.json", "r") as file:
        data = json.load(file)

def upload_saves():
    global data
    with open("sauvegardes.json", "w") as file:
        json.dump(data, file, indent=4)

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
            pass
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
            pass
        elif choix == "2":
            pass
        elif choix == "3":
            pass
        elif choix == "4":
            pass
        elif choix == "5":
            pass
        elif choix == "6":
            pass
        elif choix == "0":
            break
        else:
            print("Saisi invalide, veuillez reessayer.")

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
            os_settings()
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