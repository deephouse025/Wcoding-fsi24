# 1. Write a function to find the sum of the series, up to n terms.
#     ie. 2 + 22 + 222 + 2222 + .. n terms
#     Call the function with number_of_terms to verify that your
#     function works as expected.
# number_of_terms = 5  # => 24690 (total of 2 + 22 + 222 + 2222 + 22222)
def termMaker(_terms, _num):
    _acc = 0
    for i in range(_terms):
        _acc += int(str(_num) + str(_num)*i)
        print(_acc)

# termMaker(number_or_terms, 2)
    
    

#    b. Change number_of_terms to verify that your function is correct.


# 2. Print out the following pattern
# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# * * * * 
# * * * 
# * * 
# *


# 3. Write a function calculation() such that it can accept two variables
#     and calculate the addition and subtraction of them. It must return
#     both addition and subtraction results in a single function call.


# 4. Generate a Python list of all the even numbers between 4 and 30


# 5. Write a function that returns the largest item from the following list:
lst = [4, 6, 8, 24, 12, 2]
def largest(arr):
    print(max(arr))
largest(lst)


#    b. Change the list to verify your function is correct.
lst = [5, 222, 3, 4, 544]
largest(lst)


# 6. Write a function that given a string of odd length greater than 7,
#     it returns a new string made up of the middle three characters of
#     the string.
def number6 (str):
    if len(str) / 2 != 0:
        if len(str) > 7:
            str = list(str)
            a = (len(str) / 2) - 1
            b = (len(str) / 2) + 1
            print("6: ", str[a, b])
number6("brotherrr")


# 7. Write a function that given two strings, s1 and s2, it returns a new
#     string with s2 in the middle of s1. If s1 has an odd number of
#     characters, bias s2 towards the left.