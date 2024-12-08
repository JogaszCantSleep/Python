import random

L1 = []

for i in range(1000):
    L1.append(random.randint(0,24))

print(max(L1), ",", min(L1))
