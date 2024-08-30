from os import system
system("cls")

def salyla(s:str):
    a = " "
    n = s.split(" ")
    for i in n:
        for j in i:
            if j.isalpha() or j.isdigit():
                a += j
    x = a.lower().find(a[::-1].lower())
    if x == -1 and len(a)>1: 
        return False
    else:
        return True     
soz =  "A man, a plan, a canal: Panama"
# soz =  "race a car"
natija = salyla(soz)
print(natija)