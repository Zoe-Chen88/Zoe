"""Exercise 8.1 — Bitwise operators (bonus, not graded)

WHAT THE PROGRAM MUST DO
    Represent a set of permissions as bits, combine two of them, test whether a third is
    present, then add it and remove one.

ANSWER THESE FIRST, in comments
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What are your permissions about? Not files: invent a set from your own field,
       such as who may view, edit and publish a campaign.

WHAT THE AI CANNOT KNOW
    Your permission set and what each one means in your context.

CHECK IT YOURSELF
    Display the value in binary at each step and read the bits yourself.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: four permissions for a marketing campaign, stored as bits:
#    VIEW = 0001, EDIT = 0010, PUBLISH = 0100, DELETE = 1000
# 2. Process: the program gives a team member VIEW and EDIT (with |),
#    tests if they can PUBLISH (with &), adds PUBLISH (with |),
#    then removes EDIT (with & ~)
# 3. Out: the permissions in binary after each step, and True/False
#    for each test
# 4. My permissions are about who can work on a marketing campaign:
#    - VIEW: see the campaign and its results
#    - EDIT: change the text, images and budget
#    - PUBLISH: put the campaign online
#    - DELETE: remove the campaign
#    Example: a junior marketer can view and edit, then gets the right
#    to publish, and their edit right is removed once the campaign is live.

# Your code below
# each permission is one bit (one switch)
VIEW = 1        # 0001
EDIT = 2        # 0010
PUBLISH = 4     # 0100
DELETE = 8      # 1000

print(f"VIEW    = {VIEW:04b}")
print(f"EDIT    = {EDIT:04b}")
print(f"PUBLISH = {PUBLISH:04b}")
print(f"DELETE  = {DELETE:04b}")
print()

# step 1: combine two permissions with | (a junior marketer can view and edit)
user = VIEW | EDIT
print(f"Step 1 - view + edit:        {user:04b}")

# step 2: test if a third permission is there with &
can_publish = (user & PUBLISH) != 0
print(f"Step 2 - can publish?        {can_publish}")

# step 3: add the publish permission with |
user = user | PUBLISH
print(f"Step 3 - add publish:        {user:04b}")
print(f"         can publish now?    {(user & PUBLISH) != 0}")

# step 4: remove the edit permission with & ~
user = user & ~EDIT
print(f"Step 4 - remove edit:        {user:04b}")
print(f"         can edit now?       {(user & EDIT) != 0}")

# Check by reading the bits (right to left: VIEW, EDIT, PUBLISH, DELETE):
# 0011 -> VIEW and EDIT are on
# 0111 -> VIEW, EDIT and PUBLISH are on
# 0101 -> VIEW and PUBLISH are on, EDIT is off
# DELETE is never on, which is correct: a junior marketer cannot delete.