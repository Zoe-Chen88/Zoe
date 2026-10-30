"""Exercise 4.2 — Working with a dictionary

WHAT THE PROGRAM MUST DO
    Describe one real object from your field using a dictionary of at least five fields,
    then read it, change it, remove one field, and display every field with its value.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What object did you describe, which five fields did you choose, and why those?
       A field you would never actually use does not count.

WHAT THE AI CANNOT KNOW
    Your object and your fields. A campaign, a customer, a product, a store, a supplier.
    Choose something you would genuinely have to describe in your job.

CHECK IT YOURSELF
    Ask your program for a field that does not exist. Note what happens in a comment,
    then make it survive that case.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In:a dictionary describing one Apple product (MacBook Air) with 5 fields:
# name, price, category, release year, stock
# 2. Process:the program reads the price, changes it (apple raised it from 1199 to 1399
# euros in 2026), removes the release year, then goes through every remaining field
# 3. Out:the price before the change, then every remaining field with its value, one
# per line
# 4. My object, my five fields, and why those:
# I described a MacBook Air, as if I managed products in a store.
# - name: to identify the product
# - price: to know how much to charge customers
# - category: to group products (laptop, phone, tablet...)
# - release year: to know how recent the model is
# - stock: to know when to stock more
# I removed the release year because it is the least useful for daily sales.


# Your code below
product = {
    "name": "MacBook Air",
    "price": 1199,
    "category": "laptop",
    "release_year": 2026,
    "stock": 50
}
# read the price from the dictionary
price = product["price"]
print("price before:", price)
# change the price to the new 2026 price
product["price"] = 1399
print("price after:",product["price"])
# remove the release_year key
del product["release_year"]
# loop through the dictionary and print each key and value 
for key, value in product.items():
   print(key,":",value)
# test: asking for a key that does not exist ("color")
# gives KeyError:'color' and the program stops.
# fix: I used .get() with a default value, so the program shows "not available"
print(product.get("color", "not available"))