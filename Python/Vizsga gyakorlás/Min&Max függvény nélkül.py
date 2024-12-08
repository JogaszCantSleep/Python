import random

L1 = [] 

print("Lista legkisebb és legnagyobb elemének kiírása függvények nélkül!")
print()

mennyiseg = int(input("Hány elemű legyen a lista? "))
print()

valasztas = input("Random számok legyenek vagy te írod be? (random/én) ")
print()

if valasztas == "én":
    print("A számok:")
    print()
    for i in range(mennyiseg):
        szam = int(input())
        print()
        L1.append(szam)

if valasztas == "random":
    print("Mettől meddig legyenek a random számok?")
    print()
    tol = int(input("Ettől: "))
    print()
    ig = int(input("Eddig: "))
    print()
    for i in range(mennyiseg):
        szam = random.randint(tol, ig)
        L1.append(szam)
    for i in range(mennyiseg):
        print(i + 1, ". Szám: ", L1[i])
        print()

print("Függvény nélkül:")
print()

min = L1[1]

for i in range(len(L1)):
    if L1[i] < min:
        min = L1[i]
        
max = L1[1]

for i in range(len(L1)):
    if L1[i] > max:
        max = L1[i]

print("--------------------------")
print("Lista legkisebb eleme:", min)
print("--------------------------")
print("Lista legnagyobb eleme:", max)
print("--------------------------")

#-----------------------------------------------------------
