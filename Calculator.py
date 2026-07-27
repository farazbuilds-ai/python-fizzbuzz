# Calculator project
def sum(a,b):
 return a+b
def diff(a,b):
 return a-b
def mult(a,b):
 return a*b
def div(a,b):
 return a/b 
def mod(a,b):
 return a%b
a=float(input('Enter the first value '))
b=float(input('Enter the second value ' ))
opr=(input('Enter the operator for calculation '))
if opr=='+':
	print('Answer=',sum(a,b))
elif opr=='-':
	print('Answer=',diff(a,b))
elif opr=='*':
	print('Answer',mult(a,b))
elif opr=='/':
	if b==0:
	  print('Invalid Value!Second value is 0 ,Try Again')
	else:
	  print('Answer=',div(a,b))
elif opr=='%':
	if b==0:
	 print('Invalid value!Second value is 0,Try Again')
	else:
	 print('Answer=',mod(a,b))
else:
 	print('Invalid Operator')