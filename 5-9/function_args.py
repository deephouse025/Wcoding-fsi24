# 1. Create a function multi_print which takes advantage of *args, accepts
#     any number of positional arguments, and prints them all using a for
#     loop, also print the total number of arguments passed into multi_print.
def multi_print (*args):
    # print(args)
    # total = 0
    for num in args:
        print(num)
        # total += 1
    print("total: ", len(args))

# multi_print(1, 2, 3, 4, 5, 6)

# 2. Create a function that accepts any number of numbers as positional
#     arguments and prints the sum of those numbers.
def num_sum (*args):
    # print(args)
    # sum = 0
    # for num in args:
    #     print(num)
    #     sum += num
    print("Total: ", sum(args))

# num_sum(3, 5, 2, 2, 1, 4)




# 3. Create a function that accepts any number of positional and keyword
#     arguments, and that prints them back to the user. Your output should
#     print the positional arguments on one line, each item separated with
#     the string 'and'. All the keyword arguments should be printed in the
#     format 'key - value', each on a separate line.
#
#    Examples:
#     echo("apple", "pear", "lime", a="8", b="4", c="3")
#    Outputs:
#     apple and pear and lime
#     a - 8
#     b - 4
#     c - 3
#
#     echo("apple", 4, True, a="pear", b=12, c=False)
#    Outputs:
#     apple and 4 and True
#     a - pear
#     b - 12
#     c - False
#
#     echo("apple")
#    Outputs:
#     apple
#
#     echo(a=8, what="sup")
#    Outputs:
#     a - 8
#     what - sup

def echo(*args, **kwargs):
    # # args stuff
    # args_list = []
    # for things in args:
    #     args_list.append(things)
    # args_list.insert(1, " and ")
    # print(args_list)

    print(args, sep=" and ")

    # kwargs stuff



    # for stuff in kwargs:
    # print(kwargs)
        # print(f"{a} - {pear}")




echo(1, 2, "apple", a="three", b=4)
 


# 4. Create a function called 'breakup' that accepts any number of strings or
#     lists of strings, and a 'sep' argument. Return all the strings and list
#     of strings combined, separated by the string given in 'sep'.
#    Examples:
#     breakup("red", "green", sep=" and ") => "red and green"
#     breakup("red", "green", "pink", sep=" and ") => "red and green and pink"
#     breakup(["red", "green"], sep=" and ") => "red and green"
#     breakup("pink", ["red"], "green", sep=" and ") => "pink and red and green"

