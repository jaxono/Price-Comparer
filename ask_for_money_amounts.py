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


def ask_for_money_amounts():
	while 1:
		# Get max price
		money_max = get_valid_money_amount("How much money do you have that you can spend in dollars? (Eg. 100) ")
		# Make sure that the user has more then $0
		if money_max <= 0:
			print("You need money to shop.")
			continue
		# Get the min price
		money_min = get_valid_money_amount("What is the minimum amount of money that you would want to spend? (Eg. 10) ")
		# Make sure that the minimum amount of money is not larger the maximum
		if money_min > money_max:
			print("You cannot spend a minimum amount of money if it is more than you have.")
			continue
		break
	return money_min, money_max


# ask_for_money_amounts()
