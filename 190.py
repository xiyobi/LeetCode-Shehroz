
def ila(a: int):
        s = bin(a)[2:][::-1]
        s = s + "0"*(32 - len(s))
        x=int(s,2)
        return x
lst = "00111001011110000010100101000000"
natija = ila(lst)
print(natija,type(natija))
