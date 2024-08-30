n = [1,1,2,2,2,3]
dt = {}
m = []
for i in range(len(n)):
    dt[n[i]] = n.count(n[i])
n = sorted(dt.items(),reverse=True)
for i in n:
    i = list(i)
    for j in range(i[1]):
        m.append(i[0])
print(m)