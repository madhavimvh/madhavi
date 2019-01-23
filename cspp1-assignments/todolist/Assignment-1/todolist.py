class Task:
	def __init__(self, title, pername, time, imp, urgent, status):
		self.title = title
		self.pername = pername
		self.time = time
		self.imp = imp
		self.urgent = urgent
		self.status = status
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