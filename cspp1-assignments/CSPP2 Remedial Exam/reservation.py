global dictx
dictx = {}
global count
count = 0
global str1
str1 = ""
# def getroomno(count):
#   count += 1
#   if count not in dictx.values():
#       print(count)
#       return count
#   else:
#       getroomno(count)

def reserve(name):
    global count
    global dictx
    global str1
    count += 1
    if count >= 6:
        str1 += "All Rooms are reserved" + '\n'
        return
    if count not in dictx.values():
        # print(dictx.values())
        dictx[name] = count
        str1 += name + " " + str(count) + "\n"
    else:
        reserve(name)
    # print(name + " " + str(count))

def reserveN(name, roomno):
    global str1
    for each in dictx.values():
        if int(roomno) == int(each):
            str1 += "Room is already reserved" + "\n"
            # print(str(roomno) + " " + str(each))
            return
        if int(roomno) >= 6:
            str1 += "All Rooms are reserved" + "\n"
            return
            # print(dictx.values())
    dictx[name] = int(roomno)
    str1 += name + " " + str(roomno) + "\n"
    
    # print(name + " " + str(roomno))
def display():
    print(str1.strip())
    # listkeys = list(dictx.keys())
    # for each in listkeys:
    #     if dictx[each] >= 6:
    #         dictx.pop(each, None)
    #         print("All Rooms are reserved")
    #         # break
    #     else:
    #         print(str(each) + " " + str(dictx[each]))
    for key, value in sorted(dictx.items(), key = lambda kv:(kv[1], kv[0])):
        print("%s %s" %(key, value))
def main():
    # getroomno(count)
    num = int(input())
    string1 = []
    for i in range(num):
        string1 = input().split()
        # print(string1)
        if string1[0].strip() == "reserve":
            reserve(string1[1])
        elif string1[0].strip() == "reserveN":
            reserveN(string1[1], string1[2])
        elif string1[0].strip() == "print":
            display()
main()