import re
import math

from pip._vendor.packaging._structures import Infinity

TERMINATION_PHRASES = {"xxx", "done", "end", "finish", "finished"}

class Item:
	def __init__(self, price, mass, name, price_per_100g):
		self.price = price
		self.mass = mass
		self.name = name
		self.price_per_100g = price_per_100g

# Function to get the monetary inputs
def get_valid_money_amount(message):
	print(message)
	while 1:
		price = input()
		
		if price == "":
			print("Please enter something.")
			continue
		
		try:
			price = float(price)
		except:
			print("That is not valid input.")
			continue
		break
	return price


# Code starts here
while 1:
	# Get min and max prices
	money_max = get_valid_money_amount("How much money do you have that you can spend: ")
	money_min = get_valid_money_amount("What is the minimum amount of money that you would want to spend: ")
	# Make sure that the minimum amount of money is not larger the maximum
	if money_min > money_max:
		print("You cannot spend a minimum amount of money if it is more than you have.")
		continue
	# Make sure that the user has more then $0
	if money_max <= 0:
		print("You need money to shop.")
		continue
	break
	
items = []

# Get list of ingredients
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
	items.append(Item(item_price, item_mass, item_name.strip(), item_price_per_100g))

# Sort items by weight / 100g
sorted_items = []
sorted_items.append(Item(0, 0, "Placeholder", 0))
for item in items:
	insert_pos = 0
	
	for x in range(len(sorted_items)):
		# Find upper item
		if x >= len(sorted_items) - 1:
			above_price = math.inf
		else:
			above_price = sorted_items[x + 1].price_per_100g
		# Find lower item
		if x == 0:
			below_price = -math.inf
		else:
			below_price = sorted_items[x - 1].price_per_100g
		# Test if it fits in the spot
		if below_price <= item.price_per_100g <= above_price:
			insert_pos = x + 1
			break
	# Insert item
	sorted_items.insert(insert_pos, item)
sorted_items.pop(0)
sorted_items.reverse()


print()
# Show each item
for item in sorted_items:
	item_in_range_str = ""
	if item.price > money_max:
		item_in_range_str = "Too expensive."
	if item.price < money_min:
		item_in_range_str = "Too cheap."
	print(item.name + " at " + str(item.mass) + "g for $" + str(item.price) + ", $" + str(item.price_per_100g) + " per 100g. " + item_in_range_str)
	pass
