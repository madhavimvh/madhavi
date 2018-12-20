def main():
	list1 = input().replace("[","").replace("]","")
	if list1 == "":
		print("[]")
		return
	list2 = list1.split(",")
	list2.sort()
	# print(list2)
	list3 = []
	if len(list2) == 1:
		list3.append(list2[0])
		list3.append(list2[0])
	else:
		list3.append(int(list2[len(list2) - 2]))
		list3.append(int(list2[1]))
	print(list3)
if __name__ == "__main__":
    main()