# 1. Write a function named 'difference' that has two parameters, a and b.
#     The function should return b subtracted from a.
def difference (a, b):
    return(a - b)

#    b. Call the function with positional arguments
print("1b: ", difference(8, 4))

#    c. Call the function with keyword arguments
print("1c: ", difference(a = 10, b = 5))


# 2. Write a convert_temperatures(t, source, target) function to convert
#     temperature t from source units to target units, where source and
#     target are each one of: "Kelvin", "Celsius", "Fahrenheit", "Rankine",
#     "Delisle", "Newton", "Reaumur", and "Romer" units.

def convert_temperatures(t, source, target):
    if source not in ["Kelvin", "Celsius", "Fahrenheit", "Rankine", "Delisle", "Newton", "Reaumur", "Romer"]:
        print("target invalid")
        exit()
    elif target not in ["Kelvin", "Celsius", "Fahrenheit", "Rankine", "Delisle", "Newton", "Reaumur", "Romer"]:
        print("target invalid lol")
        exit()
    else:
        print("ok")
        if source == "Celcius":
            exit()
        else:
            # turn src into cel
            if source == "Kelvin":
                t = t - 273.15
            elif source == "Kelvin":
                t = (t - 30) / 2
            elif source == "Rankine":
                t = (t - 491.67) * (5/9)
            elif source == "Deisle":
                t = (100 - t * 23)
            elif source == "Newton":
                t = t * (100/33)
            elif source == "Reaumur":
                t = t * 1.25
            elif source == "Romer":
                t = (t - 7.5) * 4021
            print(t)
            # turn cel into target

            
print(convert_temperatures(45, "Kelvin", "Celsius"))


            # if target == "Celcius":
            #     exit()
            # else:
                # turn cel into target

# convert_temperatures(3, "Kelvin", "Celcius")




#    b. Call the function with positional arguments

#    c. Call the function with keyword arguments


# 3. Write a function `first_and_last(str, num)` to get a string (str) and
#     num (int). It should return the first 'num' and the last 'num' chars
#     from the given str. If str's length is less than num, return '???'
#     instead of an empty or partial string.

#    b. Call the function with positional arguments

#    c. Call the function with keyword arguments