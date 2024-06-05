# 1. Write a Python function that takes a list of words and returns the
#     longest word and the length of the longest word.

# def longest_word ():
#     for word in 
#     this_word = 


#    b. Call the function with positional arguments

#    c. Call the function with keyword arguments


# 2. Write a Python function to remove the n-th index character from a
#     nonempty string.
def remove_char (num, string):
    mylist = list(string)
    del(mylist[num])
    mylist = "".join(mylist)
    print(mylist)



#    b. Call the function with positional arguments
remove_char(1, "hello world i am luke")

#    c. Call the function with keyword arguments
remove_char(num = 6, string = "peanutbutterjellysandwich")
 

# 3. Create a function called add_title which takes a name and gender as
#     arguments and returns either "Mr. <name>" or "Ms. <name>"
#     (eg. Calling `add_title("Pam", "F")` returns "Ms. Pam")


#    b. Call the function with positional arguments

#    c. Call the function with keyword arguments


# 4. Create a function called multiply_elements which takes a list and a
#     number as arguments. It multiplies each element in the list by the
#     number, and returns the list

#    b. Call the function with positional arguments

#    c. Call the function with keyword arguments