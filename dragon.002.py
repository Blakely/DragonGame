import random
import time

#FIX - can't play again, can't time prints

#possible paths
paths = ["There is a fork in the path - left or right (0 or 1)?",
			 "A large tree appears before you - do you go around it, or over it (0 or 1)?",
			 "The path comes to an end at an elevator. Do you go up or down (0 or 1)?",
			 "A small infant comes between you and your goal. Do you punch it, or kick it (0 or 1)?",
			 "You are confronted with a choice, 0 or 1?",
			 "0 or 1?"]

#possible end-of-paths
outcomes = ["ANND you have a Heart attack from the suspense.",
			 "You walk a bit further, but are hit by a sudden epiphany that dictates you spend the rest of your life avoiding caves. You decide to leave.",
			 "EARTHQUAKE! You die.",
			 "You hit a dead end, and your evil half twin has you unexpectedly cornered. He kills you with a small blunt rock.",
			 "A wild Pikachu appears. A pokemon battle ensues, and you completely forget why you came to the cave to begin with.",
			 "Apparently you were being chased by Zombies this whole time. They catch up to you and eat you.",
			 "You stumble upon a dragons lair. A battle ensues, but the dragon overpowers you in the end.",
			 "You see a shiny glimmer at the end of the tunnel. You run towards it and begin to realize that it's a treasure chest with a small, fire-breathing newt sitting atop it. You mush the newt under your boot and claim the treasure."]
	

def displayIntro():
	print("You are a treasure hunter.")
	time.sleep(2)
	print("There are two caves to choose from. Pick one (0 or 1):")

def randomPaths():
	global paths
	randMax = len(paths)
	return random.randint(0,randMax-1)

def randomOutcomes():
	global outcomes
	randMax = len(outcomes)
	return random.randint(0,randMax-1)

def randomizeCaves():
	global paths, outcomes
	
	randomPath={}
	
	for x in range(0,2):
		randomPath[str(x)]=paths.pop(randomPaths())
		for i in range(0,2):
			randomPath[str(x)+str(i)]=paths.pop(randomPaths())
			for b in range(0,2):
				randomPath[str(x)+str(i)+str(b)]=outcomes.pop(randomOutcomes())
	
	return randomPath
		

def getChoice():
	validInput = ("0","1") #valid inputs 
	choice=""
	
	#keep asking for input until user gives valid input
	while (not choice in validInput):
		choice=raw_input()
		
	return choice 

def game():
	global path,currPath,level
	
	#get the next path to take from the user
	currPath=currPath+str(getChoice())
	
	#print the choiecs at this level
	print(str(Path[currPath]))
	
	level = level + 1
	
	#if were not at the third level, recurse! keep going!
	if (level!=3):
		game()
	
currPath="" #the current path string
Path = "" #The master cave path-map
level=0 # the current level

def main():
	global Path,currPath,level

	

	playAgain = 'yes'
	while playAgain == 'yes' or playAgain == 'y':
		Path=randomizeCaves()
		
		displayIntro()
		currPath=""
		level=0
		game()
	
		print ('Do you want to play again? (yes or no)')
		playAgain = raw_input()


if __name__ == "__main__": main()
