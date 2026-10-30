"""Exercise 5.2 — Repeating until something changes

WHAT THE PROGRAM MUST DO
    Keep asking the user something until a condition you define is met, then display a
    summary of what happened during the loop.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What is your stop condition, what is your maximum number of attempts, and what
       does your summary contain?

WHAT THE AI CANNOT KNOW
    Your stop condition and your safety limit. An assistant asked for a while loop will
    write one that can run for ever if the user never gives the expected answer. Decide
    how many attempts you allow, and what your program does when that limit is reached.

    Accepting "Yes", "yes" and " yes " as the same answer is your decision too. Make it
    and write it down.

CHECK IT YOURSELF
    Run it and never give the expected answer. If your program is still running after
    your stated maximum, it is wrong. Then run it and answer with capitals and extra
    spaces.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In:the answer typed by the user to the question:
# "Do you confirm your MacBook Air order? (yes/no)"
# 2. Process:the program keeps asking until the user answers yes,
# or until the maximum number of attempts is reached. Before checking,
# it removes extra spaces and puts the answer in lowercase.
# 3. Out:a summary of what happened during the loop
# 4. My stop condition, my attempt limit, my summary:
# Stop condition: the answer is "yes" (so "Yes", "YES" and " yes " all count as yes).
# Maximum: 3 attempts. If the user still has not said yes after 3 attempts, the order is cancelled.
# Summary: the number of attempts, the answers the user gave, and whether the order was confirmed or cancelled.



# Your code below
answers=[]
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    answer = input("Do you confirm your MacBook Air? (yes/no): ").strip().lower()
    answers.append(answer)  # store the answer
    if answer == "yes":
        print("Proceeding...")
        break
    attempts += 1
else:
    print("Maximum attempts reached.")

print("Summary:", answers)

# print the total number of answers
print("Total answers:", len(answers))
# print whether "yes" is in the list
print('Contains "yes":',"yes" in answers)
# Test 1: I answered "no" 3 times. The program stopped after 3 attempts
# and showed "Maximum attempts reached." -> the order is cancelled.
# Test 2: I answered " YES ". Thanks to strip() and lower(), it was
# accepted as "yes" -> the order is confirmed.