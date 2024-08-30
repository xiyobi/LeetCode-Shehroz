def son(son):
    i = 0
    if son < 0:
        return False
    if son > 0:
        while i**4 <= son:
            if i ** 4 == son:
                return True
            i += 1
    else:
        return False

s = 4
n = son(s)
print(n)