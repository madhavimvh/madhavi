'''
Write a function to tokenize a given string and return a dictionary with the frequency of
each word
'''
import re
def tokenize(string):
    "program to dictionary"
    string_1 = string.split(" ")
    #print("s",string_1)
    string_list = []
    string_dic = {}
    for each in range(len(string_1)):
        string_list.append(re.sub("[^a-z,A-Z,0-9]", "", string_1[each]))
    #print("ss",string_list)
    for word in string_list:
        if word not in string_dic:
            string_dic[word] = 1
            #print("d",string_dic)
        else:
            string_dic[word] += 1
    #print("dd",string_dic)
    return string_dic
def main():
    "program to accept input"
    lines = int(input())
    string = ""
    for i in range(lines):
        string += input()
        string += '\n'
        i += 1
    for each in string:
        if each == '\n':
            string.replace(each, "")
    #print(string)
    print(tokenize(string))
        

if __name__ == '__main__':
    main()
