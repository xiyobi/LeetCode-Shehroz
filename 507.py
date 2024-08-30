#Ishlashi tog'ti lekin vaqt chegarisi kop bolgani uchun leetcode qabul qilmaydi
def perfectnumber(num:int)->bool:
    cum = 0
    if num == 0 or num < 0:
        return False
    else:
        for i in range(1,num//2+1):
            if num % i == 0:
                cum += i
    if num == cum:
        return True
num = 28
n = perfectnumber(num)
print(n)