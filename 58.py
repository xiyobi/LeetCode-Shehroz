from os import system
system("cls")
def sozsize(soz:str):
    n = soz.split()
    #x = n[::-1]
    # print(x)
    for i in n[::-1]:
        print(i)
        if not i == " ":
            s = len(i)

        return s
    
d = "   fly me   to   the moon  "
natija = sozsize(d)
print(natija)
