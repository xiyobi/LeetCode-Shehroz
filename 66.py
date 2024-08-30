from os import system
system("cls")

def yigindi(son:list):
    d =[]
    y = len(son)
    sm = 0
    for i in range(y):
        sm += son[i]*(10**(y-1-i))
    sm+=1
    num_lst = list(map(lambda d: int(d), str(sm)))
    return num_lst
lst = [1,2,4]
natija = yigindi(lst)
print(natija,type(natija))