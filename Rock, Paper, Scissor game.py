print('Welcome!To Rock,Paper and Scissor Game')
print('1=Rock\n2= Paper\n3=Scissor')
choice=int(input('Enter your choice  '))
if choice==1:
  print('You selected Rock ')
elif choice==2:
  print('You selected Paper')
elif choice==3:
  print('you selected Scissor')
else:
  print('Invalid choice!Please try again')
import random
comp=random.randint(1,3) 
if comp==1:
  print('Computer selected Rock')
elif comp==2:
  print('Computer selected Paper')
else:
  print('Computer selected Scissor')
if (choice==1 and comp==1)or(choice==2 and comp==2)or(choice==3 and comp==3):
  print('😊Match Draw')
elif (choice==1 and comp==3)or(choice==3 and comp==2)or(choice==2 and comp==1):
	print('👑You Win!')
else:
	print('😔Computer Win!')