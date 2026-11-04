"""Exercise 7.1 — Loading a file, cleaning it, saving the result (homework)

This is the direct rehearsal for the final exam. Session 8 starts with it.

WHAT THE PROGRAM MUST DO
    Load names.txt, clean what is inside, sort it by last name, and write the result to
    a new file. The original file must not be modified.

DO THIS BEFORE ANYTHING ELSE
    Open names.txt and read it with your eyes. Then write, in comments at the top of
    your file, everything that is wrong with it. There are at least four different
    problems. Find them yourself.

    This step is not optional and it is graded. An assistant cannot see your file.

ANSWER THESE, in comments, after the list of problems
    1. What goes in?
    2. What happens to it?  (one line per problem you found, and how you deal with it)
    3. What comes out?
    4. What does "sort by last name" mean when a line contains two words, and how do you
       know which one is the last name?

WHAT THE AI CANNOT KNOW
    The actual content of names.txt. If you paste this brief into an assistant without
    describing the file, it will write a program for a clean file, and that program will
    crash or produce nonsense on the real one.

    Describe the file to it. That description is the exercise.

CHECK IT YOURSELF
    Count the lines in names.txt, then in your output file. The numbers should differ,
    and you should be able to say exactly why. Then check the first and last name of
    your sorted list by hand.

DELIVERABLE
    This file, plus the output file your program produced.
"""

# What is wrong with names.txt (found by reading it, not by guessing):
# - The capitalization is inconsistent (ada LOVELACE, grace hopper, GUIDO van rossum)
# - There are empty lines (lines 3 and 9)
# - Some lines start with extra spaces (alan TURING, linus torvalds)
# - One name has three words (Guido van Rossum), so the last name is not always the 2nd word

# 1. names.txt, a list of 10 lines with first and last names
# 2. Process, problem by problem:
#    - empty lines: I skip them
#    - extra spaces: I remove them with strip()
#    - capitalization: I fix it with title() (e.g. "Ada Lovelace")
#    - three words: I sort by the last word of the line
# 3. Out: a new file names_clean.txt with one clean name per line,
#    sorted by last name. names.txt is not modified.
# 4. With two words, the first is the first name and the second is the
#    last name. With "Guido van Rossum", I decided to sort by the last
#    word, "Rossum", so he is sorted under R.


# Your code below
names = []  # TODO: create an empty list to store the cleaned names

with open('names.txt', 'r') as file:    
    for line in file:
        clean_line = line.strip()
        if clean_line:          # skip empty lines
            names.append(clean_line.title())  # TODO: capitalize the name and add it to the list
print(names)

sorted_names = sorted(names, key=lambda name: name.split()[-1])  # TODO: split the name and pick the last word
print(sorted_names)

with open('names_clean.txt', 'w') as out_file:
    out_file.writelines(name + '\n' for name in sorted_names)  # TODO: add newline after each name

  # Check: names.txt has 10 lines, names_clean.txt has 8 lines,
  # because I removed the 2 empty lines.
  # First: Margaret Hamilton, last: Alan Turing (checked by hand).