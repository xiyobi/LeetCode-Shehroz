from os import system
system("cls")
lst = [12,2,6,15,7896]
count = 0
for i in range(len(lst)):
     if len(str(lst[i]))%2==0:
                count+=1
print(i)                
    