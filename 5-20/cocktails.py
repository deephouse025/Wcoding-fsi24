# Ask the user for the name of a cocktail. Then use the Cocktails DB
# (https://www.thecocktaildb.com/) to get data about the drink. List
# all the ingredients on separate lines sorted alphabetically. Then,
# below the ingredients, show the directions on how to make the
# cocktail. (English) If the cocktail name does not exist then let the
# user know. Regardless, ask again for another cocktail name. If the
# user types 'q', then stop asking and end the program.


# user_search = input("Cocktail name: ")
import requests

def drink_data (drink):
    a = requests.get("https://www.thecocktaildb.com/api/json/v1/1/search.php?s=" + drink)
    drink_page = a.json()
    # print(drink_page)
    all_ingredients = []
    for i in 15:
        if strIngredient != none:
            
    print(all_ingredients)



    # print(directions)
    # if has_name = True:
    #     print(name)

drink_data("gin and tonic")
# drink_data(user_search)