from os import system
system("cls")

def palidrom(s:int)-> bool:
    son = list(str(s))
    natija = (son[::-1])
    if natija == son:
        return True
    else:
        return False

son = int(input("son kiriting: "))
natija = palidrom(son)
print(natija)