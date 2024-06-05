# 1. Convert the following function to a lambda expression and assign it to
#     a variable called exp.
def exponentiate(base, exponent):
	return base ** exponent
exponentiate(2, 2)
# same as below

print((lambda x, y: x ** y)(2, 2))


# 3. Create a lambda function that adds 15 to a given number passed in
#     as an argument.
print((lambda x: x + 15)(12))


# 4. Create a lambda function that multiplies argument x with argument y
#     and print the result.
print((lambda x, y: x * y)(5, 5))