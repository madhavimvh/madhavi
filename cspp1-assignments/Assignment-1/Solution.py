class Question:
	def __init__(self,question, options, correctans, maxmarks, negmarks):
		# print(question)
		self.question = question
		self.options = options
		self.correctans = correctans
		self.maxmarks = maxmarks
		self.negmarks = negmarks
class Quiz:
	allquestions = []
	def __init__():
		pass
	def addquestion(Question):
		allquestions.append(Question)

def main():
	n = input().split()
	for i in range(int(n[1])):
		string = input().split(":")
		print(string)
		Ques = Question(string[0], string[1], string[2], string[3], string[4])
		quiz.addquestion(Ques)
main()