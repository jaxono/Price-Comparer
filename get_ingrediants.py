import re
import item_class

TERMINATION_PHRASES = {"xxx", "done", "end", "finish", "finished"}

def get_ingrediants():
	items = []
	
	# Get list of ingredients
	print("""
Now you will need to enter a list of the items you would like to compare, type done when you are finished.
""")

	while 1:
		item_name = input("Enter name of product: ").strip().title()
		if item_name.lower() in TERMINATION_PHRASES:
			break
		try:
			item_price = float(input("Enter price of product in $: ").strip())
			item_mass = float(input("Enter price of product in grams: ").strip())
		except ValueError:
			print("That is not a valid real number.")
			continue
		item_price_per_100g = item_price / item_mass * 100
		# Store data in array
		print("Added {} at ${} for {}g".format(item_name, item_price, item_mass))
		items.append(item_class.Item(item_price, item_mass, item_name, item_price_per_100g))
	return items


#get_ingrediants()
