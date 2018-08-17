'''
    Document Distance - A detailed description is given in the PDF
'''
import re
import math
def similarity(dict1, dict2):
    '''
        Compute the document distance as given in the PDF
    '''
    dict1 = dict1.lower()
    dict2 = dict2.lower()
    dict1 = dict1.split(" ")
    dict2 = dict2.split(" ")
    count = 0
    words_list1 = [] 
    while count < len(dict1):
        #print(dict1[count])
        words_list1.append(re.sub("[^a-z]", "",dict1[count]))
        count += 1
    words_list11 = remove_stopwords(words_list1)
    #print(words_list11)
    count = 0
    words_list2 = []
    while count < len(dict2):
        words_list2.append(re.sub("[^a-z]", "",dict2[count]))
        count += 1

    words_list22 = remove_stopwords(words_list2)

    words_list111 = frequency_list(words_list11, words_list22)
    return compute_similarities(words_list111)

def remove_stopwords(words_list1):
    stop_words = load_stopwords("stopwords.txt")
    temp_wordlist1 = words_list1[:]
    for each_word in temp_wordlist1:
        if each_word in stop_words:
            words_list1.remove(each_word)
    return words_list1
    
def frequency_list(words_list1, words_list2):
    freq_list = {}
    for each_word in words_list1:
        if len(each_word) > 0:
            if each_word not in freq_list:
                freq_list[each_word] = [1, 0]
            else:
                freq_list[each_word][0] += 1
    
    for each_word in words_list2:
        if len(each_word) > 0:
            if each_word not in freq_list:
                freq_list[each_word] = [0, 1]
            else:
                freq_list[each_word][1] += 1
    #print(freq_list)
    return freq_list

def compute_similarities(freq_list):
    numerator = 0
    den_1 = 0
    den_2 = 0
    for each_word in freq_list:
        numerator += freq_list[each_word][0]*freq_list[each_word][1]
        den_1 += freq_list[each_word][0]**2
        den_2 += freq_list[each_word][1]**2
    denominator = math.sqrt(den_1)*math.sqrt(den_2)
    #print(numerator)
    #print(den_1)
    #print(den_2)
    #print(denominator)
    return numerator/denominator  

def load_stopwords(filename):
    '''
        loads stop words from a file and returns a dictionary
    '''
    stopwords = {}
    with open(filename, 'r') as filename:
        for line in filename:
            stopwords[line.strip()] = 0
    return stopwords

def main():
    '''
        take two inputs and call the similarity function
    '''
    input1 = input()
    input2 = input()

    print(similarity(input1, input2))
    #print(remove_stopwords(input1))

if __name__ == '__main__':
    main()

