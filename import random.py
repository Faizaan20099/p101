import random

q = str(input("do you want to roll a dice? y for yes and n for no: "))

while q == "y":
    no = random.randint(1,6)
    if no == 1:
        print("[-----]")
        print("[-----]")
        print("[--0--]")
        print("[-----]")
        print("[-----]")
    if no == 2:
        print("[-----]")
        print("[---0-]")
        print("[-----]")
        print("[-0---]")
        print("[-----]")
    if no == 3:
        print("[-----]")
        print("[---0-]")
        print("[--0--]")
        print("[-0---]")
        print("[-----]")
    if no == 4:
        print("[-----]")
        print("[-0-0-]")
        print("[-----]")
        print("[-0-0-]")
        print("[-----]")
    if no == 5:
        print("[-----]")
        print("[-0-0-]")
        print("[--0--]")
        print("[-0-0-]")
        print("[-----]")
    if no == 6:
        print("[-----]")
        print("[-0-0-]")
        print("[-0-0-]")
        print("[-0-0-]")
        print("[-----]")
    q = input("do you want to roll a dice again? y for yes and n for no: ")