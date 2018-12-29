def image(html):
	data = html.split("</a>")
	count = 0
	list1 = []
	# for each in data:
		# print("-------------------------------")
		# print(each)
	tag = "<img"
	midtag = "src=\""
	endtag = "\""
	for each in data:
		if tag in each:
			# print(each)
			# print("--------------")
			ind = each.index(tag)
			posttag = each[ind + len(tag):]
			mid = posttag.index(midtag)
			postsrc = posttag[mid + len(midtag):]
			end = postsrc.index(endtag)
			# print("/////////")
			print(postsrc[:end])
			list1.append(postsrc[:end])
			if tag in postsrc:
				# print(postsrc)
				# print("----------------------")
				# count += 1
				check(postsrc, list1)
			# else:
	print(len(list1))
def check(postsrc, list1):
	tag = "<img"
	midtag = "src=\""
	endtag = "\""
	ind = postsrc.index(tag)
	posttag = postsrc[ind + len(tag):]
	mid = posttag.index(midtag)
	postsrc1 = posttag[mid + len(midtag):]
	end = postsrc1.index(endtag)
	print(postsrc1[:end])
	list1.append(postsrc1[:end])
	# count += 1
	# print(count)
	if tag in postsrc1:
		# count += 1
		check(postsrc1, list1)
	

def background(html):
	data = html.replace("\n","").split("{")
	global set1
	set1 = set()
	for each in data:
		checkbackground(each)
	set2 = []
	for each in set1:
		if len(each) <= 20:
			set2.append(each.strip())
	# print(set2)
	sorted(set2)
	for eachx in sorted(set2):
		print(eachx)
	print(len(set2))



def checkbackground(each):
	tag = "background-color:"
	endtag = ";"
	endtag2 = "}"
	if tag in each:
		if endtag in each:
			# print(each)
			# print("------------------------")
			ind = each.find(tag)
			posttag = each[ind + len(tag):]
			# print(posttag)
			end = posttag.find(endtag)
			set1.add(posttag[:end])
			if tag in posttag:
				if endtag in posttag:
					checkbackground(posttag)
		elif endtag2 in each:
			ind = each.find(tag)
			posttag = each[ind + len(tag):]
			# print(posttag)
			end = posttag.find(endtag2)
			set1.add(posttag[:end])
			if tag in posttag:
				if endtag2 in posttag:
					checkbackground(posttag)



def listtext(html):
	pass
	
def main():
	html = open("webpage5.html", errors='ignore').read()
	# print(html)
	string = input()
	if string == "image":
		image(html)
	elif string == "background":
		background(html)
	elif string == "list":
		listtext(html)
main()