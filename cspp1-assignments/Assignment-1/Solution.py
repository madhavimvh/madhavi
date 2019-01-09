adict = {'a': '1', 'b': '2', 'c': '3', 'd': '4'}
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
	partchoice = []
	totscore = 0
	def __init__(self):
		pass
	def addquestion(self, Question):
		self.allquestions.append(Question)
	def startquiz(self):
		for each in self.allquestions:
			print(each.getquestext() + "(" + each.getmaxmarks() + ")")
			str1 = ""
			for eachopt in each.getoptions().split(","):
				# print(each.getoptions().split(","))
				str1 += eachopt + "\t"
			str1 = str1[:-1]
			print(str1 + "\n")
	def partoptions(self, list1):
		for each in list1:
			eachx = each.split()
			if eachx[1] in adict:
				self.partchoice.append(adict[eachx[1]])
			else:
				self.partchoice.append(eachx[1])
		# print(self.partchoice)
	def matchans(self):
		for each in self.allquestions:
			print(each.getquestext())
			for part_ch in self.partchoice:
				# print(self.partchoice)
				# print(part_ch)
				# print(each.getcorrectans())
				if each.getcorrectans() == part_ch:
					print(" Correct Answer! - Marks Awarded: " + each.getmaxmarks())
					self.totscore += int(each.getmaxmarks())
					del self.partchoice[self.partchoice.index(part_ch)]
					break
				else:
					print(" Wrong Answer! - Penalty: " + each.getnegmarks())
					self.totscore += int(each.getnegmarks())
					del self.partchoice[self.partchoice.index(part_ch)]
					break
		print("Total Score: " + str(self.totscore))


def main():
	quiz = Quiz()
	k = ""
	try:
		while True:
			n = input().split()
			# print(n)
			if n[0] == "LOAD_QUESTIONS":
				print("|----------------|")
				print("| Load Questions |")
				print("|----------------|")
				try:
					if n[1] == "0":
						k = n[1]
						raise Exception("Quiz does not have questions")
					else:
						for i in range(int(n[1])):
							string = input().split(":")
							# print(string)
							# try:
							if string[0] == "" or string[1] == "" or string[2] == "" or string[3] == "" or string[4] == "":
								raise Exception("Error! Malformed question")
							else:
								print(n[1] + " are added to the quiz")
								Ques = Question(string[0], string[1], string[2], string[3], string[4])
								quiz.addquestion(Ques)
							# except Exception as e:
								# print(e)

				except Exception as e:
					print(e)
			if n[0] == "START_QUIZ":
				print("|------------|")
				print("| Start Quiz |")
				print("|------------|")
				if k != "0":
					quiz.startquiz()
					list1 = []
					for i in range(int(n[1])):
						list1.append(input())
					quiz.partoptions(list1)
			if n[0] == "SCORE_REPORT":
				print("|--------------|")
				print("| Score Report |")
				print("|--------------|")
				if k != "0":
					quiz.matchans()
	except EOFError:
		pass
main()