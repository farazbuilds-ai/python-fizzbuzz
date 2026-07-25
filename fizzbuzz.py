R=1
while R<=50:
   if R%3==0 and R%5==0:
     print("FizzBuzz")
   elif R%3==0: 
     print("Fizz")
   elif R%5==0:
     print("Buzz")
   else:
     print(R)
R+=1
