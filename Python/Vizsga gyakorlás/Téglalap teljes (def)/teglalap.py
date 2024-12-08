class teglalap():
    #Az osztály elkülönít, ha esetleg több téma is van
    def __init__(self, a, b):
        #Ha a változókat külső részről szedjük, bele kell rendelnünk egy "self" mapppába, aminek bármi lehet a neve, így az osztályban lévő defek hozzá tudnak férni
        self.a = a #Amíg a defekben vagyunk, "self.a"-ként kell hivatkozni egy bele rendelt változóra, mert abba a mappába helyeztük a defek részére
        self.b = b
    def kerulet(self): #A defekhez egyenként hozzá kell rendelni a mappát, hogy mindegyik hozzá tudjon férni a változókhoz. Csak akkor kell, ha dolgozik is belőle
        k = (self.a + self.b) * 2
        return k #Ha a kerület defet akarjuk meghívni, azt a változót fogja reprezentálni, amit megadunk neki. Itt a kerület a "k" értékével lesz egyenlő
    def terulet(self):
        t = self.a * self.b
        return t
    def kiir(self): #Nincsenek használva benne a külsős változók, de amiket meghívunk benne függvények, azoknak kellenek, így ide is kell a mappa
        print("A négyzet kerülete:", T.kerulet(), "cm") #Egy "T" változóba beleraktuk  függvényt, hogy tudjuk használni, így a továbbiakban is így kell rájuk hivatkozni
        print("A négyzet területe:", T.terulet(), "cm2")

a = int(input("Add meg a téglalap 'a' oldalát cm-ben!"))
b = int(input("Add meg a táglalap 'b' oldalát cm-ben"))

T = teglalap(a, b) #Itt a "T" változó, amibe beleraktuk a függvényt, és hozzá rendeltük a kettő változót, hogy az "init" bele rakhassa a mappába

T.kiir()

with open("teglalap.txt", "w")as f:
    f.write(f"A téglalap 'a' oldala: {a} cm\n")
    f.write(f"A téglalap 'b' oldala: {b} cm\n")
    f.write(f"A téglalap kerülete: {T.kerulet()} cm\n")
    f.write(f"A téglalap területe: {T.terulet()} cm2\n")

print("A python fájllal egy mappába megtalálja a válaszokat a 'téglalap.txt' fájlban!")

#A "with open" ha nincs "téglalap.txt" fájl a python fájl mappájába, létrehoz egyet, és azzal dolgozik
#A "w" a write-ot képviseli, tehát megadjuk neki, hogy írni tervezünk a fájlba
#Az "as f" egy változó, amit adunk neki, így utána lesz lehetőségünk írni a fájlba. Per pillanat az "f" a "téglalap.txt"
#"f.write"-tal kezdjük a sort, így az "f" változót fogjuk írni
#Mindent egy ""-be írunk ,kivéve az "f" változót az elején. A változókra {}-ben fogunk innentől hivatkozni
#A sorokat \n-nel törjük, mert a fájl alapból egy sorba kap mindent
