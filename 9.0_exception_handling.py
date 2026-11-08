"""Exercise 9.0 — Surviving what you did not expect

Useful for the final exam: two campaigns in the exam dataset have zero conversions.

WHAT THE PROGRAM MUST DO
    Ask the user for a number, divide something by it, and keep running whatever the
    user types. Never crash.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which two different failures can happen here, and should they produce the same
       message to the user? Decide before coding.

WHAT THE AI CANNOT KNOW
    Your answer to question 4, and how many attempts you allow before giving up.

    An assistant will often propose catching every error at once. Find out why catching
    each failure separately is better, and write the reason in a comment.

CHECK IT YOURSELF
    Run it with: a normal number, then zero, then the word "abc", then an empty line.
    Four runs, four behaviours, all described in a comment. If any of them stopped your
    program, it is not finished.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: the number of conversions of a campaign, typed by the user
# 2. Process: the program divides the budget (1000 euros) by the number
#    of conversions to get the cost per conversion (CPA). If the input
#    is wrong, it shows a message and asks again, 3 attempts maximum.
# 3. Out: the CPA in euros, or a clear message explaining the problem
# 4. The two failure, and whether they deserve the same message:
#    - ValueError: the user types something that is not a whole number
#      ("abc" or an empty line). Message: "Please type a whole number."
#    - ZeroDivisionError: the user types 0, and we cannot divide by 0.
#      Message: "This campaign has 0 conversions."
#    They should NOT get the same message: the causes are different,
#    so the user needs to know what to fix.
#    Why catch each failure separately: with one "catch everything"
#    block, the user does not know what went wrong, and real bugs in
#    my code could be hidden without me noticing.

# Your code below
budget = 1000          # campaign budget in euros
max_attempts = 3       # I allow 3 tries before giving up
attempts = 0

while attempts < max_attempts:
    attempts += 1
    try:
        conversions = int(input("How many conversions did the campaign get? "))
        cpa = budget / conversions
        print(f"Cost per conversion (CPA): {cpa:.2f} euros")
        break    # valid answer: stop asking
    except ValueError:
        # the input is not a whole number ("abc" or empty)
        print("Please type a whole number, for example 25.")
    except ZeroDivisionError:
        # 0 conversions: the CPA cannot be computed
        print("This campaign has 0 conversions: the CPA cannot be computed.")
else:
    # this runs only if the loop ended without break (3 wrong answers)
    print("Too many invalid answers. The program stops here.")

print("End of the program.")

# Tests (4 runs):
# - 40: the program shows "Cost per conversion (CPA): 25.00 euros"
#   and ends normally. Check by hand: 1000 / 40 = 25.
# - 0: message "This campaign has 0 conversions: the CPA cannot be
#   computed." (ZeroDivisionError), then it asks again.
# - abc: message "Please type a whole number, for example 25."
#   (ValueError), then it asks again.
# - empty line: same message as abc, because int("") is also a
#   ValueError.
# After 3 wrong answers, the program says "Too many invalid answers"
# and stops politely. In all 4 runs, the program never crashed.