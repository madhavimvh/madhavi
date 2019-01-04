def main():
	line = input().replace("[","").replace("]","")
	list1 = list(line.split(","))
	num = int(input())
	# print(list1)
	result = list1[num:] + list1[:num]
	print(result)
	
if __name__ == "__main__":
    main()