def natija(son):
    count = 0
    for i in range(1,son+1):
        if son % i == 0:
            count += 1
    if count >= 3:
        return True
    else:
        return False
    
son= 4
print(natija(son))
        