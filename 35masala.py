from os import system
system("cls")
def searchInsert(lst:list, s: int) -> int:
        for i in range(len(lst)):
            if s == lst[i]:
                return i
            elif lst[i] > s:
                return i
        return len(lst)
    

s = 7
lst = [1,2,3,4,6]
natija = searchInsert(lst,s)
print(natija)