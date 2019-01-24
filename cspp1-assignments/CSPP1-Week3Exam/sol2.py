def checklength(adict):
	maxno = 0
	maxno = max(len(x) for x in adict)
	for each in adict:
		if len(each) != maxno:
			return False
	return True
def display(adict1):
	per = 0
	if checklength(adict1):
		for each in sorted(adict1):
			# print(adict1[each])
			for i in range(len(adict1[each]) - 1):
				per = int((adict1[each][i]/adict1[each][i + 1])*100)
				if per < 0:
					per = 0
					print(each + ": " + str(float(per)) + "%")
				else:
					print(each + ": " + str(float(per)) + "%")
	else:
		orddict = sorted(adict1.items(),key=lambda x: (len(x[0]), x))
		s1 = listtodict(orddict)
		for each in s1:
			for i in range(len(adict1[each]) - 1):
				per = int(round((adict1[each][i]/adict1[each][i + 1]))*100)
				if per < 0:
					per = 0
					print(each + ": " + str(float(per)) + "%")
				else:
					print(each + ": " + str(float(per)) + "%")
def listtodict(s):
	orddict = {}
	for each in s:
		orddict[each[0]] = each[1]
	return orddict

def main():
	adict = {}
	n = int(input())
	try:
		for i in range(n):
			string = input().split("|")
			int(string[4])
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
	except ValueError:
		print("Invalid Points")
main()
