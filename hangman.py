# Hangman made by Richard Webb in Python3 using Sublime Text (text editor)
import sys,time,os,random
from variables import words_fruit, words_celebration, words_subject
# Define global variables
score = 0
# Introduction to Hangman (Basic input and print commands)
# Used a text art converter for this.
print("██╗░░██╗░█████╗░███╗░░██╗░██████╗░███╗░░░███╗░█████╗░███╗░░██╗██╗".center(119, '░'))
print("██║░░██║██╔══██╗████╗░██║██╔════╝░████╗░████║██╔══██╗████╗░██║██║".center(119, '░'))
print("███████║███████║██╔██╗██║██║░░██╗░██╔████╔██║███████║██╔██╗██║██║".center(119, '░'))
print("██╔══██║██╔══██║██║╚████║██║░░╚██╗██║╚██╔╝██║██╔══██║██║╚████║╚═╝".center(119, '░'))
print("██║░░██║██║░░██║██║░╚███║╚██████╔╝██║░╚═╝░██║██║░░██║██║░╚███║██╗".center(119, '░'))
print("╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝░╚═════╝░╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝╚═╝".center(119, '░'))
print("█▄▄░█▄█░░░█▀█░█░█▀▀░█░█░▄▀█░█▀█░█▀▄░░░█░█░█░█▀▀░█▄▄░█▄▄".center(119, '░'))
print("█▄█░░█░░░░█▀▄░█░█▄▄░█▀█░█▀█░█▀▄░█▄▀░░░▀▄▀▄▀░██▄░█▄█░█▄█".center(119, '░'))
username = input("Enter your username: ")
print("Hello "+(username)+"!, Welcome to Hangman!")
# Function that prints the hangman drawing
def print_game(attempts, word):
		if(attempts == 0):
				print("_____")
				print("║░░\█")
				print("  ░░█")
				print("  ░░█")
				print("  ░░█")
				print("  ░░█")
				print("════════")
		elif(attempts == 1):
				print("_____")
				print("║░░\█")
				print("O ░░█")
				print("  ░░█")
				print("  ░░█")
				print("  ░░█")
				print("════════")
		elif(attempts == 2):
				print("_____")
				print("║░░\█")
				print("O ░░█")
				print("| ░░█")
				print("  ░░█")
				print("  ░░█")
				print("════════")
		elif(attempts == 3):
				print(" _____")
				print(" ║░░\█")
				print(" O ░░█")
				print("/| ░░█")
				print("   ░░█")
				print("   ░░█")
				print("════════")
		elif(attempts == 4):
				print(" _____")
				print(" ║░░\█")
				print(" O ░░█")
				print("/|\░░█")
				print("   ░░█")
				print("   ░░█")
				print("════════")
		elif(attempts == 5):
				print(" _____")
				print(" ║░░\█")
				print(" O ░░█")
				print("/|\░░█")
				print("/  ░░█")
				print("   ░░█")
				print("════════")
		elif(attempts == 6):
				print(" _____")
				print(" ║░░\█")
				print(" O ░░█")
				print("/|\░░█")
				print("/ \░░█")
				print("   ░░█")
				print("════════")
				playagain_message = "\nThe word was " + (word) + "\nGame Over!\nWould you like to play again?, enter 1 for yes or 2 for no.\n"
				for char in playagain_message:
					sys.stdout.write(char)
					sys.stdout.flush()
					time.sleep(0.03)
				again = input("> ")
				again = again.lower()
				if again == "1":
				  hangman()
				return






