inputList = [int(x) for x in raw_input().split()]
street = [int(x) for x in raw_input().split()]

k = inputList[1]

minWeight = []
minWeight.append(street[0])
i=1
while(i<len(street)):
	weight = 1
	temp = 0
	if k < i:
		subList = minWeight[-k:]
		temp = min(subList)
	else:
		temp = min(minWeight)	
	minWeight.append(temp*street[i])
	i+=1
print minWeight[-1]%1000000007
