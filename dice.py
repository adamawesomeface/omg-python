import random

def rollDice(sides):
  # 3. plugin to random for result
  result = random.randint(1, int(sides))
  print(result)
  again = input('Want to roll again? Y/N')
  return again

def game():
  play = 1
  while(play > 0):
    sides = input('How many sides are on your dice?')
    keepGoing = rollDice(sides)
    if(keepGoing == 'N' or keepGoing == 'n'):
      print('fine. i dont wanna roll with you anyway.')
      play = 0

game()
