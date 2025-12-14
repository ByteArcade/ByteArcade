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

download_saves()
print(data)
upload_saves()