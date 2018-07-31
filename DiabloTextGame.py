#name:ExxleeStudios
#date:07-30-2018
#description: A text-based RPG, centered around the world of Diablo 

import time
import random

def displayIntro() :
	time.sleep(4)
	print ('Hello...')
	time.sleep(4)
	print ('...Nephalem')
	time.sleep(5)
	print()
	print('It would appear that our greatest fears have come to pass')
	print()
	time.sleep(4)
	print('Diablo, the Lord of Terror, has once again been set loose')
	print('upon this world.')
	print()
	time.sleep(4)
	print('Regrettably, I could do nothing to prevent the disaster')
	print('which devastated Tristram')
	print()
	time.sleep(4)
	print('However, you, Nephalem, have the power to stop')
	print('Diablo and his minions once and for all')
	print()
	time.sleep(4)
	print('One path leads to the destruction of the world,')
	print()
	time.sleep(4)
	print ('the other leads to finding peace, and defeating the')
	print('minions of Hell')
	print()
	print()
	time.sleep(3)
	
def choosePath() :
	path = ''
	while path != '1' and path != '2':
		path = input('How will you be defined in this life? (1 or 2)')
	
	return path
	
def checkPath(chosenPath):
	print('It takes time to master your skills...')
	time.sleep(2)
	print('Entering the high Heavens, you find Diablo')
	print()
	print('With the might of all Nephalem before you,')
	print()
	
	correctPath = random.randint(1, 2)
	
	if chosenPath == (correctPath):
		print('You destroy Diablo and his minions of hell')
		print('Freeing Tristram of Evil')
		time.sleep(1)
		print('You find peace in the temple of Ytar')
	else:
		    print('Diablo and his Lords of Evil find the World Stone')
		    print('destroying all of Sanctuary')

playAgain = "yes"
while playAgain == "yes" or playAgain == "y":
    displayIntro()
    choice = choosePath()
    checkPath(choice) 
    playAgain = input("Do you want to play again? (yes or y to continue playing): ")



    
	