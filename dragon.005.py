import random,time

'''
Author	: 	Ryan Blakely
Date	: 	May 22, 2013
File	: 	dragon.py
Purpose	:	A very basic (but easily scalable) 3-level decision making game.
'''

paths = [] #possible paths in the current game
outcomes = [] #possible end-of-paths in the current game
currPath="" #the current path string
pathMap = None #the map (dictionary/psuedo-binary tree) for the path for the current game
level=0 #current level

validInput = ("0","1") #valid user inputs for the choiecs
maxChoices=2 #maximum number of choices available
maxLevel=3 #the max level
timeDelim=">" #delimiter to split text on for the timed print

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

#splits a given string based on a delimiter into a list and prints each string in the list at a set interval
#params: string - the string to split & print
def timedPrint(msg):
	global timeDelim
	
	delay=1.5 #delay in seconds to iterate through the msg
	msgList = str(msg).split(timeDelim) #split the msg into a list
	
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
def randPath():
	global paths
	randMax = len(paths)
	return random.randint(0,randMax-1)

#gets a random outcome index from the remaining available outcomes
#returns: random outcome index
def randOutcome():
	global outcomes
	randMax = len(outcomes)
	return random.randint(0,randMax-1)

#randomizes the caves paths and outcomes into a pseudo- binary tree (the "path map")
#returns: dictionary representing the randomized path map
def randomizeCaves():
	global paths, outcomes, maxChoices
	
	randomPath={} #the dictionary to hold the random path map
	
	'''
		each decision level will be put into the dictionary with a key that represents its path
		Ex 	randomPath[0|1] is the first decison level
			randomPath[00|01|10|11] is the second decision level
			etc..
	'''		
	#randomize first decision level
	for x in range(0,maxChoices):
		randomPath[str(x)]=paths.pop(randPath())
		
		#randomize second decision level
		for i in range(0,maxChoices):
			randomPath[str(x)+str(i)]=paths.pop(randPath())
			
			#randomize third decision level (outcomes)
			for b in range(0,maxChoices):
				randomPath[str(x)+str(i)+str(b)]=outcomes.pop(randOutcome())
	
	return randomPath
		
#gets a choice (one of the valid inputs) from the user
#returns: the choice the user inputted
def getChoice():
	global validInput
	
	choice=""
	
	#keep asking for input until user gives valid input
	while (not choice in validInput):
		if(not choice): #if the user didn't make a choice (yet?), get their input
			choice=raw_input()
		
		else: #if the user has already made a choice, tell them it was invalid and get it again
			print("Invalid input. Choose 0 or 1:")
			choice=raw_input()
		
	return choice 

#the main game loop. allows the user to choose a path and recurses until the final level is reached
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
	global pathMap,currPath,level,paths,outcomes,resetPath,resetOutcome

	playAgain = 'yes'
	
	#as long as the user selects yes (or 'y'), replay the game
	while playAgain == 'yes' or playAgain == 'y':
		#reset the games possible path/outcome variables (copy the lists)
		paths=resetPath[:]
		outcomes=resetOutcome[:]
		
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
