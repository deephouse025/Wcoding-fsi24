import random
prompt = input("Would you like to roll or quit? ")
if prompt.lower() == "quit":
    exit()
if prompt.lower() == "roll":
    roll = random.randint(1, 6)
    print(roll)
else:
    print("Invalid input. ")