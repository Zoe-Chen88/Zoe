"""Exercise 4.0 — Working with a list

WHAT THE PROGRAM MUST DO
    Build a list of at least eight items, then display: the whole list, one item of your
    choice, the list sorted, and something computed from it.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What is your list about, and what did you compute from it? Why is that number
       interesting?

WHAT THE AI CANNOT KNOW
    The content of your list. It must come from your own field: marketing channels,
    campaign names, product references, cities you operate in, monthly budgets. Not
    fruit, not "item1, item2, item3".

    Keep this file. Exercise 5.1 and exercise 6.0 both reuse the list you build here.

CHECK IT YOURSELF
    If you computed an average, a total or a maximum, work it out by hand on three of
    your items first, then check your program agrees on those three.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In:a list of the starting prices(in euros) of 8 apple products in France
# 2. Process:the program displays the list, picks one price, sorts the list from
#cheapest to the most expensive, and computes average from it
# 3. Out:the whole list, one chosen price, the sorted list, and the average
# 4. What my list is about, and what I computed from it:
# My list is about the starting prices of apple products in France in 2026.
# I computed the average
# It is interesting because Apple raised its price this year, so the average helps to 
# see the general price level of the brand and compare it with competitors.


# Your code below
prices = [1479, 1119, 799, 1399, 509, 819, 449, 149]
print(prices)
item = prices[2]
print(item)
prices.sort()
print(prices)
total = sum(prices)
count = len(prices)
avg = total / count
print(avg)

#chek by band: (149+449+509+799+819+1119+1399+1479)/8=840.25
#full avaerage by the program:840.25