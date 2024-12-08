import random

menet = int(input("Hányszor fusson le? "))

elso = 0
masodik = 0

for i in range(menet):
    if random.randint(1, 2) == 1:
        elso += 1
    else:
        masodik += 1

print(elso)
print(masodik)
