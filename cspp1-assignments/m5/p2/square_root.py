# Write a python program to find the square root of the given number
# using approximation method

# testcase 1
# input: 25
# output: 4.999999999999998

# testcase 2
# input: 49
# output: 6.999999999999991

def main():
	"'#finding the square root of the given number'"
SQUARE = int(input())
i = 0.1
GUESS = 0
j = 0.1
while abs(GUESS**2 - SQUARE) >= i and GUESS <= SQUARE:
    GUESS += j
if abs(GUESS**2 - SQUARE) >= i:
    print('Failed on square root of', SQUARE)
else:
    print(str(GUESS))
main()
