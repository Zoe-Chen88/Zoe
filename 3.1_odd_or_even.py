"""Exercise 3.1 — Odd or even (homework)

WHAT THE PROGRAM MUST DO
    Ask the user for a number N, then say for every number from 1 to N whether it is
    odd or even.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What should happen if the user types 0, a negative number, or 5000?
       Decide the three behaviours before writing anything.

WHAT THE AI CANNOT KNOW
    Your three decisions. An assistant asked for "odd or even from 1 to N" will produce
    a program that behaves absurdly on 0 and on -4, and will happily print five thousand
    lines. Those are your calls, not its.

CHECK IT YOURSELF
    Run it with 6. You should see three odd and three even. Count them.
    Then run it with your three edge cases and confirm each does what you decided.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In:a whole number N typed by the user
# 2. Process:the program goes through every number from 1 to N
#and check if it is odd or even
# 3. Out:one line per number
# 4. What happens on 0, on a negative number, on a very large number:
#if the user types 0, nothing to show, enter a number above 0
#if the user types a negative number, enter a positive number
#if the user types a number over 20, number too big


# Your code below
n = int(input("Enter an integer: "))  # TODO: change the prompt
if n <= 0:
        print("Stop: number is zero or negative") 
        exit()
if n > 20:
        print("Stop: number is too large")
        exit()                         # TODO: keep exit()
else:
        print("Continue with", n)
for i in range(1, n + 1):                     # TODO: keep n + 1
    if i % 2 == 0:
        print(i,"Even")
    else:
        print(i,"Odd")