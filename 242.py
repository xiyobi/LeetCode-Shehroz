def isAnagram(s: str, t: str) -> bool:
        count = 0
        if len(s)==len(t):
              for i in range(len(t)):
                for j in range(i):
                    if s[j]==t[j]:
                          print(s[j],s[i])
                          return True
                    else:
                         return False
        else:
             return False
                    
s ="nagaram"
t ="anagram"
natija = isAnagram(s,t)
print(natija)
 