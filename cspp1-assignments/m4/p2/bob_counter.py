'''Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s. For example, if s = 'azcbobobegghakl', then your program should print

Number of times bob occurs is: 2'''

def main():
    s = input()
    n = len(s)
    i = 0
    cou = 0
    while(i<=n):
        if s[i:i+3] == 'bob':
            cou +=1
            i +=1
        else:
            i += 1            
    print(cou)
main()
