from randomdfv import list1
import random
from time import sleep
import os

# created by Avijit roy
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
 
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def situation(dj):
    if dj == 1:
        print("guess the word:...!")
        print("you have", x, "chance: ")
        print("   +---+")
        print("       |")
        print("       |")
        print("       |")
        print(" , ,====")
    elif dj == 2:
        print("guess the word:.....!")
        print("you have", x, "chance left: ")
        print("   +---+")
        print("   O   |")
        print("       |")
        print("       |")
        print(" , ,====")
    elif dj == 3:
        print("guess the word:.....!")
        print("you have", x, "chance left: ")
        print("   +---+")
        print("   O   |")
        print("   |   |")
        print("       |")
        print(" , ,====")
    elif dj == 4:
        print("guess the word:......!")
        print("you have", x, "chance left: ")
        print("   +---+")
        print("   O   |")
        print("   |\  |")
        print("       |")
        print(" , ,====")
    elif dj == 5:
        print("guess the word:.....!")
        print("you have", x, "chance left: ")
        print("   +---+")
        print("   O   |")
        print("  /|\  |")
        print("       |")
        print(" , ,====")
    elif dj == 6:
        print("guess the word:.....!")
        print("you have last chance: ")
        print("   +---+")
        print("   O   |")
        print("  /|\  |")
        print("  /    |")
        print(" , ,====")
    elif dj == 7:
        print("   +---+")
        print("   O   |")
        print("  /|\  |")
        print("  / \  |")
        print(" , ,====")
        print("you lost: \n\tthe word was", word)


td = "y"
while td.lower() == "y":
    word = random.choice(list1)
    m = 1
    x = 6
    do = []
    doi = []
    dis = []
    for k in range(len(word)):
        dis.append("_")
    print(dis)

    situation(m)
    for i in word:
        doi.append(i)
    print("_"*len(do), "\n")
    while m <= 6:
        a = input("enter the word: ")
        if a in doi and a not in do:
            dis[word.index(a)] = a
            print(dis)
            situation(m)
            do.append(a)
            if sorted(doi) == sorted(do):
                print("you win...")
                print("\tthe word was", word)
                m = 7
        else:
            print(dis)            
            print("wrong answer....!")
            m += 1
            x -= 1
            situation(m)
    clear()
    sleep(5)
    td = input("wanna play again y/n:  ")
else:
    exit()
