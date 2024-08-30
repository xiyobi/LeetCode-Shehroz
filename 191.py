s  = bin(128)
count = 0
for i in range(2,len(s)):
    if s[i] == "1":
        count += 1
print(count)
