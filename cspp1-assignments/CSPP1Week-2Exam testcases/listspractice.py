def  lists(input1):
	summ = 0
	for each in input1:
		print(each)
		if type(each) not in list:
			print("sfll")
			for num in each:
				summ += num
				print(summ)

def main():
	input1 = eval(input())
	# print(input1)
	lists(input1)
main()