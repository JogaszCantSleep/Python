import math

class kör():
    def __init__(self, r):
        self.r = r
    def átmérő(self):
        d = self.r * 2
        return d
    def kerület(self):
        K = self.r * 2 * 3.14
        return K
    def terület(self):
        T = self.r * self.r * 3.14
        return T
    def kiir(self):
        print("A kör átmérője:", kör.átmérő(), "cm")
        print("A kör kerülete:", kör.kerület(), "cm")
        print("A kör területe:", kör.terület(), "cm2")
    
r = int(input("Add meg a kör sugarát cm-ben! "))

kör = kör(r)

kör.kiir()

with open("kör.txt", "w")as f:
    f.write(f"A kör sugara: {r}cm\n")
    f.write(f"A kör átmérője: {kör.átmérő()}cm\n")
    f.write(f"A kör kerülete: {kör.kerület()}cm\n")
    f.write(f"A kör területe: {kör.terület()}cm2\n")

print("A python fájllal egy mappába megtalálja a válaszokat a 'kör.txt' fájlban!")
