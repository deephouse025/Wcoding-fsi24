x = True
y = False

if x == True and y == True:
    print("True")
else:
    print("False")


if x == False:
    print("True")
else:
    print("False")


if x == True or y == True:
    print("True")
else:
    print("False")

empty = False
full = True

if (full and not empty) or (not full and empty):
    print("Valid")