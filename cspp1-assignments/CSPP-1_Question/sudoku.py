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
			checkduplicates(temp)
	# print(list1)
	# print(getColumnValues(0, list1))
	# print(getGridValues(0, 8, list1))
	possibleValues(list1)
							

def checkduplicates(temp):
	list2 = []
	for no in temp:
		if no not in list2:
			list2.append(no)
		else:
			raise Exception("duplicates are present")
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
	for row in range(i, i + 3):
		# print(row)
		# print("ij")
		for col in range(j - 2, j + 1):
			# print(colss)
			gridvals.append(list1[row][col])
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
				possibilities(i, j, list1)

def possibilities(i , j, list1):
	numbers = [1,2,3,4,5,6,7,8,9]
	possible = []
	rowvals = getRowValues(i, list1)
	inti1 = converttoint(getRowValues(i, list1))
	# print(inti1)
	inti2 = converttoint(getColumnValues(j, list1))
	str1 =""
	for each in numbers:
		if each not in inti1:
			# print(each)
			if each not in inti2:
				# print(i)
				# print("dls")
				# print(j)
				# if each not in getGridValues(i, j, list1):
					possible.append(each)
	str1 = list(map(str, possible))
	str1 = ''.join(str1)
	print(str1)
	return str1

def converttoint(listx):
	strrow = ''.join(listx)
	strrow = strrow.replace(".","")
	strrow = list(strrow)
	inti = list(map(int,strrow))
	return inti


	
"""
Read the input and store the values in an appropriate data sturcture.
Then travese through each value, if you get a "." then collect the possible values
"""
def main():
	string = input()
	validateSudoku(string)

if __name__ == "__main__":
    main()