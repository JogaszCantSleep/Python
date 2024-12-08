import random

def Szám(szam):
    db = 0
    for i in range(len(L1)):
        if szam == L1[i]:
            db += 1
    return db

L1 = []
for i in range(30):
    L1.append(random.randint(1,10))

print("A lista elemei:", L1)

szam = int(input("Adj meg egy számot 1 és 10 között!"))

eredmeny = str(Szám(szam)) + "db ezzel egyenlő szám van a listában!"

print(eredmeny)
