from os import system
system("cls")

def reverseList(lst):
    natija = lst[::-1]
    return natija

lst = [1,2,3,4,5]

natija = reverseList(lst)
print(natija)