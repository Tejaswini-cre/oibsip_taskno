import random

Letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
         'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
Numbers=['1','2','3','4','5','6','7','8','9','10']
Symbols=['$','%','&','*','#''@','^']
print("welcome to password generator")
n_Letters=int(input("how many letters do you want?"))
n_Numbers=int(input("how many numbers do you want?"))
n_Symbols=int(input("how many symbols do you want?"))
password=[]

for char in range(1,n_Letters+1):
        password+=random.choice(Letters)
        
for num in range(1,n_Numbers+1):
        password+=random.choice(Numbers)
        
for sym in range(1,n_Symbols+1):
         password +=random.choice(Symbols)
random.shuffle(password)
clear_password=''.join(map(str,password))
print(clear_password)
         
