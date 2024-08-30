s = "Qandaysan2 salom1"
n = s.split()
m = ' '
for i in range(len(n)):
    if i == len(n)-1:
        m += n +" "
print(m)