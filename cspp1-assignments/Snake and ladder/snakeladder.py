import random
def rolldice():
	return random.randint(1,6)

def playerturn(playersdict):
	throw = rolldice()
	while True:
		for each in playersdict:
			move(each, throw, playersdict)
			

def move(playerno, throw, playersdict):
	snakes = {98: 79, 95: 75, 17: 7, 54: 39, 87: 24}
	ladders = {1: 38, 4: 14, 51: 67, 71: 92, 80: 100}
	if throw in snakes:
		playersdict[playerno] = playersdict[playerno] - snakes[throw]
	elif throw in ladders:
		playersdict[playerno] = playersdict[playerno] - ladders[throw]
	else:
		playersdict[playerno] += throw
	if playersdict[playerno] > 99:
		print(str(playerno) + "wins the game")
		return

def setupplayers(numplayers):
	playersdict = {}
	for i in range(1, numplayers + 1):
		playersdict[i] = [0]
	playerturn(playersdict)

def main():
	numplayers = int(input("no of players"))
	if numplayers < 5 and numplayers > 2:
		setupplayers(numplayers)
	else:
		print("players should be below 5 and above 2")
	# move(numplayers)
main()