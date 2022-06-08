import json
import random
import time
import sys
import datetime

class LeetCodePicker:
  def __init__(self, filename):
    self.leetcodes = self.load_leetcodes(filename)
    self.picked = set()
    self.i = 1
    print()
  
  def load_leetcodes(self, filename):
    return json.load(open(filename))

  def filter_leetcodes_by_difficulty(self, difficulty):
    return [x for x in self.leetcodes if x[1].lower() == difficulty.lower()]

  def pickRandom(self, numChoices, difficulty=None):
    leetcodes = self.leetcodes if difficulty is None else self.filter_leetcodes_by_difficulty(difficulty)
    for _ in range(numChoices):
      choice = random.choice(leetcodes)
      while choice[0] in self.picked:
        choice = random.choice(leetcodes)
        
      self.picked.add(choice[0])
      print(f"{self.i}) {choice[0]} ({choice[1]})\t- {choice[2]}")
      self.i += 1

  def timer(self, seconds):
    print()
    for remaining in range(seconds, -1, -1):
        sys.stdout.write("\r")
        sys.stdout.write(f"Time Remaining: {datetime.timedelta(seconds=remaining)} ") 
        sys.stdout.flush()
        time.sleep(1)
    print("\rTIMES UP!!!                   ")


def main():
  lcp = LeetCodePicker("leetcodes.json")
  lcp.pickRandom(2, "easy")
  lcp.pickRandom(2)

  # 1 hr 10 min
  lcp.timer(1*60**2 + 10*60)

main()