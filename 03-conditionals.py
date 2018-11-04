# 1. check for something
isSomethingOutside = 1
# 2. check length of something
thingLength = 3
isThingCandy = 1

# 3. check if its bigger than 4 inches
if(isSomethingOutside and thingLength > 4):
  #4. if snake run.
  print('omg its a big snake')
elif (isThingCandy > 0):
  #5. if candy bar... eat.
  print('omg candy! *eats*')
else:
  print('no snakes. safe.')

eggs = 0
milk = 2
butter = 0

if(milk > 1):
  eggs = eggs + 1

if (butter <= 0):
  eggs = eggs * 2
if (eggs >= 2 and milk > 1):
  butter = butter + 400
  eggs = 1
  milk = 4

print('eggs:', eggs)
print('milk:', milk)
print('butter:', butter)