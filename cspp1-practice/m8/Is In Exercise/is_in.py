"""
# Exercise: Is In
# Write a Python function, isIn(char, aStr), that takes in two arguments a 
character and String and returns the isIn(char, aStr) which retuns a boolean value.
# This function takes in two arguments character and String and returns one boolean 
value.
"""
def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    returns: True if char is in aStr; False otherwise
    '''
    a = None
    char = char.lower()
    cStr = aStr.lower()
    bStr = ''.join(sorted(cStr))
    if len(bStr) == 0:
        return "String length cannot be 0."
    elif len(bStr) == 1:
        if char in bStr:
            return True
        return False
    else:
        a = int(len(bStr)/2)
        if char == bStr[a]:
            return True
        else:
            if char < bStr[a]:
                return isIn(char,bStr[:a])
            return isIn(char,bStr[a:])
def main():
    data = input()
    data = data.split()
    print(isIn((data[0][0]), data[1]))
if __name__== "__main__":
    main()