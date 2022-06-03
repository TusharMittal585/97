import random

chances=0
a=random.randint(0,9)

while chances<5:
      guess=int(input('Guess a number between 1 and 9'))

      if guess==a:
            print('Awesome!You Won')
            break
      elif guess>a:
            print('Your guess is too high')
      else:
            print('Your guess is too low') 
      chances +=1

if not chances<5:
      print('You lose! The number is',a) 

