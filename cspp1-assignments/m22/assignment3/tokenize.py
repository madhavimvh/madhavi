'''
Write a function to tokenize a given string and return a dictionary with the frequency of
each word
'''
import re
def tokenize(string):
    string = string.lower().split(" ")
    string_list = []
    string_dic = {}
    for each in range(len(string)-1):
        string_list.append(re.sub("[^a-z]", "", string[each]))
    for word in string_list:
        if word not in string_dic:
            string_dic[word] = string.count(word)
    return string_dic
    
    
            
def main():
    lines = int(input())
    string = ""
    for i in range(lines):
        string += input()
        string += '\n'
        i += 1
    #print(string)
    print(tokenize(string))
        

if __name__ == '__main__':
    main()