def hangman(score):
	if __name__ == '__main__':
			theme_message = "Decide on a theme, enter \'Fruit\' (Easy), \'Subjects\' (Medium) or \'Celebrations\' (Hard).\n"
			for char in theme_message:
					sys.stdout.write(char)
					sys.stdout.flush()
					time.sleep(0.03)
			theme = input("Select a theme: ")
			word_theme = theme.capitalize()
			if word_theme == "Fruit":
				word = random.choice(words_fruit)
				print("███████╗██████╗░██╗░░░██╗██╗████████╗░██████╗")
				print("██╔════╝██╔══██╗██║░░░██║██║╚══██╔══╝██╔════╝")
				print("█████╗░░██████╔╝██║░░░██║██║░░░██║░░░╚█████╗░")
				print("██╔══╝░░██╔══██╗██║░░░██║██║░░░██║░░░░╚═══██╗")
				print("██║░░░░░██║░░██║╚██████╔╝██║░░░██║░░░██████╔╝")
				print("╚═╝░░░░░╚═╝░░╚═╝░╚═════╝░╚═╝░░░╚═╝░░░╚═════╝░")
				fruit_message = '\nTheme \"Fruits\" has been selected"\n'
				for char in fruit_message:
					sys.stdout.write(char)
					sys.stdout.flush()
					time.sleep(0.03)
			elif word_theme == "Celebrations":
				word = random.choice(words_celebration)
				print("░█████╗░███████╗██╗░░░░░███████╗██████╗░██████╗░░█████╗░████████╗██╗░█████╗░███╗░░██╗░██████╗")
				print("██╔══██╗██╔════╝██║░░░░░██╔════╝██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝██║██╔══██╗████╗░██║██╔════╝")
				print("██║░░╚═╝█████╗░░██║░░░░░█████╗░░██████╦╝██████╔╝███████║░░░██║░░░██║██║░░██║██╔██╗██║╚█████╗░")
				print("██║░░██╗██╔══╝░░██║░░░░░██╔══╝░░██╔══██╗██╔══██╗██╔══██║░░░██║░░░██║██║░░██║██║╚████║░╚═══██╗")
				print("╚█████╔╝███████╗███████╗███████╗██████╦╝██║░░██║██║░░██║░░░██║░░░██║╚█████╔╝██║░╚███║██████╔╝")
				print("░╚════╝░╚══════╝╚══════╝╚══════╝╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝░╚════╝░╚═╝░░╚══╝╚═════╝░")
				celebration_message = '\nTheme \"Celebrations\" has been selected"\n'
				for char in celebration_message:
					sys.stdout.write(char)
					sys.stdout.flush()
					time.sleep(0.03)
			elif word_theme == "Subjects":
				word = random.choice(words_subject)
				print("░██████╗██╗░░░██╗██████╗░░░░░░██╗███████╗░█████╗░████████╗░██████╗")
				print("██╔════╝██║░░░██║██╔══██╗░░░░░██║██╔════╝██╔══██╗╚══██╔══╝██╔════╝")
				print("╚█████╗░██║░░░██║██████╦╝░░░░░██║█████╗░░██║░░╚═╝░░░██║░░░╚█████╗")
				print("░╚═══██╗██║░░░██║██╔══██╗██╗░░██║██╔══╝░░██║░░██╗░░░██║░░░░╚═══██╗")
				print("██████╔╝╚██████╔╝██████╦╝╚█████╔╝███████╗╚█████╔╝░░░██║░░░██████╔╝")
				print("╚═════╝░░╚═════╝░╚═════╝░░╚════╝░╚══════╝░╚════╝░░░░╚═╝░░░╚═════╝░")
				subject_message = '\nTheme \"School Subjects\" has been selected"\n'
				for char in subject_message:
					sys.stdout.write(char)
					sys.stdout.flush()
					time.sleep(0.03)
			attempts = 0
			listWord = list(word)
			blank = "_"*len(word)
			listBlank = list(blank)
			new_listBlank = list(blank)
			attempt_list = []
			print_game(attempts, word)
			print("\n")
			print(""+''.join(listBlank))
			print("\n")
			# While the game is not lost (below 6 attempts), allow the user to guess a letter and turns the letter into lowercase.
			while attempts < 6:
				attempt = str(input("Guess a letter: "))
				attempt = attempt.lower()
				# Checks if the user's guess is not above 1 letter.
				if len(attempt) > 1:
					print("Invalid guess, enter one letter per guess.")
				# Checks if the user has given an input/guess.
				elif attempt == "":
					print("Please enter a guess.")
				# Checks if the user has given a letter that has already been guessed.
				elif attempt in attempt_list:
					print("You've already guessed that letter, here's what you've guessed.")
					print(' '.join(attempt_list))
				# Otherwise adds the user's letter into the attempt_list variable and defines vairable [i] as value 0.
				else:
					attempt_list.append(attempt)
					i = 0
					# While the amount of letters in the word.
					while i < len(word):
						if attempt == word[i]:
							new_listBlank[i] = listWord[i]
						i = i + 1

					if new_listBlank == listBlank:
						print("Incorrect Guess, try again.")
						attempts = attempts + 1
						print_game(attempts, word)

						if attempts < 6:
							print("Guess again.")
							print(' '.join(listBlank))

					elif listWord != listBlank:

						listBlank = new_listBlank[:]
						print(' '.join(listBlank))

						if listWord == listBlank:
							print("██╗░░░██╗░█████╗░██╗░░░██╗░░██╗░░░░░░░██╗░█████╗░███╗░░██╗██╗".center(119, '░'))
							print("╚██╗░██╔╝██╔══██╗██║░░░██║░░██║░░██╗░░██║██╔══██╗████╗░██║██║".center(119, '░'))
							print("░╚████╔╝░██║░░██║██║░░░██║░░╚██╗████╗██╔╝██║░░██║██╔██╗██║██║".center(119, '░'))
							print("░░╚██╔╝░░██║░░██║██║░░░██║░░░████╔═████║░██║░░██║██║╚████║╚═╝".center(119, '░'))
							print("░░░██║░░░╚█████╔╝╚██████╔╝░░░╚██╔╝░╚██╔╝░╚█████╔╝██║░╚███║██╗".center(119, '░'))
							print("░░░╚═╝░░░░╚════╝░░╚═════╝░░░░░╚═╝░░░╚═╝░░░╚════╝░╚═╝░░╚══╝╚═╝".center(119, '░'))	
							blankline = "______________________________________________________________________________________________________________________"		
							score = score + 1
							print("You won " + (username) + "!, the word was "+ (word) + "!, Your score is currently " + (str(score)) + "!")
							print("Log/Highscore Table")
							print(blankline)
							# Open the score.txt file and make (writable)
							with open("score.txt", "a") as highscoreFile:
							# Iterate over each line in the file
								# write line to output file
								highscoreFile.write("Username: " + (username))
								highscoreFile.write("\n")
								highscoreFile.write("Theme: " + (word_theme))
								highscoreFile.write("\n")
								highscoreFile.write("Highscore: " + (str(score)))
								highscoreFile.write("\n")
								highscoreFile.write(blankline)
								highscoreFile.write("\n")
								highscoreFile.close()
							highscoreFile = open("score.txt", "r")
							print(highscoreFile.read())
							print("Would you like to reset/clear the current highscore table?")
							resetHighscoreTable = input("Enter \'Reset\' to reset the table or nothing to continue: ")
							resetTable = resetHighscoreTable.capitalize()
							if resetTable == "Reset":
								highscoreFile = open("score.txt", "r+")
								highscoreFile.truncate(0)
								highscoreFile.close()
							else:
								pass
							print("\n")
							print("Would you like to play again?")
							print("NOTE: You may lose progress on your score!")
							again = str(input("Enter 1 for yes or 2 for no: "))
							if again == "1":
								hangman(score)
							elif again == "2":
								quit()

						else:
							print("Great Job " + (username) + ", that was correct!")


hangman(score)