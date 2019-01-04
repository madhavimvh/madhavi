import csv
def history(csv1):
	for each in csv1:
		if "Year" in each:
			yearindex = csv1.index(each) + 1
	for i in range(12,len(csv1) - 1):
		str1 = csv1[i].split(";")
		day = str1[2]
		hour = str1[3]
		windspeed = str1[len(str1) - 3]
		# print(windspeed)
		if float(windspeed) < 35.0:
			print(day + " " + hour + " " + windspeed)
			


			

def main():
	csv1 = open('history.csv','r').read().split("\n")
	# print(csv1)
	
	history(csv1)
if __name__ == "__main__":
    main()