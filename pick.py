import json
import random
# 1, 2, 3 - easy, medium, hard
leetcodes = json.load(open("leetcodes.json"))

# easy only
leetcodes = [x for x in leetcodes if x[1] == "Easy"]

for i in range(4):
    choice = random.choice(leetcodes)
    print(f"{i}) {choice[0]} ({choice[1]}) {choice[2]}")

print("\nTime Remaining: 1 hr 10 min")