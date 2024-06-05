# 1. Create an empty new list called all_colors.
all_colors = []

# 2. Add red, orange, yellow, green, blue, and purple to
#     the all_colors list one item at a time.
all_colors.append("red")
all_colors.append("orange")
all_colors.append("yellow")
all_colors.append("green")
all_colors.append("blue")
all_colors.append("purple")



# 3. Unfortunately, purple was not supposed to be in the list. Can you
#     edit the all_colors list to replace purple with 2 other items,
#     indigo and violet, as the last items in the list?
all_colors.remove("purple")
all_colors.append("indigo")
all_colors.append("violet")


# 4. Ask the user for more input: provide 3 more colors, separated by
#     commas. Parse the input appropriately and insert each of the colors
#     into the all_colors list at the end of the list.
# more_colors_input = input("Give 3 more colors: ")
# more_colors = more_colors_input.split(", ")
# all_colors = all_colors + more_colors
# print(all_colors)

# 5. Add a check to make sure the user submitted at least 3 items.
#     If not, print out an appropriate error message to the user and have
#     the Python script run to the end without doing anything more.

# more_colors_input = input("Give 3 more colors: ")
# more_colors = more_colors_input.split(", ")


# if len(more_colors) < 3:
#     print("Error! you input less than 3 colors!")
#     exit()
# else: 
#     all_colors = all_colors + more_colors



# 6. Add a check on inserting the user submitted colors into the list.
#     Only add a user submitted color, if it doesn't already exist
#     in the list.

# more_colors_input = input("Give 3 more colors: ")
# more_colors = more_colors_input.split(", ")

# if (all_colors.contains(more_colors[0])) or (all_colors.contains(more_colors[1])) or (all_colors.contains(more_colors[0])):
#     print("Error! one of these colors is already in the list!")
# else: 
#     if len(more_colors) < 3:
#         print("Error! you input less than 3 colors!")
#     else: 
#         all_colors = all_colors + more_colors



# 7. Again, ask the user to provide 3 colors with one prompt. Do the
#     same input validation (make sure there is at least 3 colors and
#     skip adding any colors that already exist in the all_colors list)
#     but this time add these colors to the front of the list.

more_colors_input = input("Give 3 more colors: ")
more_colors = more_colors_input.split(", ")

if (more_colors[0] in all_colors) or (more_colors[1] in ) or (all_colors.contains(more_colors[0])):
    print("Error! one of these colors is already in the list!")
else: 
    if len(more_colors) < 3:
        print("Error! you input less than 3 colors!")
    else: 
        all_colors = all_colors.insert(0, more_colors[2])
        all_colors = all_colors.insert(0, more_colors[1])
        all_colors = all_colors.insert(0, more_colors[0])

print(all_colors)

# 8. Swap the middle color and the color at the end of the list.
#     If there are an even number of items in the list, bias the
#     middle towards the front of the list. (ie. the middle of four
#     elements would be the second element)

all_colors[4], all_colors[9] = all_colors[9], all_colors[4]
print(all_colors)




# 9. Move the third to last element to the front.

# 10. Move "red" to the back of the all_colors list.

# 11. Ask the user for a number between 1 and the length of the all_colors
#      list. Actually display the length of the list in the prompt, so
#      the user doesn't have to guess the limit. Create a new list called
#      some_colors with this number of colors from the all_colors list.

# 12. Print out the index of "green" in some_colors list. If it is not in
#      the some_colors list, print out a apologetic message to the user
#      that there is no green in the some_colors list.

# 13. Print out the some_colors list on one line, with "ish" added to
#      each color. (For example: "yellowish greenish orangeish ...")
