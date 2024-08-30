d = 199
x = sum((map(lambda s: int(s), str(d))))
y = sum(map(lambda s: int(s), str(x)))
natija = list(map(lambda s: int (s),str(y)))
if natija[1] == 0:
    print(natija[0],type(y))