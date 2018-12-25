"""
In this method :
 * Check there are only 81 values
 * iterate through each row in the sudoku and if you find any duplicate values
 	raise an exception
 * iterate through each column in the sudoku and if you find any duplicate values
	raise an exception
 * iterate through each subgrid(3x3) in the sudoku and if you find any duplicate values
	raise an exception
"""
def validateSudoku(sudoku):
	list1 = []
	temp = []
	count = 0
	if len(sudoku) == 81:
		for i in range(len(sudoku)):
			if i % 9 == 0 and i!=0:
				list1.append(temp)
				temp = []
			temp.append(sudoku[i])
			# print(temp)
		list1.append(temp)
	else:
		raise Exception("Invalid input")
	# print(list1)
	if (sudoku.count('.') == -1):
		raise Exception("Given sudoku is solved")


	# print(getColumnValues(0, list1))
	# print(getGridValues(0, 8, list1))
	possibleValues(list1)

							

def checkduplicates(temp):
	list2 = []
	for no in temp:
		if no != ".":
			if no not in list2:
				list2.append(no)
			else:
				raise Exception("Invalid Sudoku:Duplicate values")
				return
"""
This  method should retunn all the values present in the ith row
"""
def getRowValues(i, list1):
	return list1[i]


"""
This  method should retunn all the values present in the ith column
"""
def getColumnValues(i, list1):
	column = []
	for row in list1:
		column.append(row[i])
	# print(column)
	return column


"""
This  method should retunn all the values present in the i,j th subgrid
"""
def getGridValues(i, j, list1):
	gridvals = []
	if (i >= 0 and i < 3) and (j >= 0 and j < 3):
		for subrow in range(0, 3):
			for subcol in range(0, 3):
				gridvals.append(list1[subrow][subcol])
	if (i >= 0 and i < 3) and (j >= 3 and j < 6):
		for subrow in range(0, 3):
			for subcol in range(3, 6):
				gridvals.append(list1[subrow][subcol])
	if (i >= 0 and i < 3) and (j >= 6 and j < 9):
		for subrow in range(0, 3):
			for subcol in range(6, 9):
				gridvals.append(list1[subrow][subcol])
	if (i >= 3 and i < 6) and (j >= 0 and j < 3):
		for subrow in range(3, 6):
			for subcol in range(0, 3):
				gridvals.append(list1[subrow][subcol])
	if (i >= 3 and i < 6) and (j >= 3 and j < 6):
		for subrow in range(3, 6):
			for subcol in range(3, 6):
				gridvals.append(list1[subrow][subcol])
	if (i >= 3 and i < 6) and (j >= 6 and j < 9):
		for subrow in range(3, 6):
			for subcol in range(6, 9):
				gridvals.append(list1[subrow][subcol])
	if (i >= 6 and i < 9) and (j >= 0 and j < 3):
		for subrow in range(6, 9):
			for subcol in range(0, 3):
				gridvals.append(list1[subrow][subcol])
	if (i >= 6 and i < 9) and (j >= 3 and j < 6):
		for subrow in range(6, 9):
			for subcol in range(3, 6):
				gridvals.append(list1[subrow][subcol])
	if (i >= 6 and i < 9) and (j >= 6 and j < 9):
		for subrow in range(6, 9):
			for subcol in range(6, 9):
				gridvals.append(list1[subrow][subcol])


	# print(gridvals)
	return gridvals


	
"""
This method should collect all the available values present for a "."
You should get the values present in row,column,grid.
Then you should return the values that doesnot exist in the previous values.
"""
def possibleValues(list1):
	for i in range(len(list1)):
		for j in range(len(list1[0])):
			if list1[i][j] == ".":
				checkduplicates(getRowValues(i, list1))
				checkduplicates(getColumnValues(i, list1))
				checkduplicates(getGridValues(i, j, list1))
				possibilities(i, j, list1)

def possibilities(i , j, list1):
	# for x in list1:
	# 	print(x)
	numbers = [1,2,3,4,5,6,7,8,9]
	possible = []
	# print(getRowValues(i, list1))
	inti1 = converttoint(getRowValues(i, list1))
	inti2 = converttoint(getColumnValues(j, list1))
	# print(inti1)
	# print("col")
	# print(inti2)
	# print("sub")
	inti3 = converttoint(getGridValues(i, j, list1))
	# print(inti3)
	str1 =""
	for each in numbers:
		if each not in inti1:
			# print(each)
			if each not in inti2:
				# print(i)
				# print("dls")
				# print(j)
				if each not in inti3:
					possible.append(each)
	# print(possible)
	str1 = list(map(str, possible))
	str1 = ''.join(str1)
	print(str1)
	return str1

def converttoint(listx):
	strrow = ''.join(listx)
	strrow = strrow.replace(".", "")
	strrow = list(strrow)
	inti = list(map(int, strrow))
	return inti


	
"""
Read the input and store the values in an appropriate data sturcture.
Then travese through each value, if you get a "." then collect the possible values
"""
def main():
	string = input()
	try:
		validateSudoku(string)
	except Exception as e:
				print(e)

if __name__ == "__main__":
    main()