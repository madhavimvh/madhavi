def add(a, b):
	if m !=  m1 and n != n1:
		print("Matrix addition not possible.")
		return
	c = [0]*m
	for each in range(len(c)):
		c[each] = [0]*n
	if m == m1 and n == n1:
		for i in range(m):
			for j in range(n):
				c[i][j] = int(a[i][j]) + int(b[i][j])
	for each in c:
		strg = ""
		for each1 in each:
			strg += str(each1) + " "
		print(strg)

def subtract(a, b):
	if m != m1 and n != n1:
		print("Matrix subtraction not possible.")
		return
	c = [0]*m
	for each in range(len(c)):
		c[each] = [0]*n
	if m == m1 and n == n1:
		for i in range(m):
			for j in range(n):
				c[i][j] = int(a[i][j]) - int(b[i][j])
	for each in c:
		strg = ""
		for each1 in each:
			strg += str(each1) + " "
		print(strg)

def transpose(list3):
	c = [0]*len(list3[0])
	# print(c)
	for i in range(len(c)):
		c[i] = [0]*len(list3)
	# print("ldk")
	# print(c)
	# c = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
	for i in range(len(list3)):
		for j in range(len(list3[0])):
			c[j][i] = list3[i][j]
	for each in c:
		strg = ""
		for each1 in each:
			strg += each1 + " "
		print(strg)
def det(l):
	if len(l) != len(l[0]):
		print("Determinant not possible.")
		return
	size = len(l)
	if (size > 2):
		i = 1
		t = 0
		sum1 = 0
		while t <= size - 1:
			d = {}
			t1 = 1
			while t1 <= size - 1:
				m = 0
				d[t1] = []
				while m <= size - 1:
					if (m == t):
						u = 0
					else:
						d[t1].append(l[t1][m])
					m += 1
				t1 += 1
			l1 = [d[x] for x in d]
			sum1 = sum1+i*(int(l[0][t]))*(det(l1))
			i = i*(-1)
			t += 1
		return sum1
	else:
		return (int(l[0][0])*int(l[1][1]) - int(l[0][1])*int(l[1][0]))



	

def main():
	order = input().split(" ")
	global m
	global n
	m = int(order[0])
	n = int(order[1])
	list1 = []
	for i in range(m):
		s = input()
		list1.append(s.split(" "))
	order1 = input().split(" ")
	global m1
	global n1
	m1 = int(order1[0])
	n1 = int(order1[1])
	list2 = []
	for j in range(m1):
		s1 = input()
		list2.append(s1.split(" "))
	# print(list1)
	# print(list2)
	str1 = ""
	x = int(input())
	for i in range(x):
		str1 += input() + '\n'
	str2 = str1.split('\n')
	# print(str2)
	for i in range(len(str2) - 1):
		# print(each)
		string = str2[i].split()
		# print(string)
		if string[0] == "Add":
			print("Addition")
			add(list1, list2)
		elif string[0] == "Subtract":
			print("Subtraction")
			subtract(list1, list2)
		elif string[0] == "Transpose":
			print("Transpose")
			if string[1] == "A":
				transpose(list1)
			else:
				transpose(list2)
		elif string[0] == "Determinant":
			print("Determinant")
			if string[1] == "A":
				if det(list1) != None:
					print(det(list1))
			else:
				if det(list1) != None:
					print(det(list2))
if __name__ == "__main__":
    main()
		