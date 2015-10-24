def matchCorrectAnswer(a,b,pointer):
	correctAnswer = 0
	for index,value in enumerate(a):
		if a[index] == b[index]:
			correctAnswer = correctAnswer + 1
	return correctAnswer


T = int(raw_input())
answer = []
response = []
winList = []
for i in range(0,T):
	questionLength = int(raw_input())
	answer.append(list(raw_input()))
	response.append(list(raw_input()))
	winList.append([long(x) for x in raw_input().split()])

for j in range(0,T):
	maxAns = matchCorrectAnswer(answer[j],response[j],0)
	if maxAns!=len(answer[j]) and maxAns!=0: 
		allPoints = winList[j][:maxAns+1]
		print max(allPoints)
	elif maxAns == 0:
		print winList[j][0]
	elif maxAns == len(answer[j]):
		print winList[j][maxAns]


	