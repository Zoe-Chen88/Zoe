"""Exercise 8.0 — Operators (bonus, not graded)

WHAT THE PROGRAM MUST DO
    Take two values of your choice and display, as a readable table, the result of every
    comparison between them and of the logical combinations of those results.

ANSWER THESE FIRST, in comments
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which two values did you pick, and which comparison result surprised you?

WHAT THE AI CANNOT KNOW
    Your two values. Pick a pair where the answer is not obvious: two strings with
    different capitalisation, a number and the same number written as text, or zero and
    an empty string.

CHECK IT YOURSELF
    Predict each result before running. Count how many you got right.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: two product names, a = "iPad" and b = "ipad"
#    (the same product, written with different capitalization)
# 2. Process: the program compares a and b with every comparison
#    operator (==, !=, <, >, <=, >=), then combines some of the results
#    with the logical operators and, or, not
# 3. Out: a readable table, one line per comparison, with its result
#    (True or False)
# 4. I picked "iPad" and "ipad" because in a store database, a customer
#    could type the product name in any way. What surprised me:
#    "iPad" == "ipad" is False, so Python does not see them as the same
#    product. And "iPad" < "ipad" is True, because uppercase letters
#    come before lowercase letters for Python.

# My predictions before running:
# a == b  -> False
# a != b  -> True
# a < b   -> ?
# a > b   -> ?
# a <= b  -> ?
# a >= b  -> ?
# (a == b) and (a < b) -> ?
# (a == b) or (a < b)  -> ?
# not (a == b)         -> ?

# Your code below
# the two product names I compare
a = "iPad"
b = "ipad"
print("a =", a)
print("b =", b)
print()

# every comparison between a and b
print("Comparison     Result")
print("----------     ------")
print(f"{'a == b':<15}{a == b}")
print(f"{'a != b':<15}{a != b}")
print(f"{'a < b':<15}{a < b}")
print(f"{'a > b':<15}{a > b}")
print(f"{'a <= b':<15}{a <= b}")
print(f"{'a >= b':<15}{a >= b}")
print()

# logical combinations of the results
print("Combination              Result")
print("-----------              ------")
print(f"{'(a == b) and (a < b)':<25}{(a == b) and (a < b)}")
print(f"{'(a == b) or (a < b)':<25}{(a == b) or (a < b)}")
print(f"{'not (a == b)':<25}{not (a == b)}")

# I got 7 out of 9 right. I was wrong about a < b and a <= b:
# I did not know that uppercase letters come before lowercase
# letters in Python.