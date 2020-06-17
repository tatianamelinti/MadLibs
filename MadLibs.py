# The template for the story

STORY = "This morning %s woke up feeling %s. It is going to be a %s day! Outside, a bunch of %s were protesting to keep %s in stores. They began to %s to the rhythm of the %s, which made all the %s very %s. Concerned, %s texted %s, who flew %s to %s and dropped %s in a puddle of frozen %s. %s woke up in the year %s, in a world where %s ruled the world."
print ("Mad Libs has started")
name = input("Enter a name: ")
adj1 = input("Enter an adjectiv: ")
adj2 = input("Enter an adjectiv: ")
adj3 = input("Enter an adjectiv: ")
verb = input("Enter a verb: ")
noun1 = input("Enter a noun: ")
noun2 = input("Enter a noun: ")
animal = input("Enter an animal: ")
food = input("Enter a food: ")
fruit = input("Enter a fruit: ")
superhero = input("Enter a superhero: ")
country = input("Enter a country: ")
dessert = input("Enter a dessert: ")
year = input("Enter a year: ")
print (STORY % (name, adj1, adj2, animal, food, verb, noun1, fruit, adj3, name, superhero, name, country, name, dessert, name, year, noun2))
