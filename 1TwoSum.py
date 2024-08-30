from os import system
system("cls")

def son(lst:list,s:int):
    lst2 =[]
    for i in range(len(lst)):
        for j in range(i+1,len(lst)):
            if lst[i]+lst[j] == s:
                lst2.append(i)
                lst2.append(j)
                return lst2



lst = [1,2,3,4,5]
s = 6
natija = son(lst, s)
print(natija)