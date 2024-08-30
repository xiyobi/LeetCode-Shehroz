n = 131072
i = 0
if n < 0:
    print(False)
while 2**i <= n:
    if 2**i == n:
        print(True)
        break
    i += 1
else:
    print(False)
