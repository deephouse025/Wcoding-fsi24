# 1. Create a function that asks the user for radius and height of a
#     cylinder and the function will return the volume of that cylinder.
#     Use the math library for pi!
import math
def cylinder_volume():
    radius = int(input("Please give radius: "))
    height = int(input("Please give height: "))
    print("Volume: ", (math.pi * (radius ** 2) * height))

# 2. Create a function that will generate a random number up to 1000 and
#     ask the user to guess the number. Let the user know if the guess is
#     higher or lower than the target number. Keep allowing the user to
#     guess, but stop after a correct guess, or after 10 wrong guesses.
import random
answer = random.randint(1, 1001)
correct = False
def higher_lower():
    guess_count = 0
    while correct == False and guess_count < 10:
        guess = int(input("Guess: "))
        guess_count += 1
        if guess > answer:
            print(f"Too high, {10 - guess_count} guesses remaining.")
        if guess < answer:
            print(f"Too low, {10 - guess_count} guesses remaining.")
        if guess ==  answer:
            print("Correct!")
            exit()
higher_lower()

# 3. Create a function that will generate a random date in the year 2024
#     and ask the user to guess the date. (For simplicity, have the user
#     enter in the format 'mm-dd'.) The guessing continues until the user
#     guesses the correct date or types 'q' as an input to quit.
import datetime
def guess_date():
    beg = datetime.date.today().replace(month=1, day=1).toordinal()
    end = datetime.date.today().replace(month=12, day=31).toordinal()
    answer_date = datetime.date.fromordinal(random.randint(beg, end)).isoformat()[-5:]

    x = 0
    while True:
        user_input = input("3: Guess a date (mm-dd): ")
        if user_input == answer_date:
            print(f"\tCORRECT! It took you {x + 1} guess{'es' if x > 1 else ''}.")
            break
        elif user_input == 'q':
            print(f"\tOk, goodbye. The answer was {answer_date}.")
            break
        elif user_input > answer_date:
            print("\tToo late!")
        else:
            print("\tToo early!")

        x += 1

guess_date()


# 4. Create a function that asks the user for a date in 'yyyy-mm-dd' format
#     and print out the day of the week for that date. (eg. "Monday",
#     "Tuesday", etc.)
def date_to_day():
    user_input = input("4: Give me a date (yyyy-mm-dd): ")
    user_date = datetime.date.fromisoformat(user_input)

    # days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    # print("4:", days_of_week[user_date.weekday()])

    print("4:", user_date.strftime('%A'))  # Same as above, but without needing translation.

date_to_day()