from os import system
system("cls")
n = []
sel = 36.50
if 0 <= sel and sel<= 1000:
    k = sel + 273.15
    n.append(k)
    F = sel*1.80+32.00
    n.append(F)
print(n) #return n