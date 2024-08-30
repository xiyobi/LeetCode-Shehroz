from os import system
system("cls")
def info(s:str)->str:
    d = " "
    soz = s.split(" ")
    for i in soz:
        n = i[::-1]
        d +=n+" "
    x = d[0:(len(d)-1)]
    print(x,type(x)) 
soz ="salom qalaysan yaxshimisa"
info(soz)



'''
 d =  ""
        soz = s.split()
        for i in soz:
            n = i[::-1]
            d += n
        return d  '''
