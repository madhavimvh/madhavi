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
		# print(orddict2)
		# print(orddict3)
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

def main():
		adict = {}
		adict1 = {}
		n = int(input())
		try:
			for i in range(n):
				string = input().split("|")
				int(string[4])
				if string[0] not in adict:
					adict[string[0]] = 0
					adict1[string[0]] = int(string[4])
				else:
					adict1[string[0]] += int(string[4])
				if string[2] == string[3]:
					adict[string[0]] += int(string[4])
				else:
					adict[string[0]] -= int(string[4])
			# print(adict)
			# print(adict1)
			display(adict, adict1)
		except ValueError:
			print("Invalid Points")

main()
