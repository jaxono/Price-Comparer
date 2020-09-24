import ask_for_money_amounts # Actually no errors, the IDE is just glitching.
import get_ingrediants
import sort_and_print

# Code starts here

# Print instructions
print("""This program is designed to compare a list of products and tell you which ones are the most expensive and cheapest per 100g.
First you will need to answer some questions then you can enter your list of items.
""")

# Get the min and max money the user has.
money_min, money_max = ask_for_money_amounts.ask_for_money_amounts()
# Get ingredients.
items = get_ingrediants.get_ingrediants()
# Sort and print.
sort_and_print.sort_and_print(items, money_min, money_max)
