import random

print("Teszteljük, mennyire kevés vagy sok esély a 1%!")
szam = int(input("Hányszor fusson le? "))

L1 = []

Fc = 0
Mp = 0

for i in range(szam):
    r1 = random.randint(1,100)
    r2 = random.randint(1,100)

    proba = 1
    
    while r1 != r2:
        r1 = random.randint(1,100)
        r2 = random.randint(1,100)
        proba += 1
    L1.append(proba)
    ForM = random.randint(1,2)
    if ForM == 1:
        Fc += 1
    if ForM == 2:
        Mp += 1

összp = 0

for i in range(len(L1)):
    összp += L1[i]

atlag = összp / len(L1)

print()
print("========================================================================")
print("A sikerünk átlaga:", atlag, "db próbálkozás 1 sikerhez!")
print("========================================================================")
print("Az", szam, "db sikeres szerencséhez", összp, "db próbálkozás volt szükséges!")
print("========================================================================")
print("A legszerencsésebb esetünk:",min(L1)  , "próbálkozás 1 sikerhez!")
print("========================================================================")
print("A legszerencsétlenebb esetünk:",max(L1)  , "próbálkozás 1 sikerhez!")
print("Ez", 100 / max(L1), "% szerencsével egyenlő 1 sikerhez!")
print("========================================================================")
print(szam, "próbálkozás alatt", Fc, "Fastclock, és", Mp, "Megaphone gyűlt!")
print("========================================================================")
