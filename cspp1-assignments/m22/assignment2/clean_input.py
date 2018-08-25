'''
Write a function to clean up a given string by removing the special characters and retain 
alphabets in both upper and lower case and numbers.
'''
import re
def clean_string(string):
    string_1 = []
    string = string.lower().split(" ")
    #print("s",string)
    for each in string:
        #print(each)
        string_1.append(re.sub("[^a-z]","",each))
    string_11 = ''.join(string_1)
    #print("ss",string_11)
    
    return string_11
    
def main():
    string = input()
    print(clean_string(string))
if __name__ == '__main__':
    main()
