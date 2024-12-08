import random

p = 0
o = 0
u = 0
y = 0
s = 0
w = 0
sup = 0

protector = []
old = []
unstable = []
young = []
strong = []
wise = []
superior = []

szamok = []

menetek = 0

while sup != 240:

    menetek += 1

    for i in range(25):
            szamok.append(i+1)
    
    for i in range(4):
            x = random.choice(szamok)
            protector.append(x)
            szamok.remove(x)
           
    for i in range(4):
            x = random.choice(szamok)
            old.append(x)
            szamok.remove(x)
  
    for i in range(4):
            x = random.choice(szamok)
            unstable.append(x)
            szamok.remove(x)
           
    for i in range(4):
            x = random.choice(szamok)
            young.append(x)
            szamok.remove(x)
       
    for i in range(4):
            x = random.choice(szamok)
            strong.append(x)
            szamok.remove(x)
      
    for i in range(4):
            x = random.choice(szamok)
            wise.append(x)
            szamok.remove(x)
       
    for i in range(1):
            x = random.choice(szamok)
            superior.append(x)
            szamok.remove(x)

    x = random.randint(1, 25)

    for i in range(len(protector)):
        if x == protector[i]:
            p += 3
    
    for i in range(len(old)):
        if x == old[i]:
            o += 3
            
    for i in range(len(unstable)):
        if x == unstable[i]:
            u += 3
            
    for i in range(len(young)):
        if x == young[i]:
            y += 3
            
    for i in range(len(strong)):
        if x == strong[i]:
            s += 3
            
    for i in range(len(wise)):
        if x == wise[i]:
            w += 3
            
    for i in range(len(superior)):
        if x == superior[i]:
            sup += 3

    protector = []
    old = []
    unstable = []
    young = []
    strong = []
    wise = []
    superior = []

if p == 240:
    print("Protector armorra gyűlt össze a fragment először!")
    print("Ez ", menetek, " menetbe került!...")

if o == 240:
    print("Old armorra gyűlt össze a fragment először!")
    print("Ez ", menetek, " menetbe került!...")
    
if u == 240:
    print("Unstable armorra gyűlt össze a fragment először!")
    print("Ez ", menetek, " menetbe került!...")

if y == 240:
    print("Young armorra gyűlt össze a fragment először!")
    print("Ez ", menetek, " menetbe került!...")

if s == 240:
    print("Strong armorra gyűlt össze a fragment először!")
    print("Ez ", menetek, " menetbe került!...")

if w == 240:
    print("Wise armorra gyűlt össze a fragment először!")
    print("Ez ", menetek, " menetbe került!...")

if sup == 240:
    print("Superior armorra gyűlt össze a fragment először!")
    print("Ez ", menetek, " menetbe került!...")

print("Protector:", p)
print("Old:", o)
print("Unstable:", u)
print("Young:", y)
print("Strong:", s)
print("Wise:", w)
print("Superior:", sup)

print((((menetek * 5) / 60) - ((menetek * 5) // 60)) * 60)
