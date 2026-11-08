"""Exercise 10.0 — Checking the shape of text (bonus, not graded)

WHAT THE PROGRAM MUST DO
    Validate three pieces of information typed by the user, and only save them when all
    three are acceptable.

ANSWER THESE FIRST, in comments
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What are your three fields, and what makes a value acceptable for each? Write the
       rule in plain English before writing any pattern.

WHAT THE AI CANNOT KNOW
    Your three rules. "A valid email" is not a rule, it is a wish. Say what you accept
    and what you reject, and be ready to defend a borderline case.

WHAT TO WATCH
    An assistant will hand you a pattern that looks like line noise. Do not accept it
    until it has explained it to you piece by piece, and you have written that
    explanation in your own words above it.

CHECK IT YOURSELF
    For each field, prepare one value that must pass and two that must fail. Run all
    nine. Any surprise goes in a comment.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: three pieces of information typed by the user for an order:
#    the order ID, the French postal code, and the customer email
# 2. Process: the program checks the shape of each value with a
#    regular expression. It saves the three values only if all three
#    are valid.
# 3. Out: OK or REJECTED for each field, and one new line in
#    valid_orders.csv when everything is valid
# 4. My three fields and their rules, in plain English:
#    - Order ID: exactly "ORD-" in capital letters, then exactly 5 digits.
#      Accept: ORD-12345. Reject: ord-12345 (lowercase), ORD-123 (too short).
#    - Postal code: exactly 5 digits, nothing else (French format).
#      Accept: 75008. Reject: 7500 (4 digits), 75A08 (a letter inside).
#    - Email: some text, one @, some text, a dot, some text, and no spaces.
#      Accept: zoe@skema.edu. Reject: zoe.skema.edu (no @),
#      zoe @skema.edu (a space).
#    Borderline case: I do not check if the email really exists,
#    only its shape. A shop would confirm it by sending an email.

# What each pattern means, piece by piece:
# ORD-\d{5}
#   ORD-   the exact text "ORD-"
#   \d     one digit (0 to 9)
#   {5}    exactly 5 times
# \d{5}
#   five digits, nothing more, nothing less
# [^@\s]+@[^@\s]+\.[^@\s]+
#   [^@\s]+  one or more characters that are not @ and not a space
#   @        the @ sign
#   [^@\s]+  again some text without @ or spaces (the domain, e.g. skema)
#   \.       a real dot (the \ means "a dot", not "any character")
#   [^@\s]+  the end, e.g. edu
# re.fullmatch checks that the WHOLE value has this shape,
# not just a part of it.

# Your code below

import re
import csv

# the three rules, written as regular expressions
ORDER_ID_RULE = r"ORD-\d{5}"
POSTAL_CODE_RULE = r"\d{5}"
EMAIL_RULE = r"[^@\s]+@[^@\s]+\.[^@\s]+"

# ask the user (strip removes spaces at the start and the end)
order_id = input("Order ID (e.g. ORD-12345): ").strip()
postal_code = input("Postal code (e.g. 75008): ").strip()
email = input("Email (e.g. zoe@skema.edu): ").strip()

# check each value: True if the whole value matches the rule
order_ok = re.fullmatch(ORDER_ID_RULE, order_id) is not None
postal_ok = re.fullmatch(POSTAL_CODE_RULE, postal_code) is not None
email_ok = re.fullmatch(EMAIL_RULE, email) is not None

print("Order ID:", order_id, "->", "OK" if order_ok else "REJECTED")
print("Postal code:", postal_code, "->", "OK" if postal_ok else "REJECTED")
print("Email:", email, "->", "OK" if email_ok else "REJECTED")

# save only when all three are valid
if order_ok and postal_ok and email_ok:
    with open("valid_orders.csv", "a", newline="") as f:
        csv.writer(f).writerow([order_id, postal_code, email])
    print("All three are valid: saved to valid_orders.csv")
else:
    print("At least one value is not valid: nothing was saved.")

# Tests (9 values, 3 runs):
# Run 1: ORD-12345, 75008, zoe@skema.edu -> all OK, saved
# Run 2: ord-12345, 7500, zoe.skema.edu -> all REJECTED, nothing saved
# Run 3: ORD-123, 75A08, zoe @skema.edu -> all REJECTED, nothing saved
# valid_orders.csv has exactly 1 line, as expected.
# Surprise: lowercase "ord-12345" is rejected, because regex is
# case-sensitive, like the == comparison in exercise 8.0.