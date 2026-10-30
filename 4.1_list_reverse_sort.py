"""Exercise 4.1 — Reordering without losing the original (homework)

WHAT THE PROGRAM MUST DO
    Starting from the list you built in exercise 4.0, display it in four different
    orders, and prove at the end that the original list has not been damaged.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which four orders did you choose, and in which of them is your original list
       modified rather than copied?

WHAT THE AI CANNOT KNOW
    That your original must survive. Some ways of reordering a list change it in place,
    others return a new one. Find out which is which, and say so in your comments.
    That distinction is the entire exercise.

CHECK IT YOURSELF
    The last line of your program must display the original list. Compare it, item by
    item, with what you wrote in 4.0. If it has moved, your program is wrong even
    though it ran.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In:the list of 8 apple product prices from exercise 4.0
# 2. Process:the program displays the list in four different orders without changing
# the original list
# 3. Out:the list in four orders, and at the end the original list, unchanged, to prove
# it was not damaged
# 4. My four orders, and which ones modify the original:
# cheapest to most expensive, most expensive to cheapest, reversed, and shuffled.
# sort(), reverse(), and random.shuffle() modify the original list in place, so I did 
# not use them on prices.
# sorted() and [::-1] return a new list, so the original stays the same.
# for the shuffle, I used random.sample(), which returns a new shuffled list.
# the tutor also suggested random.shuffle(prices), but it shuffles in place, 
# so it would damage the original list.


# Your code below
import random
prices = [1479, 1119, 799, 1399, 509, 819, 449, 149]
sorted_prices = sorted(prices)
print(sorted_prices)
descending_prices = sorted(prices, reverse=True)
print(descending_prices)
reversed_prices = prices[::-1]
print(reversed_prices)
shuffled_prices = random.sample(prices, len(prices))
print(shuffled_prices)
print(prices)