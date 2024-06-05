import random
answer = random.randint(1, 10)
guess = 0
guess_count = 0
while guess != answer:
    guess = int(input("guess a number between 1 and 10: "))
    if guess < answer:
        print("Too low...")
    elif guess > answer:
        print("Too high...")
    guess_count += 1
print(f"You guessed {answer} correctly! It took you {guess_count} guesses")