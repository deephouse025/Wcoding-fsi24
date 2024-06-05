# Variables population and land_area refer to floats.
population = 1_000_000
# 1. Write an if statement that will print the population 
#    if it is less than 10,000,000.
if population < 10_000_000:
    print(population, "is less that 10M")

# 2. Write an if statement that will print the population 
#    if it is between 10,000,000 and 35,000,000.
if 10_000_000 < population < 35_000_000:
    print(population, "is between 10M and 35M")

# 3. Write an if statement that will print “Densely populated” 
#    if the land density (number of people per unit of area) is 
#    greater than 100.
land_density = 50
if land_density > 100:
    print("Densely populated")

# 4. Write an if statement that will print “Densely populated” 
#    if the land density (number of people per unit of area) 
#    is greater than 100, and “Sparsely populated” otherwise.
if land_density > 100:
    print("Densely populated")
else:
    print("Sparsely populated")

# 5. Write a Python program to add 'ing' at the end of a given 
#    string (length should be at least 3). If the given string 
#    already ends with 'ing' then add 'ly' instead. If the string 
#    length of the given string is less than 3, leave it unchanged.
given_string = "buss"
if len(given_string)>= 3:
    if given_string.endswith("ing"):
        print(given_string + "ly")
    else: 
        print(given_string + "ing")
else:
    print(given_string)