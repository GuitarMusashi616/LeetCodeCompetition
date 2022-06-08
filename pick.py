import json
import random
import time
import sys
import datetime



def pickRandom(leetcodes, numChoices):
  print()
  for i in range(numChoices):
    choice = random.choice(leetcodes)
    leetcodes.remove(choice)
    print(f"{i}) {choice[0]} ({choice[1]}) {choice[2]}")
  print()


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
  
  # easy only
  leetcodes = [x for x in leetcodes if x[1] == "Easy"]

  pickRandom(leetcodes, 4)

  # 1 hr 10 min
  timer(5)  

main()