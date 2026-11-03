# Name: Zixuan CHEN
# Group: A

# 1. in:
# The file scenarios_A.csv. The separator is a comma.
# It has 14 columns: ID, Scenario, OptionA, OptionB, OptionC,
# BudgetA, BudgetB, BudgetC, ReputationA, ReputationB, ReputationC,
# FeedbackA, FeedbackB, FeedbackC.
# The columns are grouped by type, not by option: to find option B,
# I read OptionB, BudgetB, ReputationB and FeedbackB.
# Numbers are whole numbers, negative ones start with "-", no thousand separator. 
# They are read as text, so I convert them with int().
# Texts that contain a comma are inside double quotes.

# 2. What happens? (one day)
# - Show the day number, the budget and the reputation
# - Show the situation and options A, B, C
# - Ask for A, B or C, ask again until the answer is valid
# - Add the budget change and the reputation change
# - Keep reputation at 100 maximum
# - Show the feedback line
# - Save the day in the history list
# - If budget or reputation is 0 or less, the game stops

# 3. What comes out?
# At the end the player sees: fired (and why) or the final score and title, 
# plus the best and the worst move.
# One line of results.csv looks like: Zixuan,6350,100,CMO Material,2026-11-03

# 4. What could go wrong?
# - The player types a wrong key: the program asks again.
# - A gauge goes below zero: the game stops and says the player is fired.
# - Reputation goes above 100: the program sets it back to 100.
# - The file scenarios_A.csv is missing: the program shows a message and stops instead of crashing.
# Feature chosen: d (Difficulty), At the start the player picks easy (15,000 EUR) or
# hard (6,000 EUR), because it is simple to add and and it changes how the whole game feels.

import csv
import random
from datetime import date


# Read every scenario from the CSV file and return them as a list
def load_scenarios():
    with open('scenarios_A.csv', newline='') as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    return rows

# Turn one row into three option tuples (A, B, C)
def get_options(row):
    a = (row['OptionA'], int(row['BudgetA']), int(row['ReputationA']), row['FeedbackA'])
    b = (row['OptionB'], int(row['BudgetB']), int(row['ReputationB']), row['FeedbackB'])
    c = (row['OptionC'], int(row['BudgetC']), int(row['ReputationC']), row['FeedbackC'])
    return a, b, c

# Ask the player for A, B, or C until the answer is valid
def ask_choice():
    while True:
        choice = input("Your choice (A, B or C): ").strip().upper()
        if choice in {'A', 'B', 'C'}:
            return choice
        print("Please type A, B or C.")

# Apply the chosen option and return the new budget and reputation
def apply_choice(budget, reputation, option):
    budget += option[1]
    reputation += option[2]
    reputation = min(reputation, 100)
    return budget, reputation

# Return the player's title from the final score
def get_title(score):
    if score < 95:
        return "Eternal Intern"
    elif 95 <= score <= 119:
        return "Growth Hacker"
    elif 120 <= score <= 139:
        return "CMO Material"
    else:
        return "Viral Legend"

# Start of the game: player name, difficulty, scenarios
name = input("Enter your name: ")
difficulty = input("Choose difficulty (easy/hard): ").strip().lower()
budget = 15000 if difficulty == "easy" else 6000
reputation = 50
try:
    scenarios = load_scenarios()
except FileNotFoundError:
    print("Error: scenarios_A.csv not found. Please check the file path.")
    raise SystemExit(1)
random.shuffle(scenarios)
history = []

# Play 10 days: show the situation, ask a choice, apply it
for day in range(1, 11):
    row = scenarios[day - 1]
    options = get_options(row)
    print(f"\n--- Day {day} ---")
    print(f"[Budget: {budget} EUR | Reputation: {reputation}/100]")
    print(row["Scenario"])
    print(" A:", options[0][0])
    print(" B:", options[1][0])
    print(" C:", options[2][0])
    choice = ask_choice()
    chosen = options["ABC".index(choice)]
    budget, reputation = apply_choice(budget, reputation, chosen)
    print(chosen[3])
    print(f"Budget {chosen[1]:+} EUR, Reputation {chosen[2]:+}")
    history.append((chosen[2], day, chosen[0]))
    if budget <= 0 or reputation <= 0:
        break
# End of the game: fired or title, then best and worst move
if budget <= 0:
    print("You are fired: the budget ran out.")
    title = "Fired"
elif reputation <= 0:
    print("You are fired: the reputation reached zero.")
    title = "Fired"
else:
    print("Quarter survived!")
    score = reputation + budget // 200
    title = get_title(score)
    print(f"Budget left: {budget} EUR, reputation: {reputation}/100")
    print(f"Final score: {score}")
    print(f"{name}, your title: {title}")

best = max(history)
worst = min(history)
print(f"Best move:  day {best[1]}, \"{best[2]}\" ({best[0]:+})")
print(f"Worst move: day {worst[1]}, \"{worst[2]}\" ({worst[0]:+})")

# Save the result of this game as a new line in results.csv
today = date.today().isoformat()
row = [name, budget, reputation, title, today]

with open('results.csv', 'a', newline='') as f:
    writer = csv.writer(f)
    if f.tell() == 0:
        writer.writerow(['Name', 'Budget', 'Reputation', 'Title', 'Date'])
    writer.writerow(row)
print("Saved in results.csv")