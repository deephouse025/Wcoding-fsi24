# Create a class called Country that has properties for name, population,
# language, and in_europe. Make sure that 'name' is always has a value,
# and 'population' can not be set to a number less than 0. The 'in_europe'
# property must be a boolean and defaults to False. Only the 'language'
# property can be deleted from a Country object.
class Country:
    def __init__(self, name, population, language):
        self.name = name
        self.population = max(0, population)
        self.language = language
        self.in_europe = bool(in_europe)

# Add the appropriate getters and setters for the behavior outlined above,
# and add an additional method called 'grow_pop' that accepts a 'rate'
# argument that will accept a float between -1 and 1 and change the
# Country object's population appropriately.
# EXAMPLE (assume 'spain' is a Country object with population of 1000):
# spain.grow_pop(0.05)  # spain's population is now 1050
    
    

# Also include a 'show_lore' function for each object that prints out
# a string in the following format: "<coutry name> is a <terrain>-based
# entity with <population> souls."

# All Country objects share a 'terrain' property set to the string "land".
# Create a method that is shared by all the objects called 'show_kind'
# that prints out "All countries are based on " followed by the current
# value of the 'terrain' property.

# Create at least 5 countries of your choosing, with at least 3 of them
# being in Europe, with the appropriate properties.

# Simulate 1000 years of passing time by adjusting each countries'
# population with a random growth rate annually. Then print out each
# country and their resulting population in the following format:
#  === Population after 1000 years ===
#  <country1 name>: <country1 population>
#  <country2 name>: <country2 population>
#  ... etc.

# Call 'show_lore' for the country with the highest population.

# Then call 'show_lore' for only those countries that are in Europe, that
# still have a population greater than the population they started with
# 1000 years ago.

# Set the terrain property of the Country class to "water" and call 'show_lore'
# with the last country you created. Did it get updated appropriately? Can you
# set just the last country's terrain property to 'fire'? Call the 'show_kind'
# method to show the current value of the terrain for the class to confirm
# that the class is still set to "water".