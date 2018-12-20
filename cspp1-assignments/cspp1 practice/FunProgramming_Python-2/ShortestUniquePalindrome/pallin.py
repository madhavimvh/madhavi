import sys
def shortestpallin(strig):
	length = sys.maxsize
	# set1 = set()
	# print(sys.maxsize)
	for i in range(len(strig)):
		s = ""
		s += strig[i]
		for j in range(i + 1, len(strig)):
			s += strig[j]
			# print(s)
			if ispallindrome(s):
				if len(s) < length:
					pallin = s
					# set1.add(s)
					length = len(s)
				elif len(s) == length :
					# set1.add(s)
					pallin += ", " + s
	print(pallin)
	return pallin
	# print(set1)
	# return set1

def ispallindrome(str1):
	strrev = str1[::-1]
	if str1 == strrev:
		return True

	# print(strrev)

def main():
	string = input()
	shortestpallin(string)
if __name__ == "__main__":
    main()