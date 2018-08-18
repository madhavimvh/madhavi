import re
def word_list(text):
    '''
        Change case to lower and split the words using a SPACE
        Clean up the text by remvoing all the non alphabet characters
        return a list of words
    '''
    words_listtp = []
    i = 0
    while i < len(text):
        tp_text = text[i]
        print("tp",tp_text)
        tp_text = tp_text.lower()
        words_list1 = tp_text.split(" ")
        words_listtp.append(words_list1)
        print(words_listtp)
        i += 1
    count = 0
    words_list11 = []
    i = 0
    while count < len(words_listtp):
        words_len = (len(words_listtp[count]))
        print(words_len)
        while i < words_len:
            words_list11.append(re.sub("[^a-z]", "",words_listtp[count][i]))
            count += 1
            i += 1
        #print(words_list11)
    
    return words_list11
print("wl",word_list(['Computers makes as many mistakes in one second as three men working for thirty years straight.', 'Talk is cheap. Show me the code.', "That's the thing about people who think they hate computers. What they really hate is lousy programmer.", "I'm not a great programmer; I'm just a good programmer with great habits.", 'Any fool can write code that computers can understand. Good programmers write code that humans can understand.', "At forty, I was too old to work as a programmer myself anymore; writing code is a young person's job."]))
