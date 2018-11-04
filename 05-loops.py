import random

fruits = ["apple", "banana", "cherry"] # list
## FOR LOOPS
'''
for fruit in fruits:
  print(fruit)

for snake in range(10):
  print(snake)
'''

# Fill the Luggauge (lazy way)
def getBags(numberOfBags):
  bagList = []
  options = ['metal', 'plastic', 'wood', 'candy', 'snake','tickleSnakeEater']
  totalOptions = len(options) - 1
  for x in range(numberOfBags):
    # getting ranom option
    item = random.randint(0, totalOptions)
    bagList.append(options[item])

  return bagList

def feedSnakeEaters(snakes, snakeEaters):
  print('CHOMP')
  print(len(snakeEaters), 'just ate',len(snakes),'snakes. YUM.')


## WHILE LOOPS
bags = getBags(100)
print(bags)

# 2. get value of contents

metals    = []
plastics  = []
woods     = []
snakes    = []
candies   = []
snakeEats = []

# 1. loop through bag
for item in bags:
  # 3. if useful store in a comparement for robot supplies
  if(item == 'metal'):
    metals.append(item)
  if(item == 'plastic'):
    plastics.append(item)
  if(item == 'wood'):
    woods.append(item)
  if(item == 'candy'):
    candies.append(item)
  if(item == 'snake'):
    snakes.append(item)
  if(item == 'tickleSnakeEater'):
    snakeEats.append(item)

# 4. if tickleSnakeEater save
if(len(snakes) > 0 and len(snakeEats) > 0):
  feedSnakeEaters(snakes, snakeEats)

# 6. check inventory
print('You has ', len(metals), 'metal')
print('You has ', len(plastics), 'plastic')
print('You has ', len(woods), 'wood')
print('You has ', len(candies), 'candy')
print('You has ', len(snakes), 'snakes')
print('You has ', len(snakeEats), 'snake eaters')



'''
current = 1
while current <= luggageCount:
  print('checking bag #', current)
  if(current == 57):
    print('found candy!')
  if(current % 3 == 0):
    print('found metal!')
  current += 1
'''
