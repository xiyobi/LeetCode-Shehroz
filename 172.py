def trailingZeroes(n: int):
        c = 1
        count = 0
        if n <= 0:
            return 0
        if n > 0:
            while not  n == 0:
                c *= n
                n -= 1
        c = str(c)[::-1]
        for i in range(len(c)):
            print(c[i],len(c))
            if c[i] == 0:
                count += 1
            else:
                 return count 
d = 5
s = trailingZeroes(d)
print(s)