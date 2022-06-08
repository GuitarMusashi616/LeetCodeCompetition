import json
import random
import time
import sys
import datetime


def pickRandom(leetcodes, numChoices, not_picked):
  for i in range(numChoices):
    choice = random.choice(leetcodes)
    while choice[0] not in not_picked:
      choice = random.choice(leetcodes)
      
    not_picked.remove(choice[0])
    print(f"{i}) {choice[0]} ({choice[1]})\t- {choice[2]}")


def timer(remaining):
  for remaining in range(remaining, -1, -1):
      sys.stdout.write("\r")
      sys.stdout.write(f"Time Remaining: {datetime.timedelta(seconds=remaining)} ") 
      sys.stdout.flush()
      time.sleep(1)
  print("\rTIMES UP!!!                   ")


def main():
  # 1, 2, 3 - easy, medium, hard
  leetcodes = json.load(open("leetcodes.json"))
  not_picked = {x[0] for x in leetcodes}
  
  # easy only
  easy = [x for x in leetcodes if x[1] == "Easy"]
  
  print()
  pickRandom(easy, 2, not_picked)
  pickRandom(leetcodes, 2, not_picked)
  print()
  
  # 1 hr 10 min
  timer(1*60**2 + 10*60)  

main()