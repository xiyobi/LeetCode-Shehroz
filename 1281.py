n = 324
j = 1
x  = sum(map(lambda n: int(n),str(n)))
y  = list(map(lambda n: int(n),str(n)))
for i in y:
    j*= i 
print(j-x)
#return (j-x)