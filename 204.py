n= 10
count = 0
count1 = 0
for i in range(2,n,1):
    for j in range(1,i+1):
        if i % j == 0:
            count += 1
    if count == 2:
        count1 += 1
print(count1)