def main():
	order = input().split(" ")
	m = int(order[0])
	n = int(order[1])
	list1 = []
	for i in range(m):
		s = input()
		list1.append(s.split(" "))
	order1 = input().split(" ")
	m1 = int(order[0])
	n1 = int(order[1])
	list2 = []
	for j in range(m1):
		s1 = input()
		list2.append(s1.split(" "))
	print(list1)
	print(list2)
if __name__ == "__main__":
    main()
		