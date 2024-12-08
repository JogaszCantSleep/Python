import random

class jatekok():
    def menu():
        print()
        print("======")
        print("Főmenü")
        print("=====================")
        print("(1). Kő, Papír, Olló!")
        print("(2). Találd ki!")
        print("(3). Kilépés!")
        print("=====================")
        print()
        menu = input("Szia, mit szeretnél csinálni? ")
        while int(menu) < 1 or int(menu) > 3:
            print("Helytelen!")
            menu = input("Mit szeretnél csinálni? ")
        print()
        if menu == "1":
            jatekok.kopapirollo()
        if menu == "2":
            jatekok.talaldki()
        if menu == "3":
            jatekok.kilep()
            
    
    def kopapirollo():
        pen = 0
        pbot = 0
        while pen != 3 and pbot != 3:
            print("=============================")
            print("Kő (1), Papír (2), Olló (3)!")
            print("=============================")
            print()
            en = int(input("Választásod: "))
            print()
            bot = random.randint(1,3)
            if en == 1:
                if bot == 1:
                    print("============")
                    print("Te: Kő")
                    print("Bot: Kő")
                    print("Döntetlen!")
                    print("============")
                    print()
                elif bot == 2:
                    print("============")
                    print("Te: Kő")
                    print("Bot: Papír")
                    print("A bot nyert!")
                    print("============")
                    print()
                    pbot += 1
                elif bot == 3:
                    print("============")
                    print("Te: Kő")
                    print("Bot: Olló")
                    print("Nyertél!")
                    print("============")
                    print()
                    pen += 1
            elif en == 2:
                if bot == 1:
                    print("============")
                    print("Te: Papír")
                    print("Bot: Kő")
                    print("Nyertél!")
                    print("============")
                    print()
                    pen += 1
                elif bot == 2:
                    print("============")
                    print("Te: Papír")
                    print("Bot: Papír")
                    print("Döntetlen!")
                    print("============")
                    print()
                elif bot == 3:
                    print("============")
                    print("Te: Papír")
                    print("Bot: Olló")
                    print("A bot nyert!")
                    print("============")
                    print()
                    pbot += 1
            elif en == 3:
                if bot == 1:
                    print("============")
                    print("Te: Olló")
                    print("Bot: Kő")
                    print("A bot nyert!")
                    print("============")
                    print()
                    pbot += 1
                elif bot == 2:
                    print("============")
                    print("Te: Olló")
                    print("Bot: Papír")
                    print("Nyertél!")
                    print("============")
                    print()
                    pen += 1
                elif bot == 3:
                    print("============")
                    print("Te: Olló")
                    print("Bot: Olló")
                    print("Döntetlen!")
                    print("============")
                    print()
        print("============")
        print("Végeredmény:")
        print("Bot:", pbot)
        print("Te:", pen)
        print("============")
        print()
        q1 = input("Szeretnél még játszani? (y/n)")
        while q1 != "y" or q1 != "n":
            print("Helytelen!")
            q1 = input("Szeretnél még játszani? (y/n) ")
        if q1 == "y":
            jatekok.kopapirollo()
        else:
            jatekok.menu()

    def talaldki():
        print("==================================================")
        print("Üdvözöllek a Találd Ki-ben!")
        print("Találd ki melyik számra gondoltam 1 és 100 között!")
        print("5 lehetőséged lesz eltalálni a helyes számot!")
        print("==================================================")
        print()
        print("Kapsz 2 segítséget!")
        y = random.randint(1, 100)
        if y >= 50:
            print("===============================================")
            print("A te számod nagyobb mint 50, vagy egyenlő vele!")
            print("és...")
        else:
            print("===============================================")
            print("A te számod kisebb, mint 50, vagy egyenlő vele!")
            print("és...")
        if y % 2 == 0:
            print("A számod páros!")
            print("===============================================")
            print()
        else:
            print("A számod páratlan!")
            print("===============================================")
            print()
        for i in range(5):
            x = int(input("Találd ki, melyik számra gondoltam! "))
            while x < 1 or x > 100:
                print("Helytelen!")
                x = int(input("Találd ki, melyik számra gondoltam! "))
                print()
            if x == y:
                print("Ügyes vagy, kitaláltad! A számod:", y, "volt!")
                print()
                q1 = input("Szeretnél még játszani? (y/n)")
                if q1 == "y":
                    jatekok.talaldki()
                else:
                    jatekok.menu()
            elif x > y:
                print("Sajnos nem talált, kisebbet kellett volna tippelned!")
                print()
            elif x < y:
                print("Sajnos nem talált, nagyobbat kellett volna tippelned!")
                print()
        print("Sajnos nem sikerült kitalálnod... A számod", y, "volt")
        q1 = input("Szeretnél még játszani? (y/n) ")
        while q1 != "y" or q1 != "n":
            print("Helytelen!")
            q1 = input("Szeretnél még játszani? (y/n) ")
        if q1 == "y":
            jatekok.talaldki()
        else:
            jatekok.menu()

    def kilep():
        q1 = input("Teljesen biztos, hogy ki szeretne lépni?(y/n) ")
        if q1 == "y":
            print()
            print("========")
            print("Viszlát!")
            print("========")
            exit()
        elif q1 == "n":
            jatekok.menu()
        else:
            print("=================")
            print("Helytelen Válasz!")
            print("=================")
            print()
            jatekok.menu()

jatekok.menu()
