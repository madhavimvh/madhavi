def listsfloat(string):
	global sum1
	global count
	count = 0
	sum1 = 0
	for each in string:
		if type(each) not in [list]:
			sum1 += float(each)
			# print("sum" + str(sum1))
		else:
			check(each)
			count += 1
	if "." in str(sum1):
		sumstr = str(sum1).split(".")
		if sumstr[1] != 0:
			print(sum1)
		else:
			print(int(sum))
	else:
		print(sum1)
	print(count)

def check(each):
	global sum1
	global count
	for each1 in each:
		if type(each1) not in [list]:
			# print(each1)
			sum1 += float(each1)
		else:
			# print("list")
			check(each1)
			count += 1
	# print(sum1)
def main():
	global string
	string = eval(input())
	# print(string)
	listsfloat(string)

	

main()


