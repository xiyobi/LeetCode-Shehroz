from os import system
system("cls")
def uskode(soz:str, soz1:str):
   return soz.find(soz1)
      
        
soz = input("Soz kiriting: ")
soz1 = input("Soz1 kiriting: ")
natija = uskode(soz,soz1)
print(natija)