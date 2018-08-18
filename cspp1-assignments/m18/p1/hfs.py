def word_list(text):
    '''
        Change case to lower and split the words using a SPACE
        Clean up the text by remvoing all the non alphabet characters
        return a list of words
    '''
    text = text.lower()
    words_list1 = text.split(" ")
    words_list11 = re.sub("[^a-z],"",words_list1")
    return words_list11

print(word_list(['Computers makes as many mistakes in one second as three men working for thirty years straight.', 'Talk is cheap. Show me the code.', "That's the thing about people who think they hate computers. What they really hate is lousy programmer.", "I'm not a great programmer; I'm just a good programmer with great habits.", 'Any fool can write code that computers can understand. Good programmers write code that humans can understand.', "At forty, I was too old to work as a programmer myself anymore; writing code is a young person's job."]))
