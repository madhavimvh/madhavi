# Exercise: Assignment-1
# Write a Python function, factorial(n), that takes in one number and
# returns the factorial of given number.

# This function takes in one number and returns one number.

def ispallindrome(s):
   def tochars(s):
    s = s.lower()
    ans = " "
    for c in s:
        if c in "abcdefghijklmnopqrstuvwxyz":
            ans = ans + c
            print(ans)
    return ans

    def ispal(s):
        print(s)
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and ispal(s[1:-1])

    return ispal(s)

    
    
print(ispallindrome("madam"))
