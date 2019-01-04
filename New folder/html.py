def hyperlinks(html):
    data = html.split("</a>")
    for each in data:
        print("sdhf")
        print(each)
    tag = "<a href=\""
    endtag = "\""
    for item in data:
        if "<a href=\"" in item:
            # print(item)
            # print("item")
            try:
                ind = item.index(tag)
                # print(ind)
                item=item[ind+len(tag):]
                # print(len(tag))
                # print(item)
                end=item.index(endtag)
                # print(end)
            except: pass
            else:
                # print("hyperlinks")
                print(item[:end])

def heading(html):
    list1 = ["<h1", "<h2", "<h3", "<h4", "<h5", "<h6"]
    data = html.replace("\n", "").replace(" ","").split("</h")
    for each in data:
        # print("-----------")
        for header in list1:
            if header in each:
                # print(each)
                tag = header
                midtag = ">"
                ind = each.find(tag)
                postheader = each[ind + 1:]
                # print("postheader: " + postheader)
                mid = postheader.find(midtag)
                if "<" in postheader:
                    check(postheader[mid + 3:])
                else:
                # print("----------")
                # print(mid)
                    print(postheader[mid + 1:])
def check(postheader):
    # tag = "<"
    # print(postheader)
    midtag = ">"
    endtag = "</"
    ind = postheader.find(midtag)
    end = postheader.find(endtag)
    print(postheader[ind + 1: end])       
    # data = ['<','h','>','m','a','d','h','u','<','/','h','>']
    # str1 = ""
    # for i in range(len(data) - 2):
    #     # print(i)
    #     # print(data[i] + data[i + 1])
    #     if data[i] + data[i + 1] == "<h":
    #         if data[i + 2] == '1' or data[i + 2] == '2' or data[i + 2] == '3' or data[i + 2] == '4' or data[i + 2] == '5' or data[i + 2] == '6':
    #             a = i + 3`
    #             while True:
    #                 if data[a] == "<":
    #                     print("--------------")
    #                     # print(str1)
    #                     break
    #                 else:
    #                     str1 += data[a]
    #                     a += 1
def gettext(html):
	data = list(html.replace("\n","").replace(" ",""))
	# print(html)
	str1 = ">"
	str2 = "<"
	str3 = ""
	for i in range(len(data) - 1):
		if data[i] == ">" and data[i + 1] != "<":
			if(''.join(data[i - 6:i])) != "script":
				a = i + 1
				while True:
					str3 += data[a]
					a = a + 1
					if data[a] == "<":
						str3 += "\n"
						# print("--------")
						break
	str4 = []
	str4 = str3.replace("\t","").split("\n")
	for each in str4:
		if "{" not in each:
			if len(each) != 0:
				print(each)


	# print(str3)
	# for each in str3:
		# if each != "":
			# print(each)





def main():
    html = open("page.html", errors='ignore').read()
    # print(html)
    # hyperlinks(html)
    # heading(html)
    gettext(html)
    


if __name__ == "__main__":
    main()