def son(s):
   for i in range(len(s)):
      if s[i] == 1:
        return i
l = [1,1,2,2,4,4,3]
natija = son(l)
print(natija)
        