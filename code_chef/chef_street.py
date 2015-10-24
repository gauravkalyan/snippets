inputList = [int(x) for x in raw_input().split()]
street = [int(x) for x in raw_input().split()]

first = inputList[0]%inputList[1]
product = street[0]%1000000007
if first >1:
	product = product*street[first-1]%1000000007
while(first + inputList[1]<=inputList[0]):
	first = first + inputList[1]
	product = product*street[first-1]%1000000007
print product
