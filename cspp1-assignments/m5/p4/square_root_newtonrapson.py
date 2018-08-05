# Write a python program to find the square root of the given number
# using approximation method

# testcase 1
# input: 25
# output: 4.999999999999998

# testcase 2
# input: 49
# output: 6.999999999999991

def main():
	"'#finding square of a number using newton rapson'"
i = 0.01
Y = int(input())
GUESS = Y/2.0
while abs(GUESS*GUESS - Y) >= i:
    GUESS = GUESS - (((GUESS**2) - Y)/(2*GUESS))
print(GUESS)
main()
