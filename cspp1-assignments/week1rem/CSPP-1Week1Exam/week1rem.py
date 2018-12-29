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
	pass
def listtext(html):
	pass
def main():
	html = open("webpage5.html", errors='ignore').read()
	# print(html)
	# string = input()
	# if string == "image":
	image(html)
	# elif string == "background":
	background(html)
	# elif string == "list":
	listtext(html)
main()