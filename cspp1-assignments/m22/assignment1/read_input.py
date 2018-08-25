'''
Write a python program to read multiple lines of text input and store the input into a string.
'''

def main():
    lines_n = input()
    string_n = ""
    for i in range(int(lines_n)):
        string_n += input()
        string_n += '\n'
    print(string_n)
if __name__ == '__main__':
    main()
