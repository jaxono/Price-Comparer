import math
import item_class

def sort_and_print(items, money_min, money_max):
	# Sort items by weight / 100g
	sorted_items = []
	sorted_items.append(item_class.Item(0, 0, "Placeholder", 0))
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