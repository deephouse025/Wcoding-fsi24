# 1. Create a movies list containing a single tuple. 
#     The tuple should contain a movie title, the director’s 
#     name, the release year of the movie, and the movie’s budget.
movies = [("Interstellar", "Christopher Nolan", 2014, "165M")]

#    b. Use an f-string to print the movie name and release year 
#        by accessing your new movie tuple.
print(f"1.b: Movie name: {movies[0][0]}, release year: {movies[0][2]}")

#    c. Add another new movie tuple to the movies collection using append.
movies.append(("1.c: Walter Mitty", "Ben Stiller", 2013, "90M"))

#    d. Print both movies in the movies collection.
for movie in movies:
    print(f"1d: {movie[0]} - {movie[2]}")
print()

#    e. Remove the first movie from movies.
del(movies[0])
print("1e: ", movies)
print()






# 2. Below is a list of tuples, where each tuple contains details about an
#     employee of a shop: their name, the number of hours worked last week,
#     and their hourly rate. Print how much each employee is due to be paid
#     at the end of the week in a nice, readable format.
employees = [
    ("Rolf Smith", 35, 8.75),
    ("Anne Pun", 30, 12.50),
    ("Charlie Lee", 50, 15.50),
    ("Bob Smith", 20, 7.00)
]
for worker in employees:
    print("2a: ", f"{worker[0]}: ${worker[1] * worker[2]}")
# for i in employees:
#     hours = employees[i][1]
#     rate = employees[i][2]
#     name = employees[i][0]
#     print(f"{name}: ${hours * rate}")




#    b. For the employees above, print out those who are earning an hourly
#        wage above average.
all_rates = 0
for worker in employees:
    all_rates += worker[2]
avg_rate = all_rates / len(employees)

results = []
for worker in employees: 
    if worker[2] > avg_rate: 
        results.add(worker[0])

print("2b:", f"Average: ${round(avg_rate)} - Earning above average: {', '.join(results)}")



# total = []
# for i in employees:
#     pay = employees[i]
#     total.append(pay)

# average = total / len(total)





# 3. Consider the following data structure. Remove all the * that do not have a
#     neighboring *. Then print out the number of *'s that remain.
field = [
    "....**....*..***...*",
    "**..*...**...**.*...",
    "*...***...*...****..",
    "...*********......**",
    "****.........*...***",
    "....*.....*....*...."
]

total_stars = 0
for row in field:
    row = row.replace(".*.", "...")
    if row.find("*.") == 0:
        rew = "." + row[1:]
    if row.find(".*", -2) != -1:
        row = row[:-1] + "."

    total_stars += row.count("*")

print("3: Total stars: ", total_stars)




# outer loop for going thru each list item (row)
# i = 0
# while i < len(field):

#     row = field[i]
#     print(row)

#     # inner loop for going thru each character on this row
#     j = 0
#     while j < len(row):
#         this_char = field[i][j]
#         next_char = field[i][j + 1]
#         print("this char = ", this_char)
#         print("next char = ", next_char)

#         if this_char == "*":
#             if next_char != "*":
#                 del(this_char)
        
#         j += 1
#     i += 1
        