

# 1. Ask your user for a first name value using the input function and
#     assign the result to a variable called first_name.
first_name = input("First Name: ")

#    b. Ask your user for a last name value using the input function and
#        assign the result to a variable called last_name.
last_name = input("Last Name: ")

#    c. Combine first_name and last_name into a single variable full_name
#        and print out the length of the string contained in that variable.
full_name = first_name + last_name
print(len(full_name))

# 2. Ask your user for a greeting and store it in a variable called greeting.
greeting = input("Please input a greeting: ")

#    b. Ask your user for the number of times they want to repeat that
#        greeting and store it in a variable called count.
count = int(input("How many times do you want that greeting to repeat?"))

#    c. Print out whether or not the count is less than 100.
if count < 100:
    print("Count is less than 100!")
else:
    print("Count is more than 100")

#    d. Print out the greeting repeated count number of times.
print((greeting + "\n") * count)

# 3. Ask your user for the lowest value in a range and store it in a
#     variable called low.
low = int(input("Please give a lower range value: "))

#    b. Ask your user for the highest value in a range and store it in
#        a variable called high.
high = int(input("Please give an upper range value: "))

#    c. Ask the user for a value, and print whether or not that value
#        is in the range (inclusive).

value = int(input("Please give your value: "))
if (low < value < high):
    print("Value is within range!")
else: 
    print("Value is not within range.")
