class FoodLog:
	def __init__(self, fooditem, date, time):
		self.fooditem = fooditem
		self.date = date
		self.time = time
	def getfooditem(self):
		return self.fooditem
	def getdateF(self):
		return self.date
	def gettimeF(self):
		return self.time
	def sumFL(self):
		print("- " + self.time + ": " + self.fooditem)
class WaterLog:
	def __init__(self, waterquan, date, time):
		self.waterquan = waterquan
		self.date = date
		self.time = time
	def getwaterquan(self):
		return self.waterquan
	def getdateW(self):
		return self.date
	def gettimeW(self):
		return self.time
	def sumWater(self):
		print("- " + self.time + ": " + self.waterquan)

class PhysicalActivity:
	def __init__(self, activity, date, time):
		self.activity = activity
		self.date = date
		self.time = time
	def getactivity(self):
		return self.activity
	def getdatePA(self):
		return self.date
	def gettimePA(self):
		return self.time
	def sumPA(self):
		print("- " + self.time + ": " + self.activity)
class WeightLog:
	def __init__(self, weight, date, time):
		self.weight = weight
		self.date = date
		self.time = time
	def getweight(self):
		return self.weight
	def getdateweight(self):
		return self.date
	def gettimeweight(self):
		return self.time
	def sumweight(self):
		print("- " + self.time + ": " + self.weight)
class SleepLog:
	def __init__(self, sleephrs, date, time):
		self.sleephrs = sleephrs
		self.date = date
		self.time = time
	def getsleephrs(self):
		return self.sleephrs
	def getdateSP(self):
		return self.date
	def gettimeSP(self):
		return self.time
	def sumsleep(self):
		print("- " + self.time + ": " + self.sleephrs)

class FitByte:
	foodlogs = []
	waterlogs = []
	physicalacties = []
	weightlogs = []
	sleeplogs = []
	def __init__(self):
		pass
	def addfoodlog(self, FoodLog):
		self.foodlogs.append(FoodLog)
	def addwaterlog(self, WaterLog):
		self.waterlogs.append(WaterLog)
	def addphysicalact(self, PhysicalActivity):
		self.physicalacties.append(PhysicalActivity)
	def addweightlog(self, WeightLog):
		self.weightlogs.append(WeightLog)
	def addsleeplog(self, SleepLog):
		self.sleeplogs.append(SleepLog)
	def food1(self, each1):
		for each in self.foodlogs:
				if each.getdateF() == each1:
					each.sumFL()
	def water1(self, each1):
		for each in self.waterlogs:
				if each.getdateW() == each1:
					each.sumWater()
	def PA1(self, each1):
		for each in self.physicalacties:
				if each.getdatePA() == each1:
					each.sumPA()
	def weight1(self, each1):
		for each in self.weightlogs:
				if each.getdateweight() == each1:
					each.sumweight()
	def sleep1(self, each1):
		for each in self.sleeplogs:
				if each.getdateSP() == each1:
					each.sumsleep()
	def disFL(self, dateset):
		print("Food:")
		for each1 in sorted(dateset, reverse = True):
			for each in self.foodlogs:
				if each1 in each.getdateF():
					print(each1 + ":")
					break
			self.food1(each1)
	def disWaterlog(self, dateset):
		print("Water:")
		for each1 in sorted(dateset, reverse = True):
			for each in self.waterlogs:
				if each1 in each.getdateW():
					print(each1 + ":")
					break
			water1(each1)
	def disPAct(self, dateset):
		print("PhysicalActivity:")
		for each1 in sorted(dateset, reverse = True):
			for each in self.physicalacties:
				if each1 in each.getdatePA():
					print(each1 + ":")
					break
			PA1(each1)
	def disWeight(self, dateset):
		print("Weight:")
		for each1 in sorted(dateset, reverse = True):
			for each in self.weightlogs:
				if each1 in each.getdateweight():
					print(each1 + ":")
					break
			weight1(each1)
	def disSleep(self, dateset):
		print("Sleep:")
		for each1 in sorted(dateset, reverse = True):
			for each in self.sleeplogs:
				if each1 in each.getdateSP():
					print(each1 + ":")
					break
			sleep1(each1)

	def summary(self, dateset):
		print("Summary:")
		for each1 in sorted(dateset, reverse = True):
			print(each1 + ":") 
			for each in self.foodlogs:
				if each1 in each.getdateF():
					# print(each1)
					# print(each.getdateF())
					print("Food:")
					break
			self.food1(each1)
			for each in self.waterlogs:
				if each1 in each.getdateW():
					print("Water:")
					break
			water1(each1)
			for each in self.physicalacties:
				if each1 in each.getdatePA():
					print("PhysicalActivity:")
					break
			PA1(each1)
			for each in self.weightlogs:
				if each1 in each.getdateweight():
					print("Weight:")
					break
			weight1(each1)
			for each in self.sleeplogs:
				if each1 in each.getdateSP():
					print("Sleep:")
					break
			sleep1(each1)
		


def main():
	fitbyte = FitByte()
	dateset = set()
	n = int(input())
	for i in range(n):
		string = input().split(" ")
		if string[0] == "Food":
			str1 = string[1].split(",")
			dateset.add(str1[1])
			foodlg = FoodLog(str1[0], str1[1], str1[2])
			fitbyte.addfoodlog(foodlg)
		if string[0] == "Water":
			str1 = string[1].split(",")
			dateset.add(str1[1])
			waterlg = WaterLog(str1[0], str1[1], str1[2])
			fitbyte.addwaterlog(waterlg)
		if string[0] == "PhysicalActivity":
			str1 = string[1].split(",")
			dateset.add(str1[1])
			PAlog = PhysicalActivity(str1[0], str1[1], str1[2])
			fitbyte.addphysicalact(PAlog)
		if string[0] == "Weight":
			str1 = string[1].split(",")
			dateset.add(str1[1])
			weightlg = WeightLog(str1[0], str1[1], str1[2])
			fitbyte.addweightlog(weightlg)
		if string[0] == "Sleep":  
			str1 = string[1].split(",")
			dateset.add(str1[1])
			sleeplg = SleepLog(str1[0], str1[1], str1[2])
			fitbyte.addsleeplog(sleeplg)
		if string[0] == "Foodlog":
			fitbyte.disFL(dateset)
		if string[0] == "Waterlog":
			fitbyte.disWaterlog(dateset)
		if string[0] == "PhysicalActivitylog":
			fitbyte.disPAct(dateset)
		if string[0] == "Weightlog":
			fitbyte.disWeight(dateset)
		if string[0] == "Sleeplog":
			fitbyte.disSleep(dateset)
		if string[0] == "Summary":
			# print(dateset)
			fitbyte.summary(dateset)

			




main()