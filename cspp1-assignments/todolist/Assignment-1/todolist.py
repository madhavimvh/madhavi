class Task:
	def __init__(self, title, pername, time, imp, urgent, status):
		self.pername = pername
		self.imp = imp
		self.urgent = urgent
		self.title = title
		self.status = status
		self.time = time
		# try:
		if self.title == "":
			raise Exception("Title not provided")
			return
		# else:
			# self.title = title
		elif int(self.time) < 0:
			raise Exception("Invalid timeToComplete " + self.time)
			return
		# else:
			# self.time = time
		elif self.status != "todo" and self.status != "done":
			raise Exception("Invalid status " + self.status)	
		# except Exception as e:
			# print(e)
	def gettask(self):
		return self.title
	def getpername(self):
		return self.pername
	def gettime(self):
		return self.time
	def getstatus(self):
		return self.status
	def getimp(self):
		return self.imp
	def getimpN(self):
		if self.imp == "y":
			self.imp = "Important"
		elif self.imp == "n":
			self.imp = "Not Important"
		return self.imp
	def geturg(self):
		return self.urgent
	def geturgN(self):
		if self.urgent == "y":
			self.urgent = "Urgent"
		elif self.urgent == "n":
			self.urgent = "Not Urgent"
		return self.urgent
	def display(self):
		if self.imp == "y":
			self.imp = "Important"
		elif self.imp == "n":
			self.imp = "Not Important"
		if self.urgent == "y":
			self.urgent = "Urgent"
		elif self.urgent == "n":
			self.urgent = "Not Urgent"
		print(self.title + ", " + self.pername  + ", " + self.time + ", " + self.imp  + ", " + self.urgent + ", " + self.status)

class Todoist:
	alltasks = []
	def __init__(self):
		pass
	def addtask(self, Task):
		self.alltasks.append(Task)
	def getNextTask(self, personnme):
		for each in self.alltasks:
			if each.getpername() == personnme:
				if each.getimp() == "y":
					if each.geturg() == "n":
						if each.getstatus() == "todo":
							each.display()
							return
		for each in self.alltasks:
			if each.getpername() == personnme:
				if each.getimp() == "y":
					if each.geturg() == "n":
						if each.getstatus() == "todo":
							each.display()
							return
		else:
			print("null")
	def getNextTaskN(self, persnname, count):
		list1 = []
		for each in self.alltasks:
			if each.getpername() == persnname:
				if each.getstatus() == "todo":
					list1.append(each.gettask())
					list1.append(each.getpername())
					list1.append(each.gettime())
					list1.append(each.getimpN())
					list1.append(each.geturgN())
					list1.append(each.getstatus())
					# print(count)
			if len(list1) == int(count)*6:
				print("[%s]" % (', '.join(list1)))
				# print(list1)
				return
		list1.append("null")
		print("[%s]" % (', '.join(list1)))


	def displayall(self):
		for each in self.alltasks:
			each.display()
	def totalTime4Completion(self):
		total = 0
		for each in self.alltasks:
			if each.getstatus() == "todo":
				total += int(each.gettime())
		print(total)


def main():
	try:
		while True:
			todoist = Todoist()
			string = input().split(",")
			try:
				if string[0] == "task":
					task = Task(string[1], string[2], string[3], string[4], string[5], string[6])
					task.display()
				if string[0] == "add-task":
					task1 = Task(string[1], string[2], string[3], string[4], string[5], string[6])
					todoist.addtask(task1)
				elif string[0] == "print-todoist":
					todoist.displayall()
				elif string[0] == "get-next":
					todoist.getNextTask(string[1])
				elif string[0] == "get-next-n":
					todoist.getNextTaskN(string[1], string[2])
				elif string[0] == "total-time":
					todoist.totalTime4Completion()
			except Exception as e:
					print(e)
	except EOFError:
		pass

main()