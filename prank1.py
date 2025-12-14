import time
import random
import os
import platform


def cl():
    os.system('cls' if os.name == 'nt' else 'clear')

def pause(temps):
    time.sleep(temps)

def init():
    for e in range(5):
        cl()
        print("\033[95mInitialisation du programme", end="", flush=True)
        for t in range(3):
            print(".", end="", flush=True)
            time.sleep(random.uniform(0.1, 1))

def tentative_entree():
    cl()
    text = "\033[91mtentative d'entrée dans le système : "
    entree = 0
    for i in range(random.randint(1000, 2500)):
        print(text, "\033[96m", i)
        time.sleep(random.uniform(0.00001, 0.015))
        entree += 1
    print(f"Entree dans le systeme à la tentative {entree}")

def lecture_sys():
    cl()
    barres = ["|", "/", "-", "\\"]
    for u in range(random.randint(10, 50)):
        for y in range(len(barres)):
            cl()
            print("\033[92mLecture du système", barres[y])
            time.sleep(0.1)
    cl()

def infos_sys():
    cl()
    system_name = platform.system()
    system_version = platform.version()
    full_info = platform.platform()

    print(f"\033[95mSystème : {system_name}")
    print(f"Version : {system_version}")
    print(f"Info complète : {full_info}")


init()
tentative_entree()
lecture_sys()
infos_sys()