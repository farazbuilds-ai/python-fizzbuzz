import random
alphabets=['a','b','c' ,'d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers=['1','2','3','4','5','6','7','8','9']
symbols=['#','$','&','@','?','!','^','_','/','*','+']
length=int(input('Enter the length of Password '))
password=alphabets+numbers+symbols
for i in range(length):
 letters=random.choice(password)
 print(letters,end = "")