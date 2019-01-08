class Question:
	optinvotes = {}
	def __init__(self, question, options):
		self.question = question
		self.options = options
		print(options)
		for opt in options:
			self.optinvotes[opt] = 0
	def setOptionVotes(self, optin):
		self.optinvotes[optin] += 1
	def commonSelectedOption(self):
		n = max(self.optinvotes.values())
		for each in optinvotes:
			if optinvotes[each] == n:
				return each


class Quiz:
	questions = []
	def __init__(self):
		pass
	def addQuestion(self, Question):
		self.questions.append(Question)
	def getQuestion(self, i):
		return self.questions[i]
class Participant():
	def __init__(self, name, qno, option):
		self.name = name
		self.qno = qno
		self.option = option



def main():
	quiz = Quiz()
	noofques = int(input())
	for i in range(noofques):
		ques = input()
		options = []
		for i in range(4):
			options.append(input())
		ques1 = Question(ques, options)	
		quiz.addQuestion(ques1)
	participants = int(input())
	for i in range(participants):
		name = input()
		for i in range(noofques):
			line = input().split()
			q = int(line[0])
			p = Participant(name, q - 1, line[1])
			question = quiz.getQuestion(q - 1)
			question.setOptionVotes(line[1])
	for i in range(noofques):
		print("Highest number of votes for question :" + quiz.getQuestion(i).getText() + " : " + quiz.getQuestion(i).commonSelectedOption())

main()
