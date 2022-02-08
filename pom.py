#! Python3
#pom.py pomodoro timer

import time datetime

# Display user instructions
activeTask = input('Enter name of task> ')
pomDur = 25
pomDur = int(input('Enter pom minutes [20]> ') or "25")
print(f'{activeTask} is the task.  Press enter to start pomodoro timer')
input()
print('Started')

def pomodoro(n):
  pomNum = n
  elipse = 0
  startTime = time.time()
  pomTime = round(time.time() - startTime, 2)
  while round(pomTime <= pomDur):
    pomTime = round(time.time() - startTime, 2)
    if (pomTime > 0 and pomTime % 5 == 0.00):
      elipse = elipse + 5
      print(f'{elipse}...')
      time.sleep(.1)
  print('Times up')
  pomNum = pomNum + 1
  return(pomNum)

for i in range(4):
  count = pomodoro(i)
  print(f'You\'ve done {count} poms')
  print(f'{activeTask} is the task.  Press enter to start pomodoro timer')
  input()
  print('Started')

print('Break until ')



 

