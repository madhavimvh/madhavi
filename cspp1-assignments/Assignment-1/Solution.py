class Question:
	def __init__(self,question, options, correctans, maxmarks, negmarks):
		print(question)
		self.question = question
		self.options = options
		self.correctans = correctans
		self.maxmarks = maxmarks
		self.negmarks = negmarks
class Quiz:
	allquestions = []
	def __init__(self):
		pass
	def addquestion(self, Question):
		self.allquestions.append(Question)

def main():
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
	if n[0] == "SCORE_REPORT":
		print("|--------------|")
		print("| Score Report |")
		print("|--------------|")
main()