def addProfitCost(value, multiply=1.20):
	try:
		value = int(value)
		import math
		temp = int(math.floor(value*multiply/100)+1)*100
	except (ValueError, TypeError):
		temp = value
	return temp

print addProfitCost(5653)
