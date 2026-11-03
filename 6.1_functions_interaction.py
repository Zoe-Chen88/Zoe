"""Exercise 6.1 — Small functions working together

WHAT THE PROGRAM MUST DO
    Write three small functions, each doing one thing, and a fourth that uses the other
    three to answer one question about your data.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?  (say which function does what, in order)
    3. What comes out?
    4. What question does your fourth function answer, and why does splitting it into
       three make it easier to check?

WHAT THE AI CANNOT KNOW
    Your question and your split. Ask an assistant for "three functions" and it will
    invent three; they will not be the three your question needs. Decide the split first,
    on paper, then ask.

    One function, one job. If you cannot describe what one of yours does in a single
    sentence without using the word "and", it is doing two things.

CHECK IT YOURSELF
    Test each of the three small functions on its own before combining them. Write in a
    comment the input and expected output you used for each. That is three test cases,
    and they are part of the deliverable.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In:the list of 8 Apple product prices from exercise 4.0
# 2. Process, function by function:
# Process, in order:
# - compute_average(prices) returns the average price of the list
# - is_below(price, limit) returns True if the price is lower than the limit
# - format_price(price) returns the price as a text with the euro sign, e.g. "799 €"
# - show_cheaper_products(prices) uses the first three: it gets the average,
# checks every price against it, and prints the cheaper ones nicely formatted
# 3. Out:the list of products that cost less than the average price, one per line, e.g. "799 €"
# 4. The question my fourth function answers:
# My fourth function answers: which Apple products are cheaper than the average price? 
# Splitting it into three small functions makes it easier to check, 
# because I can test each part alone: if the result is wrong, I know which small function has the mistake.


# Your code below
prices = [1479, 1119, 799, 1399, 509, 819, 449, 149]

def compute_average(prices):
    # add up all the prices
    total=sum(prices)
    # divide bu the number of prices
    average=total/len(prices)
    return average
print(compute_average(prices))
# Test 1: input = my 8 prices, expected output = 840.25

def is_below(price, limit):
    # check if the price is lower than the limit
    result=price<limit
    return result
print(is_below(799, 840.25))
print(is_below(1479, 840.25))
# Test 2: is_below(799, 840.25)-> expected True
#         is_below(1479, 840.25)-> expected False

def format_price(price):
    # turn the number into a text with the euro sign
    formatted=f"{price}€"
    return formatted
print(format_price(799))
# Test 3: format_price(799) -> expected "799€"

def show_cheaper_products(prices):
    avg = compute_average(prices)
    for p in prices:
        if is_below(p, avg):
            print(format_price(p))
show_cheaper_products(prices)

