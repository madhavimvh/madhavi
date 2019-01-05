def listsfloat(string):
	global sum1
	global count
	size = 0
	count = 0
	sum1 = 0
	for each in string:
		if type(each) not in [list]:
			if type(each) not in [str]:
				sum1 += float(each)
			# print("sum" + str(sum1))
		else:
			listsfloat(each)
			count += 1
	if "." in str(sum1):
		sumstr = str(sum1).split(".")
		if sumstr[1] != '0':
			print(sum1)
		else:
			print(int(sum1))
	else:
		print(sum1)
	print(count)

def check(each):
	global sum1
	global count
	for each1 in each:
		if type(each1) not in [list]:
			if type(each1) not in [str]:
				sum1 += float(each1)
		else:
			# print("list")
			check(each1)
			count += 1
	# print(sum1)
# def liststr(string):
# def depth(l):
#     if isinstance(l, list):
#         return 1 + max(depth(item) for item in l)
#     else:
#         return 0
def list_depth(list_of_lists):
    if isinstance(list_of_lists, list):
        if(len(list_of_lists) == 0):
            depth = 1
        else:
            depth = 1 + max([list_depth(l) for l in list_of_lists])
            print(depth)
            print([list_depth(l) for l in list_of_lists])
    else:
        depth = 0
    return depth
def main():
	global string
	string = eval(input())
	listsfloat(string)
	print(list_depth(string))

main()


