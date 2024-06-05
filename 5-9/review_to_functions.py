# 1. Ask the user for a number. Depending on whether the number is even or
#     odd, print out an appropriate message to the user. If the number is a
#     multiple of 4, print out yet a different message.
def odd_even (number):
    if int(number) % 2 != 0:
        print("Odd!")
    elif int(number) % 4 == 0:
            print("Number is divisible by 4")
    else:
        print("Even!")
        



# 2. Use the following list and write a function that prints out all the
#     elements of the list that are less than 5.
arr = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

def less_than(nums_arr):
    for num in nums_arr:
        if num < 5:
            print(num)
less_than(arr)


#    b. Instead of printing the elements one by one, make a new list that
#        has all the elements from arr that are less than 5 and print
#        out this new list.

def less_than(nums_arr):
    new_arr = []
    for num in nums_arr:
        if num < 5:
            new_arr.append(num)
    print(new_arr)

less_than(arr)




# 3. Create a function that asks the user for a number and then prints out a
#     list of all the divisors of that number.
number = int(input("give a number: "))
def print_divisors (number):
    divisors = []
    for num in range(1, (number + 1)):
        if number % num == 0:
            divisors.append(num)

    print(divisors)
print_divisors(number)

    
# print_divisors(200)


# 4. Use the following lists and write a function that returns a new list that
#     contains only the elements that are common between the lists (without 
#     duplicates).
arr1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
arr2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

def commonalities (first, second):
    arr3 = []
    for num in arr1:
        if num in arr2:
            if num not in arr3:
                arr3.append(num)
    return arr3

print(commonalities(arr1, arr2))


# 5. Write a function that asks the user for a string and prints out whether
#     this string is a palindrome or not. (A palindrome is a string that
#     reads the same forwards and backwards.)
# def palindrome_checker (word):
#     if reversed(word.lower) == word.lower:
#         print("This word is a palindrome! ")
#     else:
#         print("Not a palindrome")
# palindrome_checker(121)

word = input("Give a word: ")

def palindrome_checker (word):
    if word[::-1].lower() == word.lower():
        print(f"{word} is a palindrome!")
    else:
        print(f"{word} is not a palindrome")
palindrome_checker(word)