# Write a python program to find if the given number is a perfect cube or not
# using guess and check algorithm

# testcase 1
# Input: 24389
# Output: 24389 is a perfect cube

# testcase 2
# Input: 21950
# Output: 21950 is not a perfect cube

def main():
    s = int(input("enter cube"))
    i = 1
    while i**3 <= s:
        i=i+1
    if (i-1)**3 == s:
        print("perfect cube")
    else:
        print("not a perfect cube")
main()
