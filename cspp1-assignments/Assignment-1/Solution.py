class Question:
	def __init__(self,question, options, correctans, maxmarks, negmarks):
		# print(question)
		self.question = question
		self.options = options
		self.correctans = correctans
		self.maxmarks = maxmarks
		self.negmarks = negmarks
	def getquestext(self):
		return self.question
	def getoptions(self):
		return self.options
	def getcorrectans(self):
		return self.correctans
	def getmaxmarks(self):
		return self.maxmarks
	def getnegmarks(self):
		return self.negmarks


class Quiz:
	allquestions = []
	def __init__(self):
		pass
	def addquestion(self, Question):
		self.allquestions.append(Question)
	def startquiz(self):
		str1 = ""
		for each in self.allquestions:
			print(each.getquestext() + "(" + each.getmaxmarks() + ")")
			for eachopt in each.getoptions():
				str1 = each + "\t"
			print(str1)
	# def partoptions():


def main():
	try:
		while True:
			quiz = Quiz()
			n = input().split()
			print(n)
			if n[0] == "LOAD_QUESTIONS":
				print("|----------------|")
				print("| Load Questions |")
				print("|----------------|")
				print(n[1] + " are added to the quiz")
				for i in range(int(n[1])):
					string = input().split(":")
					# print(string)
					Ques = Question(string[0], string[1], string[2], string[3], string[4])
					quiz.addquestion(Ques)
			if n[0] == "START_QUIZ":
				print("|------------|")
				print("| Start Quiz |")
				print("|------------|")
				quiz.startquiz()
				list1 = []
				for i in range(int(n[1])):
					list1.append(input())
			if n[0] == "SCORE_REPORT":
				print("|--------------|")
				print("| Score Report |")
				print("|--------------|")
	except EOFError:
		pass
main()