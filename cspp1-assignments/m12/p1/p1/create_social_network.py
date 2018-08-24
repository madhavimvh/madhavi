'''
    Assignment-1 Create Social Network
'''
import re
def create_social_network(data):
    '''
        The data argument passed to the function is a string
        It represents simple social network data
        In this social network data there are people following other people

        Here is an example social network data string:
        John follows Bryant,Debra,Walter
        Bryant follows Olive,Ollie,Freda,Mercedes
        Mercedes follows Walter,Robin,Bryant
        Olive follows John,Ollie

        The string has multiple lines and each line represents one person
        The first word of each line is the name of the person
        The second word is follows that separates the person from the followers
        After the second word is a list of people separated by ,

        create_social_network function should split the string on lines
        then extract the person and the followers by splitting each line
        finally add the person and the followers to a dictionary and
        return the dictionary

        Caution: watch out for trailing spaces while splitting the string.
        It may cause your test cases to fail although your output may be right

        Error handling case:
        Return a empty dictionary if the string format of the data is invalid
        Empty dictionary is not None, it is a dictionary with no keys
    '''
    print("data",data)
    adict = {}
    data_new = []
    ele_new = ""
    data = data.split("\n")
    print("d",data)
    for each_word in data:
        data_new.append(each_word.split(" follows "))
    print("dn",data_new)
    for i in range(len(data_new)-1):
        if data_new[i][0] not in adict:
            adict[data_new[i][0]] = data_new[i][1].split(",")
            print("dict",adict)
        elif data_new[i][1] not in adict[data_new[i][0]]:
            data_new[i][0].append(data_new[i][1])
            print("adict",adict)
    return adict
            
            
        
        
        
        

    

def main():
    '''
        handling testcase input and printing output
    '''
    string = ''
    lines = int(input())
    for i in range(lines):
        i += 1
        string += input()
        string += '\n'
    print("string",string)

    print(create_social_network(string))

if __name__ == "__main__":
    main()
