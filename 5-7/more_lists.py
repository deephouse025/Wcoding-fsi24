# 1. Create a list of 3 fruits and store it in a variable called "fruits"

fruits = ["apples", "bananas", "strawberries"]

#    b. Check if "apples" is in your list of fruits (True or False)
print("apples" in fruits)

#    c. Append 2 more fruits to your list of fruits
fruits.append("pears")
fruits.append("blueberries")

#    d. Update your fruits variable to contain the values of the original
#       fruits list, but in reverse order
fruits = fruits[::-1]
print(fruits)

#    e. Print the very first in your list of fruits
print(fruits[0])

#    f. Print the 3rd and 4th fruits as a sublist (shorter list)
sublist = (fruits[2], fruits[3])
print(sublist)

#    g. Add the string 'big ' in front of the last item in the list
#       If the lastfruit was "pineapple", update it to be "big pineapple"
fruits[4] = ('big ') + fruits[4]

#    h. Pop off the last fruit in the list and store it in variable big_fruit
big_fruit = fruits.pop(4)

#    i. Print the current length of the fruits list
print(len(fruits))

#    j. Print the length of big_fruit
print(len(big_fruit))


# 2. Create an empty dictionary and store it in the variable shopping_cart.
shopping_cart = {}
#     Then add the following keys:
#     - "items" key should correspond to an empty list
#     - "created_at" key should correspond to today's date as a string
#     - "total" key is the total value of the items in shopping_cart (0)
#     - "recent" key should correspond to True
shopping_cart["items"] = []
shopping_cart["created_at"] = "05/07/2024"
shopping_cart["total"] = 0
shopping_cart["recent"] = True

#    b. Update the "total" in the shopping_cart by increasing it by 5000
shopping_cart["total"] += 5000
print(shopping_cart)

#    c. Update the "items" in the shopping_cart by appending to it big_fruit
shopping_cart["items"].append(big_fruit)

#    d. Check if "big apples" is in the "items" list in your shopping_cart
print("big apples" in shopping_cart["items"])


# 3. Create a dictionary called favorites. It should have...
#    an "items" property that corresponds to ["water", "juice", "bread"]
#    a "total" property that corresponds to 15000
#    a "recent" property that corresponds to False
#    and a "created_at" property that is yesterday's date as a string

favorites = {"items": ["water", "juice", "bread"], "total": 15_000, "recent": False, "created_at": "05/06/2024"}


# 4. Create a dictionary called order. It should have...
#    an "items" property which is the combination of
#         "items" from shopping_cart and
#         "items" from favorites
#    a "total" property which is the sum of
#         "total" from shopping_cart and
#         "total" from favorites
#    a "created_at" property which corresponds to today's date as a string
#    a "recent" property which corresponds to applying logical or to
#         "recent" of shopping_cart and
#         "recent" of favorites

order = {
    "items": (shopping_cart["items"], favorites["items"]),
    "total": (shopping_cart["total"], favorites["total"]),
    "created_at": shopping_cart["created_at"],
    "recent": (shopping_cart["recent"] or favorites["recent"])
}
print(order)