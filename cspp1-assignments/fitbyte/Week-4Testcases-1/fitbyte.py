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
	def Foodlogdis(self):
		print("Food:" + "\n" + self.date + ":" + "\n" + "- " + self.time + ": " + self.fooditem)
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
	def waterlogdis(self):
		print("Water:" + "\n" + self.date + ":" + "\n" + "- " + self.time + ": " + self.waterquan)

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
	def PAdis(self):
		print("PhysicalActivity:" + "\n" + self.date + ":" + "\n" + "- " + self.time + ": " + self.activity)
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
	def wtdis(self):
		print("Weight:" + "\n" + self.date + ":" + "\n" + "- " + self.time + ": " + self.weight)
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
	def sleeplogdis(self):
		print("Sleep:" + "\n" + self.date + ":" + "\n" + "- " + self.time + ": " + self.sleephrs)

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
	def disFL(self):
		for each in self.foodlogs:
			each.Foodlogdis()
	def disWaterlog(self):
		for each in self.waterlogs:
			each.waterlogdis()
	def disPAct(self):
		for each in self.physicalacties:
			each.PAdis()
	def disWeight(self):
		for each in self.weightlogs:
			each.wtdis()
	def disSleep(self):
		for each in self.sleeplogs:
			each.sleeplogdis()

	def summary(self):
		self.disFL()
		self.disWaterlog()
		self.disPAct()
		self.disWeight()
		self.disSleep()


def main():
	fitbyte = FitByte()
	n = int(input())
	for i in range(n):
		string = input().split(" ")
		if string[0] == "Food":
			str1 = string[1].split(",")
			foodlg = FoodLog(str1[0], str1[1], str1[2])
			fitbyte.addfoodlog(foodlg)
		if string[0] == "Water":
			str1 = string[1].split(",")
			waterlg = WaterLog(str1[0], str1[1], str1[2])
			fitbyte.addwaterlog(waterlg)
		if string[0] == "PhysicalActivity":
			str1 = string[1].split(",")
			PAlog = PhysicalActivity(str1[0], str1[1], str1[2])
			fitbyte.addphysicalact(PAlog)
		if string[0] == "Weight":
			str1 = string[1].split(",")
			weightlg = WeightLog(str1[0], str1[1], str1[2])
			fitbyte.addweightlog(weightlg)
		if string[0] == "Sleep":  
			str1 = string[1].split(",")
			sleeplg = SleepLog(str1[0], str1[1], str1[2])
			fitbyte.addsleeplog(sleeplg)
		if string[0] == "Foodlog":
			fitbyte.disFL()
		if string[0] == "Waterlog":
			fitbyte.disWaterlog()
		if string[0] == "PhysicalActivitylog":
			fitbyte.disPAct()
		if string[0] == "Weightlog":
			fitbyte.disWeight()
		if string[0] == "SleepLog":
			fitbyte.disSleep()
		if string[0] == "Summary":
			fitbyte.summary()

			




main()