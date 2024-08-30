
def ila(a: int):
        # a = a[::-1]
        print(a,type(a))
        x=int(a,2)
        return x
lst = "00111001011110000010100101000000"
natija = ila(lst)
print(natija,type(natija))