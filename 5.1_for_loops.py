"""Exercise 5.1 — Doing the same thing to every item

WHAT THE PROGRAM MUST DO
    Take the list you built in exercise 4.0 and, for every item, display a line that
    combines the item, its position, and something computed about it.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What did you compute for each item, and what does the reader learn from that line?

WHAT THE AI CANNOT KNOW
    Your list from 4.0, and what is worth computing about its items. Length of the name,
    share of a total, position in a ranking, whether the item passes a threshold you set.
    Open your 4.0 file, copy the list across, and say in a comment what you decided.

CHECK IT YOURSELF
    Count the lines your program printed. There must be exactly as many as items in your
    list. If there is one more or one less, you have an off-by-one, and it is worth
    understanding now rather than in the exam.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In:the list of 8 Apple product prices from exercise 4.0
# 2. Process:the program computes the average price, then for every
# price it checks if it is above or below the average
# 3. Out:8 lines, one per product, each with its position, its price,
# and whether it is above or below the average
# 4. What I compute for each item, and why it is worth showing:
# For each item I compared the price with the average (840.25 euros).
# The user learns which Apple products are expensive compared to
# the rest of the range, and which ones are more affordable.


# Your code below
prices = [1479, 1119, 799, 1399, 509, 819, 449, 149]
# TODO: compute the average price
average = sum(prices) / len(prices)
print("Average price:",average)
# loop over the prices with their position
for idx, price in enumerate(prices, start=1):
    status = "above" if price > average else "below"
    print(f"{idx} {price} is {status} average")
#Check: the program printed 8 lines, and my list has 8 items,
#so there is no off-by-one error.
#3 products are above average, 5 are below.