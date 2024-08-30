s = "byd"
k = 4
k = k % len(s)
if not len(s) == k:
    d = s[k:len(s)]
    f = s[0:k]
    s = d + f
else:
    d = s[k+1:len(s)-1]
    f = s[:k+1]
    s = d + f

print(s)
