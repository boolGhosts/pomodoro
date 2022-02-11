#! Python3
#pom.py pomodoro timer

import time, datetime, subprocess, shelve

pomtaskShelf = shelve.open('pomtasks')

def taskinput():
    activeTask = input('Enter name of task> ').upper()
    if activeTask == 'CLEAR':
        for i in pomtaskShelf.keys():
            print(f'deleting {i}...')
            del pomtaskShelf[i]
        taskinput()
    elif activeTask == 'LIST':
        for k, v in pomtaskShelf.items():
            print(f' - {k, v}')
        taskinput()
    elif activeTask == 'DELETE':
        q = input('Which task to delete? > ').upper()
        if q in pomtaskShelf.keys():
            del pomtaskShelf[q]
        else:
            print('does not exist')
        taskinput()
    else:
        print(f'{activeTask} is the task.')
        if activeTask in pomtaskShelf:
            print(f'{activeTask} task exists with {pomtaskShelf[activeTask]} poms.')
        else:
            pomtaskShelf[activeTask] = 0
            print(f'Creating new key named {activeTask}.')
        return(activeTask)

def pomodoro(n):
  pomNum = n
  elipse = 0
  startTime = time.time()
  pomTime = round(time.time() - startTime, 2)
  while round(pomTime <= pomDur):
    pomTime = round(time.time() - startTime, 2)
    if (pomTime > 0 and pomTime % 5 == 0.00):
      elipse = elipse + 5
      #print(f'{elipse/60}...')
      print('...')
      time.sleep(59)
  print('Times up')
  subprocess.Popen(['start', './pomodoro/alarm.wav'], shell=True)
  pomNum = pomNum + 1
  return(pomNum)

def pomactive(activeTask):
    for i in range(4):
        count = pomodoro(i)
        pomtaskShelf[activeTask] = pomtaskShelf[activeTask] + 1
        print(f'You\'ve done {pomtaskShelf[activeTask]} poms')
        if i < 3:
            print(f'{activeTask} is the task.  Press enter to start pomodoro timer')
            input()
            print('Started')
    return()


activeTask = taskinput()

pomInput = int(input('Enter task time [25] min > ') or "25")
pomDur = pomInput*60
input('+++++Press Enter to Start+++++')
print('Started')


pomactive(activeTask)

lnbreakmin = int(input('Long break time! How long? [15]min > ') or "15")
lnbreakcalc = datetime.datetime.fromtimestamp(time.time() + lnbreakmin*60)
print(f"Break until {lnbreakcalc.strftime('%H:%M')}.")
time.sleep(lnbreakmin*60)
subprocess.Popen(['start', './pomodoro/alarm.wav'], shell=True)
print(f'Break over! {activeTask} is the task.  Press enter to start pomodoro timer')
input()

pomactive(activeTask)
