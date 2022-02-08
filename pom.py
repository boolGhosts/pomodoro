#! Python3
#pom.py pomodoro timer

import time, datetime, subprocess

# Display user instructions
activeTask = input('Enter name of task> ')
pomDur = 25
pomDur = int(input('Enter task time [25] min > ') or "25")
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
  #subprocess.Popen(['start', 'alarm.wav'], shell=True)
  pomNum = pomNum + 1
  return(pomNum)

def main():
    for i in range(4):
        count = pomodoro(i)
        print(f'You\'ve done {count} poms')
        if i < 3:
            print(f'{activeTask} is the task.  Press enter to start pomodoro timer')
            input()
            print('Started')
    return()

while True:
    main()
    lnbreakmin = int(input('Long break time! How long? [15]min > ') or "15")
    lnbreakcalc = datetime.datetime.fromtimestamp(time.time() + lnbreakmin*60)
    print(f"Break until {lnbreakcalc.strftime('%H:%M')}.")
    time.sleep(lnbreakmin*60)
    #subprocess.Popen(['start', 'alarm.wav'], shell=True)
    print(f'Break over! {activeTask} is the task.  Press enter to start pomodoro timer')
    input()
