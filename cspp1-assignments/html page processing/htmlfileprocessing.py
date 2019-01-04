def hyperlinks(html):
	data = html.split(" ")
	print(data)







def main():
	html = open("page.html", errors='ignore').read()
	hyperlinks(html)
	
if __name__== "__main__":
	main()