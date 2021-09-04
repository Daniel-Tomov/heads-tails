import random
import time

guess = ''
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter "heads" or "tails":')
    guess = input()
toss = random.randint(0, 1) # 0 is tails, 1 is heads

if toss == 1:
    toss = 'heads'
if toss == 0:
    toss = 'tails'

if guess == toss:
    print('You got it!')
else:
  print('Better luck next time!')

time.sleep(5)
print(':(')