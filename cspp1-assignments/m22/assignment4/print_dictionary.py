'''
Write a function to print a dictionary with the keys in sorted order along with the
frequency of each word. Format of the printing should be one key per line and separate
the key and frequency with a SPACE - SPACE.
'''
from collections import OrderedDict 
def print_dictionary(dictionary):
    """dictionary_1 = dictionary.keys()
    print(dictionary)
    for k, v in dictionary.items():
        print(k, "-", v)"""
    keys = sorted(dictionary.keys())
    #print(keys)
    for key in keys:
        print(key, " - ", dictionary[key])

def main():
    dictionary = eval(input())
    print_dictionary(dictionary)

if __name__ == '__main__':
    main()
