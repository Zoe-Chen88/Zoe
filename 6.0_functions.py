"""Exercise 6.0 — Naming a piece of work

WHAT THE PROGRAM MUST DO
    Write a function that computes something useful about the list you built in exercise
    4.0, then call it three times with different inputs and display the three results.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?  (what your function receives)
    2. What happens to it?
    3. What comes out?  (what your function returns)
    4. What is your function called, and does its name say what it does without reading
       the code?

WHAT THE AI CANNOT KNOW
    What is worth computing about your data, and what to call it. A function named
    "process" or "do_stuff" fails this exercise even if it works.

    Your function must RETURN its result, not print it. Find out why that difference
    matters and write the reason in a comment. It is the whole point of the exercise.

CHECK IT YOURSELF
    Call your function with an empty list. Note what happens. Then decide whether that
    behaviour is acceptable, and say so in a comment.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In:a list of prices (numbers).
# 2. Process:add up all the prices, then multiply the total by 0.9 (a 10% discount).
# 3. Out:returns one number - the total price after the 10% discount.
# 4. My function name, and why return rather than print:
# My function name: discounted_sum
# The name tells you what it does without reading the code:
# it gives the total after a 10% discount.
# return gives the result back to the program, so I can store it in a variable, 
# round it, compare it or use it in another calculation. 
# print only shows it on the screen, and the function would return None, 
# so the value can't be reused.


# Your code below
def discounted_sum(values):
    total = sum(values)
    return total * 0.9

prices = [1479, 1119, 799, 1399, 509, 819, 449, 149]

print(discounted_sum(prices))
print(discounted_sum(prices[:3]))
print(discounted_sum(prices[-3:]))
empty = []
print(discounted_sum(empty))
# Empty list: returns 0.0 with no error.
# This is acceptable, because the total of no items is 0.
