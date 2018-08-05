# Write a python program to find the square root of the given number
# using approximation method

# testcase 1
# input: 25
# output: 4.999999999999998

# testcase 2
# input: 49
# output: 6.999999999999991

def main():
        X = int(input())
        i = 0.01
        LOW = 0
        HIGH = X
        ANS = (HIGH + LOW)/2.0
        while abs(ANS**2 - X) >= i:
            if ANS**2 < X:
                LOW = ANS
            else:
                HIGH = ANS
            ANS = (HIGH + LOW)/2.0
        print(ANS)

main()
