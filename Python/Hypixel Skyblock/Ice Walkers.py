import random

kills = 0
h = 0
c = 0
l = 0
b = 0
g_c = 0

for i in range(1000000):
    kills += 1
    dollar = kills * 8
    combat_exp = kills * 40
    r1 = random.randint(1, 400)
    r2 = random.randint(1, 400)
    if r1 == r2:
        r1 = random.randint(1, 4)
        if r1 == 1:
            h += 1
        if r1 == 2:
            c += 1
        if r1 == 3:
            l += 1
        if r1 == 4:
            b += 1
    if r1 != r2:
        r1 = random.randint(1, 200)
        r2 = random.randint(1, 200)
        if r1 == r2:
            g_c += 1

print(h, c, l, b, g_c)
print(kills)
print(dollar)
print(combat_exp)
