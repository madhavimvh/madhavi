def display(adict1):
	per = 0
	for each in sorted(adict1):
		# print(adict1[each])
		for i in range(len(adict1[each]) - 1):
			per = int((adict1[each][i]/adict1[each][i + 1])*100)
			if per < 0:
				per = 0
				print(each + ": " + str(float(per)) + "%")
			else:
				print(each + ": " + str(float(per)) + "%")
				

def main():
	adict = {}
	n = int(input())
	for i in range(n):
		string = input().split("|")
		if string[0] not in adict:
			# print(string[0])
			ques = {}
			if string[2] == string[3]:
				ques[string[1]] = int(string[4])
			else:
				ques[string[1]] = -1*int(string[4])
			# print(ques)
			adict[string[0]] = ques
		else:
			for each in adict:
				if each == string[0]:
					ques = adict[each]
					if string[2] == string[3]:
						ques[string[1]] = int(string[4])
					else:
						ques[string[1]] = -1*int(string[4])



	# print(adict)
	adict1 = {}
	for each in adict:
		maxm = 0
		tot = 0
		ques = adict[each]
		for each1 in ques:
			maxm += ques[each1]
			tot += abs(ques[each1])
		if each not in adict1:
			adict1[each] = [maxm]
			adict1[each].append(tot)
		else:
			for each2 in adict1:
				if each2 == each:
					adict1[each] = [maxm]
					adict1[each].append(tot)

	# print(adict1)
	display(adict1)
main()
