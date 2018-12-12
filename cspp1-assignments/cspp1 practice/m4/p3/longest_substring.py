'''Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which the letters occur in alphabetical order.
For example, if s = 'azcbobobegghakl', then your program should print

Longest substring in alphabetical order is: beggh

In the case of ties, print the first substring.
For example, if s = 'abcbcd', then your program should print

Longest substring in alphabetical order is: abc

Note: This problem may be challenging. We encourage you to work smart.
If you've spent more than a few hours on this problem, we suggest that you move on to a different part of the course.
If you have time, come back to this problem after you've had a break and cleared your head.'''

def main():
    s = input("Please enter a sentence: ")
    c = ""
    d = ""
    e = ""
    for i in s:
            if c <= i:
                    c = i
                    d += c
                    if len(d) > len(e):
                            e = d
            else:
                    c = i
                    d = c
    print(e)
if __name__== "__main__":
	main()
