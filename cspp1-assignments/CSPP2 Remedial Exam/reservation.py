global dictx
dictx = {}
global count
count = 0
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
    count += 1
    if count not in dictx.values():
        # print(dictx.values())
        dictx[name] = count
    else:
        reserve(name)
    # print(dictx)

def reserveN(name, roomno):
    dictx[name] = int(roomno)
    # print(dictx)
def display():
    for each in dictx.keys():
        print(str(each) + " " + str(dictx[each]))
    # for key, value in sorted(dictx.items(), key = lambda kv: (-kv,kv[0])):
    #     print("%s: %s" % (key, value))
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