"""Exercise 7.0 — Collecting data and saving it

WHAT THE PROGRAM MUST DO
    Ask the user for the information needed to record one entry, then save it to a CSV
    file. Running the program twice must produce two entries, not overwrite the first.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?  (name your file, and list your columns)
    4. Which columns did you choose, and what would you actually do with this file once
       it has two hundred rows in it?

WHAT THE AI CANNOT KNOW
    Your columns. They must be the ones you would really need to collect for a purpose
    you can state. See 7.0_student_data.csv for the shape of a header line, not for
    the columns to use.

    Two behaviours are yours to decide, and an assistant will guess them wrong:
    what happens the very first time, when the file does not exist yet and needs its
    header line, and what happens when a value the user typed is not acceptable.

CHECK IT YOURSELF
    Run your program three times with different values. Then open the file and count
    the lines. You should have three entries and exactly one header line. If you have
    three header lines, or one entry, your program is wrong.

DELIVERABLE
    This file, plus the CSV your program produced.
"""

# 1. In:the information typed by the user for one order:
# the customer name, the product, and the quantity
# 2. Process:the program checks that the quantity is a whole number
# above 0, adds today's date, and adds the order as a new line
# at the end of the file (it never overwrites the old orders)
# 3. Out, file name and columns:one new line in the file orders.csv
# Columns: customer_name, product, quantity, date
# 4. Why these columns, and what this file is for:
# I chose these columns because a store needs to know who ordered,
# what, how many, and when. With 200 rows, I could find the best-selling
# product, the busiest days, and the customers who order the most, to plan stock and promotions.

# Your code below
import os
import csv
from datetime import date

def today_text():
    today = date.today()
    return today.strftime("%Y-%m-%d")

customer_name = input("Enter the customer name: ")
product = input("Enter the product:")

while True:
    try:
        quantity = int(input("Enter the quantity: "))
        if quantity>0:
            break
        print("The quantity must be above 0.")
    except ValueError:
        print("Please enter a whole number.")

today=today_text()
file_exists = os.path.exists("orders.csv")

with open("orders.csv", "a", newline="") as f:
    writer = csv.writer(f)
    if not file_exists:
        writer.writerow(["customer_name", "product", "quantity", "date"])
    writer.writerow([customer_name, product, quantity, today])
python 7.0_standard_io_file_output.py

# Test: I ran the program 3 times with different orders.
# orders.csv has 1 header line and 3 entries: the file is not overwritten
# and the header is written only once.
# When I typed "abc" or "-2" as quantity, the program asked again.