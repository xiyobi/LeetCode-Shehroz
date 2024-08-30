def missingNumber(son: list):
    son.sort()
    for i in range(son[0],(len(son))):
        if not son[i] == i:
            return i
son = [0,1]
natija = missingNumber(son)
print(natija,type(natija))