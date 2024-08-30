from os import system
system("cls")
def ikkkikik(a:str, b:str):
    x  = int(a,2)
    y = int(b,2)
    z = bin(x + y)[2:]
    
    return z

a = str(11)
b = str(1)
ikkkikik(a,b)    







































'''
ajoyib usul bilib oldim 
easy exam
def ila(a: str, b: str) -> str:
        x=int(a,16)
        print(x)
        y=int(b,16)
        print(y)
        z=x+y
        z=bin(z)[2:]
        return z
'''
a = str(1010)
b = str(1011)
natija = ikkkikik(a,b)
print(natija)

