# Here is the word so far: ****
# Guess a letter (5 guesses left): l
# Here is the word so far: l***
# Guess a letter (4 guesses left): k
# Here is the word so far: l**k
# Guess a letter (3 guesses left): a
# Here is the word so far: l*ak
# Guess a letter (2 guesses left): e
# You guessed the word!: leak

# stars[2] = letters[3]
# print(stars)
# answer = ["a", "g", "h", "i"]






# answer
import random
answer = []
for x in range(0, 4):
    answer.append(random.randint(1, 9))
print(answer)
# [4, 7, 7, 7]

newArr = list(("* " * len(answer)).split())
print(newArr)
['*', '*', '*', '*']

# playing loop
guess_count = 0
playing = True
guess = ""
while playing == True:
    guess = int(input(f"Guess a letter ({6 - guess_count} guesses left): "))
    guess_count += 1
    for x in range(len(answer)):
        if guess == answer[x]:
            newArr[x] = answer[x]
    if newArr == answer:
        print(f"You guessed the word!: {answer}")
        playing = False
    print(f"Here is the word so far: {newArr}")
    if guess_count > 6:
        print("Out of guesses...")
        exit()