def szam(ev1, ev2):
    if ev1 > ev2:
        kul = ev1 - ev2
        print("A különbség", kul, "év!")
        ev = ev2
        for i in range(kul + 1):
            if (ev % 400) == 0 or (ev % 4) == 0 and (ev % 100) != 0:
                L1.append(ev)
            ev += 1
        print("Szökőévek:", L1)
    if ev1 < ev2:
        kul = ev2 - ev1
        print("A különbség:", kul, "év!")
        ev = ev1
        for i in range(kul + 1):
            if (ev % 400) == 0 or (ev % 4) == 0 and (ev % 100) != 0:
                L1.append(ev)
            ev += 1
        print("Szökőévek:", L1)
    if ev1 == ev2:
        ev = ev1
        if (ev % 400) == 0 or (ev % 4) == 0 and (ev % 100) != 0:
            print("A két szám ugyanaz, de", ev1, "pont egy szökőév!")
        else:
            print("A két szám ugyanaz!")

L1 = []

print("Szökőév számoló!")
          
ev1 = int(input("Add meg a kezdő évet!"))
ev2 = int(input("Add meg a második évet!"))

szam(ev1, ev2)
