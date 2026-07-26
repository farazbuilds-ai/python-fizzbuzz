attemps = 0
print("Welcome!to Guess The Number game")
print("I have selected a number between 1 to 100")
import random
secret=random.randint(1,100)
while True:
 n=int(input("Enter a number between 1 to 100:"))
 attemps +=1
if n<1 or n>100:
  print("Wrong!Please enter a number between 1 to 100")
elif n<secret:
  print("Too Low")
elif n>secret:
  print("Too High")
else:
  print("Congratulations! You win the game")
  print("Attemps:",attemps)
break
