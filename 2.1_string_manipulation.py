"""Exercise 2.1 — Transforming text (homework)

WHAT THE PROGRAM MUST DO
    Ask the user for a sentence, then display four different transformations of it.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which four transformations did you choose, and in what situation would each of
       them be useful? One line each.

WHAT THE AI CANNOT KNOW
    Your four transformations. Pick them yourself. Open ../examples/strings/string_methods.py
    to see what is available, then choose, then justify.

    A transformation that produces the same thing as another one does not count as two.

CHECK IT YOURSELF
    Run it with a sentence that has spaces at both ends and a capital in the middle.
    For each of your four results, say in a comment whether it is what you expected.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In:a sentence typed by the user
# 2. Process:the sentense is transformed in 4 ways:-upper(),-title(),-strip(),-len()
# 3. Out:the 4 transformed versions
# 4. My four transformations, and when each is useful:
#-upper():to make an important message stand out
#-title():to format names correctly
#-strip():to clean extra spaces a user typed by mistake in a form
#-len():to check the lenth of a text


# Your code below
sentence = input("enter a sentence: ")   # TODO: change the prompt
upper_sentence = sentence.upper()        # TODO: keep upper()
title_sentence = sentence.title()        # TODO: keep title()
stripped_sentence = sentence.strip()      # TODO: keep strip()
length = len(sentence)                   # TODO: keep len()

print("Upper:", upper_sentence)
print("Title:", title_sentence)
print("Stripped:", stripped_sentence)
print("Length:", length)