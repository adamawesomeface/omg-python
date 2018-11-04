import random


def getSnakeLength():
  snakeLength = random.randint(1,12)
  isSnake = 0
  if(snakeLength > 4):
    isSnake = 1
  else:
    isSnake = 0
  return isSnake

for snake in range(100):
  snake = getSnakeLength()
  if(snake > 0):
    print('snake!', snake)