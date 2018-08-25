'''
Write a function to print a dictionary with the keys in sorted order along with the
frequency of each word. Format of the printing should be one key per line and separate
the key and frequency with a SPACE - SPACE.
'''
from collections import OrderedDict 
def print_dictionary(dictionary):
    alpha = OrderedDict(sorted(ages.items(), key=lambda x: x[0]))
    for k, v in dictionary.items():
        print(k, "-", v)
    #keys = sorted(index.keys())
    #print(keys)
    #for key in keys:
        #print(key, " - ", index[key])"""

def main():
    dictionary = eval(input())
    print_dictionary(dictionary)

if __name__ == '__main__':
    main()
