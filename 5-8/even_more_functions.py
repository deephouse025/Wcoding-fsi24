# 1. Write a function to find the largest of three numbers, without using
#     the built-in `max` function.
def largerest (one, two, three):
    largest = one
    if two > one:
        largest = two
    elif three > one:
        largest = three
    print(largest)

# return(largerest(55, 65, 21))


# 2. Write a function to sum all the numbers in a list, without using the
#     built-in `sum` function.
def summed (list):
    sum = 0
    for num in list:
        sum += num
        print(num)
        print(sum)

# return(summed([2, 4, 5, 2, 3, 2, 1, 2, 2]))

# 3. Write a function to multiply all the numbers in a list, without using
#     any library functions.
def multiplied (list):
    total = 1
    for num in list:
        total *= num
        print(num)
        print(total)

# return(multiplied([2, 3, 4, 2, 6]))


# 4. Write a function to reverse a string, without using the built-in
#     `reverse` function.
def reversed(string):
    output = []
    mylist = list(string)
    for num in mylist:
        output.insert(0,num)
    output = "".join(output)
    return(output)


# print(reversed("hello"))


# 5. Write a function called 'withinRange' that takes three parameters,
#     a number you are checking for, the first number to check against and
#     the last number to check against. Check whether the first number falls
#     in the other numbers (inclusive) and return a boolean.
def withinRange (check_for, check_against_first, check_against_second):
    if check_against_first < check_against_second:
        if check_against_first < check_for < check_against_second:
            return("Within range? ", True)
        else:
            return(False)
    elif check_against_first > check_against_second:
        if check_against_first > check_for > check_against_second:
            return("Within range? ", True)
        else:
            return(False)  
# print(withinRange(10, 5, 15))


# 6. Write a function that takes a list and returns a new list with
#     unique elements of the first list.
def unique (list):
    for num in list:
        if list[num] == list[num + 1]:
            print(num)
            del list[num]
            print(list)
        




# 7. Write a function that takes a number as a parameter and checks if the
#     number is prime or not.
def prime_check(numL):
    _list = []
    if numL % 2 == 0:
        return False
    _half = int(numL/2)
    for i in range(_half+1, 3, -2):
        if numL%1==0:
            return False
    return True


# 8. Write a function to print only the even numbers from a given list.
# if int % 2 == 0


# 9. Write a function to create and print the list of squares for the
#      numbers between 1 and 30 (both included).