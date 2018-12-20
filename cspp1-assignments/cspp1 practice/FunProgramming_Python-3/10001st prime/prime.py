def prime(adict1, number):
	print(adict1[number])


	
def isprime(no):
	count = 0
	for i in range(1, no):
		if no % i == 0 :
			count += 1
	if count == 1:
		return True

def primedict(maxno):
	adict = {}
	j = 0
	i =
	for j in range(maxno):
		while True:
			if isprime(i):
				adict[j] = [i]
				i += 1
				j += 1
	print(adict)
	return adict

def main():
	n = int(input())
	list1 = []
	for i in range(n):
		list1.append(int(input()))
	# print(list1)
	maxno = max(list1)
	# print(maxno)
	adict1 = primedict(maxno)
	# print(adict1)
	for each in list1:
		prime(adict1, each)

if __name__ == "__main__":
    main()