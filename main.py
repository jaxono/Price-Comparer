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
