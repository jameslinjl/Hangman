import time
from array import *

## function for playing a hangman game ##
def play(word):
	
	wordarray = array('c', [])
	guessedletters = array('c', [])

	i = 0
	while i < len(word):
			wordarray.append('_')
			wordarray.append(' ')
			i = i + 1

	gamemenu = True
	correctcounter = 0
	incorrectcounter = 0

	while gamemenu:
			remainingguesses = 6 - incorrectcounter
			
			## menu selection
			print wordarray.tostring()
			print "Guessed Letters: " + guessedletters.tostring()
			print "Incorrect Guesses Remaining: " + str(remainingguesses)
			selection = raw_input("(1) Guess Letter\n(2) Guess the Word [ONLY ONE CHANCE]\n(3) Quit\n\nSelect what you want to do: ")
			selection = int(selection)

			if selection == 1:
					time.sleep(.5)
						
					letter = raw_input("\nPlease enter a letter you want to guess: ")
					
					## allows you to guess the letters ##
					i = 0
					letterinword = False
					while i < len(word):
							if word[i] == letter[0]:

									letterinword = True
									wordarray.pop(2*i)
									wordarray.insert(2*i, letter[0])
									
									if guessedletters.count(letter[0]) == 0:
										print "\nYou correctly guessed " + letter[0] + "\n"
										correctcounter = correctcounter + word.count(letter[0])
										guessedletters.append(letter[0])
							i = i + 1

					## incorrect guess
					if (not letterinword):
							print "\n" + letter[0] + " is not in the word"
							if guessedletters.count(letter[0]) == 0:
								guessedletters.append(letter[0])
								incorrectcounter = incorrectcounter + 1


					if correctcounter == len(word):
							printwin()
							gamemenu = False

					if incorrectcounter >= 6:
							print "\nOUT OF GUESSES!"
							printlose(word)
							gamemenu = False

			if selection == 2:
					time.sleep(1)
					print "[WARNING: IF YOU ARE WRONG, YOU AUTOMATICALLY LOSE]"
					wordguess = raw_input("\nType in your entire guess here: ")

					i = 0
					match = True
					while i < len(wordguess):
						if word[i] != wordguess[i]:
								match = False
						i = i + 1
					
					if len(word) != len(wordguess):
							match = False
					
					if match:
							printwin()
							gamemenu = False
					else:
							printlose(word)
							gamemenu = False

			if selection == 3:
					gamemenu = False

## function to print winning statement
def printwin():
		print "YOU GOT THE WORD! CONGRATS!"
		time.sleep(.5)
		print "YOU GOT THE WORD! CONGRATS!"
		time.sleep(.5)
		print "YOU GOT THE WORD! CONGRATS!"
		time.sleep(.5)

## function to print losing statement
def printlose(w):
		print "WRONG! WRONG! WRONG! WRONG!"
		time.sleep(.5)
		print "THE WORD IS: " + w
		time.sleep(.5)
		print "THE WORD IS: " + w
		time.sleep(.5)
		
		
		
## start the main module ##
menu = True

while menu:
		print "\n---------------------------------"
		print "WELCOME TO PYTHON WORD GUESSER!!!"
		print "---------------------------------\n"
	

		#Get the menu input from the user and perform basic error checking
		try:
			start = raw_input("(1) Play Game\n(2) Quit\n\nSelect what you want to do: ")
		except KeyboardInterrupt:
			time.sleep(1)
			print "\nSee you soon!"
			exit()

		try:
			number = int(start)
		except ValueError:
			print "Enter an integer please."
			time.sleep(1)
			continue

		#Play the game
		if number == 1:
			time.sleep(.5)
			print "\nHave one person enter a word to guess..."
			time.sleep(.5)
			word = raw_input("\nEnter the word here: ")

			j = 0
			while j < 5: 
				countdown = 5-j
				print("\n" + str(countdown) + "\n")
				print "GET READY!!!\n\n\n\n\n"
				countdown = 5-j
				time.sleep(1)
				j = j+1

			play(word)

		#Valid input type but not an option
		if number != 1 and number != 2:
			print "Please enter a valid number."
			time.sleep(1)
		
		#Quit the game
		if number == 2:
			print "See you soon!"
			menu = False		
	




