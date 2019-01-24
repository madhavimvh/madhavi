class Patron:
	def __init__(self, patname, mobno):
		# print("patron", patname, mobno)
		self.patname = patname
		self.mobno = mobno
	def getpatname(self):
		# print(self.patname)
		return self.patname
	def getmobno(self):
		return self.mobno
	def displaypat(self):
		print(self.mobno + " " + self.patname)

class Show:
	def __init__(self, movname, showdate, time, seatnos):
		self.movname = movname
		self.showdate = showdate
		self.time = time
		self.seatnos = seatnos
	def getmovname(self):
		return self.movname
	def getshowdate(self):
		return self.showdate
	def gettime(self):
		return self.time
	def getseatnos(self):
		return self.seatnos
	def display(self):
		print(self.movname + "," + self.showdate + " " + self.time)

class Bookyourshow:
	allshows = []
	allpatrons = []
	def __init__(self):
		pass
	def addApatron(self, Patron):
		self.allpatrons.append(Patron)
		# for each in self.allpatrons:
			# each.displaypat()
			# print(each.getpatname())
			# print(each.getmobno())
	def addAshow(self, Show):
		self.allshows.append(Show)
		# for each in self.allshows:
			# each.display()

	def getAshow(self, movname, date, time):
		for each in self.allshows:
			if each.getmovname() == movname:
				if each.getshowdate() == date:
					if each.gettime() == time:
						each.display()
	def checkseats(self, seatslist, cusseats):
		# print(seatslist)
		# print(cusseats)
		for each in cusseats:
			if each not in seatslist:
				return False
			else:
				seatslist[seatslist.index(each)] = "N/A"
		else:
			# seatslist[seatslist.index(each)] = "N/A"
			# print(seatslist)
			return True

	def bookashow(self, movname, date, time, Patron, cusseats):
		for each in self.allshows:
			if each.getmovname() == movname:
				if each.getshowdate() == date:
					if each.gettime() == time:
						if self.checkseats(each.getseatnos(), cusseats):
							return True
						else:
							return False
	def printTickets(self, movname, date, time, mobno):
		for each in self.allpatrons:
			if each.getmobno() == mobno:
				print(mobno + " " + movname + " " + date + " " + time)





def main():
	bookyourshow = Bookyourshow()
	n = int(input())
	for i in range(n):
		string = input().replace("[","").replace("]","").split(",")
		str1 = string[0].split(" ")
		str2 = string[1].rpartition(" ")
		# print(string)
		# print(str1)
		# print(str2)
		if str1[0] == "add":
			seats = []
			for i in range(2,len(string)):
				seats.append(string[i])
			show = Show(str1[1], str2[0],str2[2], seats)
			bookyourshow.addAshow(show)
		if str1[0] == "book":
			cusseats = []
			for i in range(4, len(string)):
				cusseats.append(string[i])
			patron = Patron(string[2], string[3])
			# print(patron.getpatname())
			bookyourshow.addApatron(patron)
			bookyourshow.bookashow(str1[1], str2[0], str2[2], patron, cusseats)
		if str1[0] == "print":
			bookyourshow.printTickets(str1[1], str2[0], str2[2], string[2])






main()