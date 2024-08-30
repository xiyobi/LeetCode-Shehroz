n = 10
m = 3
cum = 0
cum1 = 0
for i in range(1,n+1):
    if i%m == 0:
        cum += i
    elif not i%m == 0:
            cum1 += i
print( abs(cum - cum1))
print(cum)
print(cum1)