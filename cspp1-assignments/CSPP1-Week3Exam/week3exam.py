from collections import OrderedDict
def checklength(adict):
	maxno = 0
	maxno = max(len(x) for x in adict)
	for each in adict:
		if len(each) != maxno:
			return False
	return True

def display(adict, adict1):
	score = 0
	if checklength(adict):
		for key1 in sorted(adict):
			for key2 in sorted(adict1):
				if key1 == key2:
					# print(adict[key1], adict1[key2])
					score = int((adict[key1]/adict1[key2])*100)
					if score < 0:
						score = 0
					print(key1 + ": " + str(float(score)) + "%")
	else:
		s = sorted(adict.items(),key=lambda x: (len(x[0]), x))
		s1 = sorted(adict1.items(),key=lambda x: (len(x[0]), x))
		# print(adict)
		# print(adict1)
		# print("-------")
		orddict2 = listtodict(s)
		orddict3 = listtodict(s1)
		print(orddict2)
		print(orddict3)
		for key1 in orddict2:
			for key2 in orddict3:
				if key1 == key2:
					# print(adict[key1], adict1[key2])
					score = int((orddict2[key1]/orddict3[key2])*100)
					if score < 0:
						score = 0
					print(key1 + ": " + str(float(score)) + "%")	

def listtodict(s):
	orddict1 = {}
	for each in s:
		# print(each[0], each[1])
		orddict1[each[0]] = each[1]
	# print(orddict1)
	return orddict1
def displaynew(adict, adict1):
	adictx = {}
	if checklength(adict):
		for each in sorted(adict):
			# print(each)
			for eachx in sorted(adict1):
				# print(eachx)
				total = 0
				if each == eachx:
					adictx = adict[each]
					# print(adictx)
					for each1 in adictx:
						total += int(adictx[each1])
					score = int((total/adict1[eachx])*100)
					if score < 0:
						score = 0
					print(each + ": " + str(float(score)) + "%")
	else:
		s = sorted(adict.items(),key=lambda x: (len(x[0]), x))
		s1 = sorted(adict1.items(),key=lambda x: (len(x[0]), x))
		# print(adict)
		# print(adict1)
		# print("-------")
		orddict2 = listtodict(s)
		orddict3 = listtodict(s1)
		# print(orddict2)
		# print(orddict3)
		for key1 in orddict2:
			for key2 in orddict3:
				total = 0
				if key1 == key2:
					adictx = orddict2[key1]
					for each1 in adictx:
						total += int(adictx[each1])
					# print(adict[key1], adict1[key2])
					score = int(round((total/orddict3[key2]), 2)*100)
					if score < 0:
						score = 0
					print(key1 + ": " + str(float(score)) + "%")

def main():
		adict = {}
		adict1 = {}
		ques = {}
		n = int(input())
		# try:
		# 	for i in range(n):
		# 		string = input().split("|")
		# 		int(string[4])
		# 		if string[0] not in adict:
		# 			ques = {}
		# 			adict[string[0]] = 0
		# 			adict1[string[0]] = int(string[4])
		# 		else:
		# 			adict1[string[0]] += int(string[4])
		# 		if string[2] == string[3]:
		# 			adict[string[0]] += int(string[4])
		# 		else:
		# 			adict[string[0]] -= int(string[4])
		# 	# print(adict)
		# 	# print(adict1)
		# 	display(adict, adict1)
		# except ValueError:
		# 	print("Invalid Points")
		try:
			for i in range(n):
				string = input().split("|")
				int(string[4])
				if string[0] not in adict:
					ques = {}
					if string[2] == string[3]:
						ques[string[1]] = int(string[4])
						adict[string[0]] = ques
						# adict1[string[0]] = int(string[4])
						# print(adict1)
						# print("--------")
					else:
						ques[string[1]] = (-1*int(string[4]))
						adict[string[0]] = ques
						# adict1[string[0]] = int(string[4])
						# print(adict1)
						# print("------------------")

				else:
					# if string[1] not in ques:
						# adict1[string[0]] += int(string[4])
					# print(adict1)
					for each in adict:
						if each == string[0]:
							if string[2] == string[3]:
								ques = adict[string[0]]
								ques[string[1]] = int(string[4])
							else:
								ques = adict[string[0]]
								ques[string[1]] = (-1*int(string[4]))



			# print(adict)
			for no in adict:
				tot = 0
				temp = adict[no]
				for q in temp:
					tot += abs(int(temp[q]))
				adict1[no] = tot
					
			# print(adict1)
			displaynew(adict, adict1)

		except ValueError:
			print("Invalid Points")
main()
