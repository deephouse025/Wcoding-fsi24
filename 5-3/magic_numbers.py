# 1. Get a 3-digit number from the user. Ask that all three digits are
#     different numbers. Store this number in a variable called 'first_num'.
first_num = (input("Please give a 3-digit number: "))

# 2. Validate that all 3 digits are different numbers. If not, instruct
#    the user to run the exercise again with a valid number and stop
#    running the rest of the code by calling 'exit()'.
if len(first_num) < 3:
    exit()



# 3. Reverse the 3 digits in first_num, without using the list 'reverse'
#    or 'reversed' functions. Use only what you've learned so far.
#    Save this reversed number in another variable called 'second_num'.
else:
    second_num = first_num[::-1]
    print(second_num)

# 4. Subtract second_num from first_num and store the result in another
#    variable called 'third_num'. If third_num is a negative number
#    turn it into a positive number.
first_num = int(first_num)
second_num = int(second_num)  
third_num = first_num - second_num
if third_num < 1:
    third_num = third_num * -1

# 5. Reverse third_num and save it to a variable called 'fourth_num'.
fourth_num = int(str(third_num[::-1]))

# 6. Add third_num and fourth_num and print out the result. (1089)
print(third_num + fourth_num)

# 7. Subtract the lesser number of first_num and second_num from the
#    greater number of first_num and second_num so that you end up
#    with a positive number for the difference. Save this difference
#    in a variable called 'fs_diff'.


# 8. Add up the individual digits that make up fs_diff and print out
#    the resulting sum. (18)