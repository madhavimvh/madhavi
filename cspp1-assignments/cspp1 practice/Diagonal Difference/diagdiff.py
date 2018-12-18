def diagdiff(list1, n):
	d1 = 0
	d2 = 0
	diff = 0
	for i in range(n):
		d1 += int(list1[i][i])
		d2 += int(list1[i][n - i - 1])
	diff = abs(d1 - d2)
	return diff






def main():
	n = int(input())
	if n == 0 or n < 0:
		print("Matrix can't be formed.")
		return
	list1 = []
	for i in range(n):
		inp = input()
		list1.append(inp.split())
	# print(list1)
	print(diagdiff(list1, n))
if __name__ == "__main__":
    main()