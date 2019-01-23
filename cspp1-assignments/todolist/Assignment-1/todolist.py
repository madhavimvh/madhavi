class Task:
	def __init__(self, title, pername, time, imp, urgent, status):
		self.pername = pername
		self.imp = imp
		self.urgent = urgent
		self.title = title
		self.status = status
		self.time = time
		try:
			if title == "":
				raise Exception("Title not provided")
			# else:
				# self.title = title
			elif int(time) < 0:
				raise Exception("Invalid timeToComplete " + time)
			# else:
				# self.time = time
			elif status != "todo" or status != "done":
				raise Exception("Invalid status " + status)	
		except Exception as e:
			print(e)
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


def main():
	string = input().split(",")
	task = Task(string[1], string[2], string[3], string[4], string[5], string[6])
	if string[0] == "task":
		task.display()
main()