def happy(no):
	sqr = 0
	n = 0
	if no == 1:
		return("Happy Number")
	while (no > 0):
		rem = no % 10
		sqr += rem**2
		n = n//10
	no == sqr
	if no != 1:
		happy(no)
		print("Not a Happy Number")


def main():
	n = int(input())
	list1 = []
	for i in range(n):
		inp = int(input())
		list1.append(inp)
	print(list1)
	for j in range(len(list1)):
		print(list1[j])
		happy(list1[j])
if __name__ == "__main__":
    main()	