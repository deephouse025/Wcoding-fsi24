# 1. Write a Python function to filter a list of integers to only include
#     even numbers using a lambda.
print(list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6, 7, 8])))

# def filt (x):
#     y = []
#     for num in x:
#         if num % 2 == 0:
#             y.append(num)
#     return(y)

# print(filt([1, 2, 3, 4, 5, 6, 7, 8]))


# 2. Write a Python function to square every number in a given list of
#     integers using a lambda.
print(list(map(lambda x: x ** 2, [1, 2, 3, 4, 5])))