import random,time

'''
Author	: 	Ryan Blakely
Date	: 	May 22, 2013
File	: 	dragon.py
Purpose	:	A very basic (but easily scalable) 3-level decision making game.
'''

paths = [] #possible paths in the game
outcomes = [] #possible end-of-paths in the game
currPath="" #the current path string
pathMap = None #the map for the path
level=0 #current level

maxLevel=3 #the max level

#splits a given string based on a delimiter into a list and prints each string in the list at a set interval
#params: string - the string to split & print
def timedPrint(msg):
	delim=">" #delimited to split the msg on
	delay=1 #delay in seconds to iterate through the msg
	msgList = str(msg).split(delim) #split the msg into a list
	
	#for each message in the list, print it and pause for the length of the delay
	for timeMsg in msgList:
		print(str(timeMsg).lstrip())
		time.sleep(delay)

#prints the intro message along with the first choice
def displayIntro():
	timedPrint("You are a treasure hunter in a dragon infested area of Australia.>...")
	timedPrint("Damn Australia.")
	timedPrint("Anyways, you look ahead and there are two caves potentially filled with treasure to choose from.")
	timedPrint("Choose a cave (0 or 1):")

#gets a random path index from the remaining available paths
#returns: random path index
def randomPath():
	global paths
	randMax = len(paths)
	return random.randint(0,randMax-1)

#gets a random outcome index from the remaining available outcomes
#returns: random outcome index
def randomOutcome():
	global outcomes
	randMax = len(outcomes)
	return random.randint(0,randMax-1)

#randomizes the caves paths and outcomes into a pseudo- binary tree (the "path map")
#returns: dictionary representing the randomized path map
def randomizeCaves():
	global paths, outcomes
	
	randomPath={} #the dictionary to hold the random path map
	
	'''
		each decision level will be put into the dictionary with a key that represents its path
		Ex 	randomPath[0|1] is the first decison level
			randomPath[00|01|10|11] is the second decision level
			etc..
	'''		
	
	#randomize first decision level
	for x in range(0,2):
		randomPath[str(x)]=paths.pop(randomPath())
		
		#randomize second decision level
		for i in range(0,2):
			randomPath[str(x)+str(i)]=paths.pop(randomPath())
			
			#randomize third decision level (outcomes)
			for b in range(0,2):
				randomPath[str(x)+str(i)+str(b)]=outcomes.pop(randomOutcome())
	
	return randomPath
		
#gets a choice (one of the valid inputs) from the user
#returns: the choice the user inputted
def getChoice():
	validInputs = ("0","1") #valid inputs 
	choice=""
	
	#keep asking for input until user gives valid input
	while (not choice in validInput):
		choice=raw_input()
		
	return choice 

def game():
	global pathMap,currPath,level
	
	#get the next path to take from the user
	currPath=currPath+str(getChoice())
	
	#print the choicess at this level
	timedPrint(str(pathMap[currPath]))
	
	level = level + 1 #next level!
	
	#if were not at the third level, recurse! keep going!
	if (level!=maxLevel):
		game()

#the main method - starts the program and contains the replay functionality for the game
def main():
	global pathMap,currPath,level,paths,outcomes
	
	#all the possible paths to choose from in the game
	resetPath = ["There is a fork in the path.> Left or right (0 or 1)?",
				"A large tree appears before you.> Do you go around it, or over it (0 or 1)?",
				"The path comes to an end at an elevator.> Do you go up or down (0 or 1)?",
				"A small infant comes between you and your goal.> Do you punch it, or kick it (0 or 1)?",
				"You are confronted with a choice - 0 or 1?",
				"You have an itch on your foot.> Intense. > Do you scratch it, or continue on (0 or 1)?"]
	
	#all the possible outcomes to end up with in the game
	resetOutcome = [">ANND you have a Heart attack from the suspense.",
					"You walk a bit further...> But you are hit by a sudden epiphany that dictates you spend the rest of your life avoiding caves.> You decide to leave. > Game Over.",
					"EARTHQUAKE!!> You die.> Game Over.",
					"You hit a dead end, and your evil half twin has you unexpectedly cornered.> He kills you with a small blunt rock.> Game Over.",
					"A wild Pikachu appears.> A pokemon battle ensues!> ... > Why did you come here again? > You leave.> Game Over.",
					"Apparently you were being chased by Zombies this whole time.> They catch up to you and eat you.> Game Over.",
					"You stumble upon a dragons lair.> DRAGON BATTLE!> ...the dragon overpowers you in the end.> Game Over",
					"You see a shiny glimmer at the end of the tunnel.> You run towards it and begin to realize that it's a treasure chest with a small, fire-breathing newt sitting atop it.> You mush the newt under your boot and claim the treasure.> Congratulations, you win!"]
	
	playAgain = 'yes'
	
	#as long as the user selects yes (or 'y'), replay the game
	while playAgain == 'yes' or playAgain == 'y':
		#reset the games possible path/outcome variables (copy the lists)
		paths=list(resetPath) 
		outcomes=list(resetOutcome)
		
		#create the path map (random paths to random outcomes)
		pathMap=randomizeCaves()
		
		#reset game variables
		currPath=""
		level=0
		
		#display the intro and play the game!
		displayIntro()
		game()
	
		print ("Do you want to play again? (yes or no)")
		playAgain = raw_input() 


if __name__ == "__main__": main()
