def sonlar(num):
    if num < 0:
        return False
    i = 0
    while 3**i <= num:
        if 3**i == num:
            return True
        i += 1
    else:
        return False


s= 5
natija = sonlar(s)
print(natija)