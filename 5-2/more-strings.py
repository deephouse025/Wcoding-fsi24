# Create a variable called tongue_twister, assign your favorite tongue twister to that variable as a string.
tongue_twister = "She sells seashells by the seashore"

# Then, create a variable called count, assign a number between 2 and 1,000 to that variable.
count = 14

# Print out the uppercase version of that tongue twister repeated count number of times.
print(tongue_twister.upper * 14)

# Assign that repeated string to a new variable called tongue_twisters.
tongue_twisters = tongue_twister.upper * count

# Print the lowercase version of that variable's (tongue_twisters) value.
print(tongue_twisters.lower)

# Then, print the result of multiplying the length of that variable's value by 15,000.
print(tongue_twisters * 15,000)

# Reassign the value of tongue_twister to be the string 'haha'.
tongue_twister = "haha"

# Reassign the value of tongue_twisters to be the number 9000.
tongue_twisters = 9000

# Combine the two variables into a single string using an f-string
f"{tongue_twister} + {tongue_twisters}"

# Print the result. (eg. 'haha9000')
print(f"{tongue_twister} + {tongue_twisters}")

# Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.
# Sample String : 'restart'
# Expected Result : 'resta$t'