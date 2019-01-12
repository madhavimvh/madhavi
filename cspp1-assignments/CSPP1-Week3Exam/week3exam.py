def display(adict, adict1):
	score = 0
	for key1 in sorted(adict):
		for key2 in sorted(adict1):
			if key1 == key2:
				# print(adict[key1], adict1[key2])
				score = int((adict[key1]/adict1[key2])*100)
				print(key1 + ": " + str(float(score)) + "%")
def main():
	adict = {}
	adict1 = {}
	n = int(input())
	for i in range(n):
		string = input().split("|")
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


main()
