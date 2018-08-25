'''
Write a python program to read multiple lines of text input and store the input into a string.
'''
def main():
    "program to take input"
    lines_n = int(input())
    string_n = ""
    for i in range(lines_n):
        string_n += input()
        string_n += '\n'
        i += 1
    print(string_n)
if __name__ == '__main__':
    main()
