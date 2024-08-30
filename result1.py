class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        belgi = 1
        natija = 0
        uzunlik = len(s)
        
        while i < uzunlik and s[i] == ' ':
            i += 1
        
        if i < uzunlik and (s[i] == '-' or s[i] == '+'):
            belgi = -1 if s[i] == '-' else 1
            i += 1
        
        while i < uzunlik and s[i].isdigit():
            raqam = ord(s[i]) - ord('0')
            
            if natija > (2**31 - 1) // 10 or (natija == (2**31 - 1) // 10 and raqam > (2**31 - 1) % 10):
                return 2**31 - 1 if belgi == 1 else -2**31
            
            natija = natija * 10 + raqam
            i += 1
        
        return natija * belgi
