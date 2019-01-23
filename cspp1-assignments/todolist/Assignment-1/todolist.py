class Task:
	def __init__(self, title, pername, time, imp, urgent, status):
		self.title = title
		self.pername = pername
		self.time = time
		self.imp = imp
		self.urgent = urgent
		self.status = status
	def display():
		if imp == "y":
			imp = "Important"
		if urgent == "y":
			urgent = "Urgent"
		print(title + "," + pername  + "," + time + "," + imp  + "," + urgent + "," + status)


def main():
	string = input().split(",")
	task = Task(string[1], string[2], string[3], string[4], string[5], string[6])
	if string[0] == "task":
		task.display()


main()