import random

def jatek():
    pen = 0
    pbot = 0
    while pen != 3 and pbot != 3:
        en = int(input("Kő (1), Papír (2), Olló (3)!"))
        bot = random.randint(1,3)
        if en == 1:
            if bot == 1:
                print("Te: Kő")
                print("Bot: Kő")
                print("Döntetlen!")
            elif bot == 2:
                print("Te: Kő")
                print("Bot: Papír")
                print("A bot nyert!")
                pbot += 1
            elif bot == 3:
                print("Te: Kő")
                print("Bot: Olló")
                print("Nyertél!")
                pen += 1
        elif en == 2:
            if bot == 1:
                print("Te: Papír")
                print("Bot: Kő")
                print("Nyertél!")
                pen += 1
            elif bot == 2:
                print("Te: Papír")
                print("Bot: Papír")
                print("Döntetlen!")
            elif bot == 3:
                print("Te: Papír")
                print("Bot: Olló")
                print("A bot nyert!")
                pbot += 1
        elif en == 3:
            if bot == 1:
                print("Te: Olló")
                print("Bot: Kő")
                print("A bot nyert!")
                pbot += 1
            elif bot == 2:
                print("Te: Olló")
                print("Bot: Papír")
                print("Nyertél!")
                pen += 1
            elif bot == 3:
                print("Te: Olló")
                print("Bot: Olló")
                print("Döntetlen!")
    print("Végeredmény:")
    print("Bot:", pbot)
    print("Te:", pen)
    q = input("Szeretnéd folytatni? (y/n)")
    if q == "y":
        jatek()
    elif q == "n":
        exit()

jatek()

