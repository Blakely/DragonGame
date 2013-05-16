import random
import time

def displayIntro():
	print ('You are on a planet full of dragons. In front of you,')
	print ('you see two caves. In one cave, the dragon is friendly')
	print ('and will share his treasure with you. The other dragon')
	print ('is greedy and hungry, and will eat you on sight.')
	print
	
def chooseCave():
	cave = ''
	while cave != '1' and cave != '2':
		print ('Which cave will you go into? (1 or 2)')
		cave = raw_input()
	return cave

def checkCave(chosenCave):
	print ('You approach the cave...')
	time.sleep(2)
	print ('It is dark and spooky...')
	time.sleep(2)
	print ('A large dragon jumps out in front of you! He opens his jaws and...')
	print
	time.sleep(2)
	
	friendlyCave = random.randint(1, 2)
	
	if chosenCave == str(friendlyCave):
		print ('Gives you his treasure!')
	else:
		print ('Gobbles you down in one bite!')


outcomes = ["ANND you have a Heart attack from the suspense.",
			"You walk a bit further, but are hit by a sudden epiphany that dictates you spend the rest of your life avoiding caves. You decide to leave.",
			"EARTHQUAKE! You die.",
			"You hit a dead end, and your evil half twin has you unexpectedly cornered. He kills you with a small blunt rock.",
			"A wild Pikachu appears. A pokemon battle ensues, and you completely forget why you came to the cave to begin with.",
			"It begins getting very dark. You start feeling your way around and notice the teeth you are hanging onto are very large and sharp, not unlike a dragons. The dragon kills you",
			"You stumble upon the dragons lair. A battle ensues, but the dragon overpowers you in the end.",
			"You see a shiny glimmer at the end of the tunnel. You run towards it and begin to realize that it's a treasure chest with a small gecko sitting atop it. That must be the dragon! You mush the gecko under your boot and claim the treasure"]

#{1:{1:(1,2),2:(1,2)},2:{1:(1,2),2:(1,2)}}
#{1:{1:(1,2),2:(3,4)},2:{1:(5,6),2:(7,8)}}
paths = [[[1,2],[3,4]],[[5,6],[7,8]]]

	



def leftOrRight(cpath):
	validInput = ("left","right")
	fork=""
	
	while (not fork in validInput):
		print("You can go left or right. Choose one: ")
		fork=raw_input()
		
		if(fork=="left"):
			return 0
		elif(fork=="right"):
			return 1

def upOrDown(cpath):
	validInput = ("up","down")
	fork=""
	
	while (not fork in validInput):
		print("You can go up or down. Choose one: ")
		fork=raw_input()
		
		if(fork=="up"):
			return 0
		elif(fork=="down"):
			return 1

path=1
currPath = paths
level=0

def game():
	global path,currPath,level
	
	if(path==0):
		path=leftOrRight(currPath)
	elif(path==1):
		path=upOrDown(currPath)
	
	level = level + 1
	print level
	if (level==3):
		print outcomes[path]
	else:
		currPath=currPath[path]
		game()

def main():
	global path,currPath,level
	
	playAgain = 'yes'
	while playAgain == 'yes' or playAgain == 'y':
		displayIntro()
		path=1
		currPath = paths
		level=0
		game()
		#caveNumber = chooseCave()
		#checkCave(caveNumber)
	
		print ('Do you want to play again? (yes or no)')
		playAgain = raw_input()


if __name__ == "__main__": main()
