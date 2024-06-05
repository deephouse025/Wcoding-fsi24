# 1. Create an empty dictionary called monster. Then add the following properties:
#     "damage" property set to 500
#     "defense" property set to 70
#     "weakness" property set to "water"
monster = {}
monster.setdefault = ("damage", 500)
monster.update = ({"defense", 70})
monster["weakness"] = "water"

#    b. Do it again, all in one line of Python code
monster = {"damage": 500, "defense": 70, "weakness": "water"}

#    c. Set its "name" property to "Gogomish" in a separate line of code
monster["name"] = "Gogmish"

#    d. Print out the monster
print(monster)


# 2. Starting with the dictionary:
boy = {"height": 100, "weight": 250}

#    a. Delete the "height" property from boy
del boy["height"]

#    b. Delete the "weight" property from boy
del boy["weight"]

#    c. Print out the boy
print(boy)