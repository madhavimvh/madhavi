def main():
	n = input()
	dict = {}
	for i in range(int(n)):
		val = input()
		vallis = val.split(" ")
		print(vallis)
		if vallis[0] not in dict:
			dict[vallis[0]]=vallis[1]
		elif vallis[1] not in dict[vallis[0]]:
			dict(vallis[0].append([vallis[1]])
		print(dict)
main()
