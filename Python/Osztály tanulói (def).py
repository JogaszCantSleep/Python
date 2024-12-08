class tanulok():
    def __init__(self, vezn, kern, szev, iszam, oszt):
        self.vezn = vezn
        self.kern = kern
        self.szev = szev
        self.iszam = iszam
        self.oszt = oszt

    def set_vezn(self, vezn):
        self.vezn = vezn

    def set_kern(self, kern):
        self.kern = kern

    def set_szev(self, szev):
        self.szev = szev

    def set_iszam(self, iszam):
        self.iszam = iszam

    def set_oszt(self, oszt):
        self.oszt = oszt

    def kiir(self):
        print("=========================")
        print("Vezetéknév:   ", self.vezn)
        print("Keresztnév:   ", self.kern)
        print("Születési év: ", self.szev)
        print("Irányítószám: ", self.iszam)
        print("Osztály:      ", self.oszt)
        print("=========================")
        print()
    
    def menu():
        print("======")
        print("Főmenü")
        print("================")
        print("(1). Adatbevitel")
        print("(2). Adatkiírás")
        print("(3). Keresés")
        print("(4). Módosítás")
        print("(5). Törlés")
        print("(6). Kilépés")
        print("================")
        print()
        menu = input("Mit szeretne tenni?: ")
        print()
        if menu == "1":
            tanulok.adatb()
        elif menu == "2":
            tanulok.adatk()
        elif menu == "3":
            tanulok.keres()
        elif menu == "4":
            tanulok.modos()
        elif menu == "5":
            tanulok.torol()
        elif menu == "6":
            tanulok.kilep()
        else:
            print("===A Főmenü menüpontjaiból válasszon!===")
            print()
            tanulok.menu()

    def adatb():
        q1 = int(input("Hány nevet szeretne bevinni? "))
        print()
        for i in range(q1):
            print(i + 1, ". Tanuló:")
            print("===Adja meg a következő adatokat a bevitelhez!===")
            vezn = input("Vezetéknév:    ")
            kern = input("Keresztnév:    ")
            szev = input("Születési év:  ")
            iszam = input("Irányítószám:  ")
            oszt = input("Osztály:       ")
            print()
            L1.append(tanulok(vezn, kern, szev, iszam, oszt))
        q2 = input("Szeretne még nevet bevinni?(y/n) ")
        print()
        if q2 == "y":
            tanulok.adatb()
        elif q2 == "n":
            tanulok.menu()
        else:
            print("=================")
            print("Helytelen Válasz!")
            print("=================")
            print()
            tanulok.menu()
            

    def adatk():
        if len(L1) == 0:
            print("===Még egy név sincs a rendszerben!===")
            print()
            tanulok.menu()
        for i in range(len(L1)):
            L1[i].kiir()
            if i + 1 == len(L1):
                print("===Összesen", len(L1), "tanuló===")
                print()
                tanulok.menu()

    def keres():
        if len(L1) == 0:
            print("===Még egy név sincs a rendszerben!===")
            print()
            tanulok.menu()
        print("(1). Név")
        print("(2). Születési év")
        print("(3). Irányítószám")
        print("(4). Osztály")
        print()
        q2 = input("Mi alapján szeretne keresni? ")
        print()
        if q2 == "1":
            tanulok.keresnev()
        elif q2 == "2":
            tanulok.keresszev()
        elif q2 == "3":
            tanulok.keresiszam()
        elif q2 == "4":
            tanulok.keresoszt()
        else:
            print("=================")
            print("Helytelen Válasz!")
            print("=================")
            print()
            tanulok.menu()
                
    def keresnev():
        q1 = input("Vezetéknév: ")
        q2 = input("Keresztnév: ")
        print()
        talalt = "nem"
        for i in range(len(L1)):
            if q1 == L1[i].vezn and q2 == L1[i].kern:
                print(i + 1, ". Tanuló:")
                L1[i].kiir()
                talalt = "igen"
                if i + 1 == len(L1):
                    print("===Összesen", len(L1), "tanuló===")
                    print()
                    tanulok.menu()
        if talalt == "nem":
            print("Ilyen névvel nem szerepel tanuló a rendszerben!")
            print()
            q3 = input("Újrapróbálja?(y/n) ")
            print()
            if q3 == "y":
                tanulok.keres()
            elif q3 == "n":
                tanulok.menu()
            else:
                print("=================")
                print("Helytelen Válasz!")
                print("=================")
                print()
                tanulok.menu()

    def keresszev():
        q1 = input("Születési év: ")
        print()
        talalt = "nem"
        for i in range(len(L1)):
            if q1 == L1[i].szev:
                print(i + 1, ". Tanuló:")
                L1[i].kiir()
                talalt = "igen"
                if i + 1 == len(L1):
                    print("===Összesen", len(L1), "tanuló===")
                    print()
                    tanulok.menu()
        if talalt == "nem":
            print("Ilyen születési évvel nem szerepel tanuló a rendszerben!")
            print()
            q3 = input("Újrapróbálja?(y/n) ")
            print()
            if q3 == "y":
                tanulok.keres()
            elif q3 == "n":
                tanulok.menu()
            else:
                print("=================")
                print("Helytelen Válasz!")
                print("=================")
                print()
                tanulok.menu()

    def keresiszam():
        q1 = input("Irányítószám: ")
        print()
        talalt = "nem"
        for i in range(len(L1)):
            if q1 == L1[i].iszam:
                print(i + 1, ". Tanuló:")
                L1[i].kiir()
                talalt = "igen"
                if i + 1 == len(L1):
                    print("===Összesen", len(L1), "tanuló===")
                    print()
                    tanulok.menu()
        if talalt == "nem":
            print("Ilyen irányítószámmal nem szerepel tanuló a rendszerben!")
            print()
            q3 = input("Újrapróbálja?(y/n) ")
            print()
            if q3 == "y":
                tanulok.keres()
            elif q3 == "n":
                tanulok.menu()
            else:
                print("=================")
                print("Helytelen Válasz!")
                print("=================")
                print()
                tanulok.menu()

    def keresoszt():
        print("============================================")
        print("Kérem az osztályt nagybetűvel írja pl: 10B")
        print("Ha a keresni kívánt személy már elballagott,\nírja be: Ballagott.")
        print("============================================")
        print()
        q1 = input("Osztály: ")
        print()
        talalt = "nem"
        for i in range(len(L1)):
            if q1 == L1[i].oszt:
                print(i + 1, ". Tanuló:")
                L1[i].kiir()
                talalt = "igen"
                if i + 1 == len(L1):
                    print("===Összesen", len(L1), "tanuló===")
                    tanulok.menu()
        if talalt == "nem":
            print("Ilyen osztályú tanuló nem szerepel a rendszerben!")
            print()
            q3 = input("Újrapróbálja?(y/n) ")
            print()
            if q3 == "y":
                tanulok.keres()
            elif q3 == "n":
                tanulok.menu()
            else:
                print("=================")
                print("Helytelen Válasz!")
                print("=================")
                print()
                tanulok.menu()

    def modos():
        k = 1
        L2 = []
        if len(L1) == 0:
            print("===Még egy név sincs a rendszerben!===")
            print()
            tanulok.menu()
        print("Ki adatait szeretné módosítani? ")
        print()
        q1 = input("Vezetéknév: ")
        q2 = input("Keresztnév: ")
        print()
        talalt = 0
        for i in range(len(L1)):
            if q1 == L1[i].vezn and q2 == L1[i].kern:
                print(k , ". Tanuló")
                k = k + 1
                L1[i].kiir()
                L2.append(i)
                talalt = talalt + 1
        print("===", len(L2), "tanuló található ezzel a névvel!===")
        print()
        if talalt == 1:
            print("(1). Vezetéknév")
            print("(2). Keresztnév")
            print("(3). Születési év")
            print("(4). Irányítószám")
            print("(5). Osztály")
            print()        
            q3 = int(input("Melyik adatot kívánja változtatni? "))
            print()
            if q3 == 1:
                L1[L2[0]].set_vezn(input("Mire szeretné változtatni? "))
                print()
                print("=====")
                print("Kész!")
                print("=====")
                print()
                tanulok.menu()
            elif q3 == 2:
                L1[L2[0]].set_kern(input("Mire szeretné változtatni? "))
                print()
                print("=====")
                print("Kész!")
                print("=====")
                print()
                tanulok.menu()
            elif q3 == 3:
                L1[L2[0]].set_szev(input("Mire szeretné változtatni? "))
                print()
                print("=====")
                print("Kész!")
                print("=====")
                print()
                tanulok.menu()
            elif q3 == 4:
                L1[L2[0]].set_iszam(input("Mire szeretné változtatni? "))
                print()
                print("=====")
                print("Kész!")
                print("=====")
                print()
                tanulok.menu()
            elif q3 == 5:
                L1[L2[0]].set_oszt(input("Mire szeretné változtatni? "))
                print()
                print("=====")
                print("Kész!")
                print("=====")
                print()
                tanulok.menu()
            else:
                tanulok.menu()
        elif talalt > 1:
            q4 = int(input("Hanyadik tanuló adatait kívánja módosítani? "))
            print()
            L1[L2[q4 - 1]].kiir()
            print("(1). Vezetéknév")
            print("(2). Keresztnév")
            print("(3). Születési év")
            print("(4). Irányítószám")
            print("(5). Osztály")
            print()
            q3 = int(input("Melyik adatot kívánja változtatni? "))
            print()
            if q3 == 1:
                L1[L2[q4 - 1]].set_vezn(input("Mire szeretné változtatni? "))
                print()
                print("=====")
                print("Kész!")
                print("=====")
                print()
                tanulok.menu()
            elif q3 == 2:
                L1[L2[q4 - 1]].set_kern(input("Mire szeretné változtatni? "))
                print()
                print("=====")
                print("Kész!")
                print("=====")
                print()
                tanulok.menu()
            elif q3 == 3:
                L1[L2[q4 - 1]].set_szev(input("Mire szeretné változtatni? "))
                print()
                print("=====")
                print("Kész!")
                print("=====")
                print()
                tanulok.menu()
            elif q3 == 4:
                L1[L2[q4 - 1]].set_iszam(input("Mire szeretné változtatni? "))
                print()
                print("=====")
                print("Kész!")
                print("=====")
                print()
                tanulok.menu()
            elif q3 == 5:
                L1[L2[q4 - 1]].set_oszt(input("Mire szeretné változtatni? "))
                print()
                print("=====")
                print("Kész!")
                print("=====")
                print()
                tanulok.menu()
            else:
                tanulok.menu()
        else:
            print("===Nincs ilyen név a rendszerben!===")
            print()
            tanulok.menu()

    def torol():
        k = 1
        L3 = []
        if len(L1) == 0:
            print("===Még egy név sincs a rendszerben!===")
            print()
            tanulok.menu()
        print("Kit szeretne törölni a rendszerből? ")
        print()
        q1 = input("Vezetéknév: ")
        q2 = input("Keresztnév: ")
        print()
        talalt = 0
        for i in range(len(L1)):
            if q1 == L1[i].vezn and q2 == L1[i].kern:
                print(k , ". Tanuló")
                k = k + 1
                L1[i].kiir()
                L3.append(i)
                talalt = talalt + 1
        print("===", len(L3), "tanuló található ezzel a névvel!===")
        print()
        if talalt == 1:       
            q3 = input("Teljesen biztos, hogy törölni akarja ezt a tanulót?(y/n) ")
            print()
            if q3 == "y":
                L1.pop(L3[0])
                print("=====")
                print("Kész!")
                print("=====")
                print()
                tanulok.menu()
            elif q3 == "n":
                tanulok.menu()
            else:
                print("=================")
                print("Helytelen Válasz!")
                print("=================")
                print()
                tanulok.menu()
        elif talalt > 1:
            q4 = int(input("Hanyadik tanulót kívánja törölni? "))
            print()
            L1[L3[q4 - 1]].kiir()
            q5 = input("Teljesen biztos, hogy törölni akarja ezt a tanulót?(y/n) ")
            print()
            if q5 == "y":
                L1.pop(L3[q4 - 1])
                print("=====")
                print("Kész!")
                print("=====")
                print()
                tanulok.menu()
            elif q5 == "n":
                tanulok.menu()
            else:
                print("=================")
                print("Helytelen Válasz!")
                print("=================")
                print()
                tanulok.menu()
        else:
            print("===Nincs ilyen név a rendszerben!===")
            print()
            tanulok.menu()
        
    def kilep():
        q1 = input("Teljesen biztos, hogy ki szeretne lépni?(y/n) ")
        print()
        if q1 == "y":
            print("========")
            print("Viszlát!")
            print("========")
            exit()
        elif q1 == "n":
            tanulok.menu()
        else:
            print("=================")
            print("Helytelen Válasz!")
            print("=================")
            print()
            tanulok.menu()

L1 = []

print()

tanulok.menu()
