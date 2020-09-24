import re
import item_class

TERMINATION_PHRASES = {"xxx", "done", "end", "finish", "finished"}

items = []

# Get list of ingredients
print("""
Now you will need to enter a list of the items you would like to compare, type done when you are finished.
Eg.
5 6 SuperBrand Plain Flour
4 8 GoodBrand Self Raising Flour
12 3 ExpensiveFoodCo Flour
done
""")

def get_ingrediants():
	while 1:
		# Get ingredient text
		item = input("Enter ingredient: ").strip().lower()
		# Check if it is in the list of phrases that will end the loop
		if item in TERMINATION_PHRASES:
			break
		# Separate input
		try:
			item = re.split(" +", item)
			item_price = float(item[0])
			item_mass = float(item[1])
		except ValueError:
			print("The price and/or weight is not a valid real number.")
			continue
		except IndexError:
			print("You have not entered the price and/or weight and/or name correctly.")
			continue
		except Exception:
			print("Syntax error.")
			continue
		item_name = ""
		for nameWord in item[2:]:
			item_name += nameWord.title() + " "
		if item_name == "":
			print("Your item does not have a valid name")
		item_price_per_100g = item_price / item_mass * 100
		# Store data in array
		items.append(item_class.Item(item_price, item_mass, item_name.strip(), item_price_per_100g))
	return items
