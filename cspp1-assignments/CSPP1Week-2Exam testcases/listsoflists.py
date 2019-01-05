def main():
	global string
	string = input().split()
	print(string)
	list1 = []
	list2 = []
	for i in range(len(string) - 1):
		if string[i] == '[':
			num = check(string[i + 1], i + 1)
			a = num + 1
			while True:
				list2.append(string[a])
				a = a + 1
				if string[a] == ']':
					list1.append(list2)
					list2 = []
					break
	print(list1)

main()
def check(string, i):
	if '[' in string:
		a = i + 1
		check(string[a], a)
	else:
		return i


