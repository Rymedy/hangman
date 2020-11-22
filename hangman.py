# Hangman made by Richard Webb in Python3 using Sublime Text (text editor)
import sys,time,os,random
from vairables import words_fruit
from vairables import words_celebration
from vairables import words_subject
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
					time.sleep(0.05)
				again = input("> ")
				again = again.lower()
				if again == "1":
				  hangman()
				return
def scoresystem():
	score = 0
	score = score + 1
	print ((str(username)) + "'s win score is now " + (str(score)) + "!")

def hangman():

	if __name__ == '__main__':
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
			theme_message = "Decide on a theme, enter 1 for fruit, 2 for celebrations and 3 for school subjects.\n"
			for char in theme_message:
					sys.stdout.write(char)
					sys.stdout.flush()
					time.sleep(0.05)
			word_theme = input("Select a theme: ")
			if word_theme == "1":
				word = random.choice(words_fruit)
				print("░░░░░░░░░░░░░░░░░░░░░░▄█░░░░")
				print("░░░░░░░░░░░░░░░░░░░░▄█░░█░░░")
				print("░░░░░░░░░░░░░░░░░░░█░░██░█░░")
				print("░░░░░░░░░░░░░░░░░▄█░░░░█░▄█░")
				print("░░░░░░░░░░░░░░░▄█░░░░▄░░█░█░")
				print("░░░░░░░░░░░░░░▄█░░░░░░░░▓█▄█")
				print("░░░░░░░░░░░░▄█░░░░░░░░░░▄█░█")
				print("░░░░░░░░░░░█░░░░░░░░░▓█░▄█░█")
				print("░░░░░░░░░▄▓░░░░░░░░░░░░░▄█░█")
				print("░░░░░░░▄█░░░░░░░░░░░░▓█░▄░▄█")
				print("░░░░░░▄█░░░░░░░░░░░░░░░▄█░█░")
				print("░░░░▄█░░░░░░░░░░░░░▄░░░█░▄█░")
				print("░░░█░░░░░░░░░░░░░░░█░▄█░▄█░░")
				print("░▄██░░░▓█░░▄█░░██░░░▄█░▄█░░░")
				print("▒█░░█▓▄░░░░█░░░░░▄██░▄█░░░░░")
				print("░░██▄░░██▓█▄▄██▓█░░▄█░░░░░░░")
				print("░░░░░███▄▄░░░░▄▄█")
				fruit_message = '\nTheme \"Fruits\" has been selected"\n'
				for char in fruit_message:
					sys.stdout.write(char)
					sys.stdout.flush()
					time.sleep(0.05)
			elif word_theme == "2":
				word = random.choice(words_celebration)
				print("                          (             )")
				print("                  )      (*)           (*)      (")
				print("         *       (*)      |             |      (*)")
				print("                  |      |~|           |~|      |          *")
				print("                 |~|     | |           | |     |~|")
				print("                 | |     | |           | |     | |")
				print("                ,| |a@@@@| |@@@@@@@@@@@| |@@@@a| |.")
				print("           .,a@@@| |@@@@@| |@@@@@@@@@@@| |@@@@@| |@@@@a,.")
				print("         ,a@@@@@@| |@@@@@@@@@@@@.@@@@@@@@@@@@@@| |@@@@@@@a,")
				print("        a@@@@@@@@@@@@@@@@@@@@@' . `@@@@@@@@@@@@@@@@@@@@@@@@a")
				print("        ;`@@@@@@@@@@@@@@@@@@'   .   `@@@@@@@@@@@@@@@@@@@@@';")
				print("        ;@@@`@@@@@@@@@@@@@'     .     `@@@@@@@@@@@@@@@@'@@@;")
				print("        ;@@@;,.aaaaaaaaaa       .       aaaaa,,aaaaaaa,;@@@;")
				print("        ;;@;;;;@@@@@@@@;@      @.@      ;@@@;;;@@@@@@;;;;@@;")
				print("        ;;;;;;;@@@@;@@;;@    @@ . @@    ;;@;;;;@@;@@@;;;;;;;")
				print("        ;;;;;;;;@@;;;;;;;  @@   .   @@  ;;;;;;;;;;;@@;;;;@;;")
				print("        ;;;;;;;;;;;;;;;;;@@     .     @@;;;;;;;;;;;;;;;;@@@;")
				print("    ,%%%;;;;;;;;@;;;;;;;;       .       ;;;;;;;;;;;;;;;;@@;;%%%,")
				print(" .%%%%%%;;;;;;;@@;;;;;;;;     ,%%%,     ;;;;;;;;;;;;;;;;;;;;%%%%%%,")
				print(".%%%%%%%;;;;;;;@@;;;;;;;;   ,%%%%%%%,   ;;;;;;;;;;;;;;;;;;;;%%%%%%%,")
				print("%%%%%%%%`;;;;;;;;;;;;;;;;  %%%%%%%%%%%  ;;;;;;;;;;;;;;;;;;;'%%%%%%%%")
				print("%%%%%%%%%%%%`;;;;;;;;;;;;,%%%%%%%%%%%%%,;;;;;;;;;;;;;;;'%%%%%%%%%%%%")
				print("`%%%%%%%%%%%%%%%%%,,,,,,,%%%%%%%%%%%%%%%,,,,,,,%%%%%%%%%%%%%%%%%%%%'")
				print(" `%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%'")
				print("  `%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%'")
				print("             \"\"\"\"\"\"\"\"\"\"\"\"\"\"`,,,,,,,,,'\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"")
				print("                            `%%%%%%%'")
				print("                               %%%")
				print("                              %%%%%")
				print("                           .,%%%%%%%,.")
				print("                      ,%%%%%%%%%%%%%%%%%%%")
				celebration_message = '\nTheme \"Celebrations\" has been selected"\n'
				for char in celebration_message:
					sys.stdout.write(char)
					sys.stdout.flush()
					time.sleep(0.05)
			elif word_theme == "3":
				word = random.choice(words_subject)
				print("                                    ░░░░░░░░░░                                    ░░                          ")
				print("            ░░░░                  ░░░░░░░░▒▒▒▒▒▒▒▒                              ░░░░                          ")
				print("  ░░░░░░    ░░░░░░                ░░░░▒▒▒▒▒▒▒▒▒▒                              ░░░░░░                          ")
				print("  ░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒              ░░░░▒▒▒▒▒▒▒▒▒▒                            ░░░░░░░░                          ")
				print("    ░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒              ░░  ▒▒▒▒▒▒▒▒▒▒                          ░░░░░░░░░░        ░░░░░░░░          ")
				print("          ▒▒▒▒▒▒▒▒▒▒▒▒          ░░░░░░▒▒▒▒▒▒▒▒▒▒          ░░░░░░░░      ░░░░░░░░▒▒░░░░░░    ▒▒▒▒▒▒▒▒          ")
				print("          ▒▒▒▒▒▒▒▒▒▒▒▒░░        ░░░░▒▒▒▒▒▒▒▒▒▒▒▒      ░░░░░░▒▒▒▒▒▒▒▒  ░░░░░░▒▒▒▒░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒          ")
				print("          ░░▒▒▒▒▒▒▒▒▒▒▒▒        ░░░░▒▒▒▒▒▒▒▒▒▒▒▒    ░░▒▒░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░        ▒▒▒▒▒▒▒▒          ")
				print("          ░░▒▒  ▒▒▒▒▒▒▒▒▒▒      ░░░░▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░    ░░▒▒▒▒▓▓▓▓▓▓░░░░▒▒▒▒▒▒▒▒          ▒▒▒▒▒▒▒▒          ")
				print("          ░░▒▒    ▒▒▒▒▒▒▒▒░░  ░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒      ▒▒▓▓▒▒▒▒████▓▓░░░░▒▒▒▒▒▒▒▒          ▒▒▒▒▒▒▒▒▒▒▒▒░░    ")
				print("          ░░▒▒    ▒▒▒▒▒▒▒▒▒▒  ░░░░▒▒  ▒▒▒▒▒▒▒▒▒▒▓▓    ▒▒▒▒▒▒▒▒▒▒████▓▓░░░░▒▒▒▒▒▒▒▒          ▒▒▒▒▒▒▒▒▒▒▒▒▒▒    ")
				print("          ░░▒▒      ▒▒▒▒▒▒▒▒▒▒░░░░▒▒  ▒▒▒▒▒▒▒▒▒▒▒▒  ░░▒▒████▒▒▒▒████▓▓░░░░▒▒▒▒▒▒▒▒          ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒  ")
				print("          ░░▒▒      ▒▒▒▒▒▒▒▒▒▒░░░░▒▒    ▒▒▒▒▒▒▒▒▒▒░░▒▒▓▓████▒▒▒▒████▒▒░░░░▒▒▒▒▒▒▒▒          ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒  ")
				print("          ░░▒▒        ▒▒▒▒▒▒▒▒▒▒░░▒▒  ░░▒▒▒▒▒▒▒▒▓▓▒▒▒▒▓▓██▓▓▒▒▒▒▓▓▓▓▓▓░░░░▒▒▒▒▒▒▒▒        ░░▒▒▒▒▒▒▒▒  ▓▓▒▒▒▒▒▒")
				print("          ░░▒▒        ░░▒▒▒▒▒▒▒▒░░░░░░░░░░░░▒▒▒▒▓▓▒▒▒▒▒▒▓▓▒▒░░░░▓▓▓▓▓▓░░░░▒▒▒▒▒▒▒▒░░░░    ▒▒▒▒▒▒▒▒  ░░▓▓▒▒▒▒▒▒")
				print("          ░░▒▒    ░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒░░▒▒▒▒▒▒▒▒░░░░░░▒▒▒▒▒▒▒▒░░▒▒▒▒▒▒▒▒▒▒▒▒")
				print("            ▒▒░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░▒▒▒▒░░░░░░░░░░▒▒░░░░▒▒▒▒▒▒▒▒▓▓▓▓▒▒▒▒▒▒▒▒  ")
				print("         ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▓▓▓▓▒▒▒▒▒▒▒▒░░   ")
				print("      ░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒")
				print("      ░░░░  ░░░░░░▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░  ░░  ░░    ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒")
				print("      ░░░░░░░░░░░░▒▒░░░░░░░░░░░░░░░░                              ░░░░░░░░░░░░░░░░░░░░░░░░  ░░░░░░░░░░░░░░    ")
				print("      ░░░░░░░░░░░░░░  ░░░░░░░░                                                ░░                              ")
				print("                                                                                    ░░                        ")
				print("                              ░░                            ░░        ░░            ░░░░                      ")
				print("                      ░░                                    ░░░░              ▒▒                              ")
				print("                                    ░░                        ░░░░          ▓▓▒▒  ░░                          ")
				print("                                    ░░  ░░                    ░░            ▒▒░░  ░░                          ")
				print("                              ▒▒▒▒▒▒░░  ░░░░░░░░░░░░░░░░░░                          ░░▒▒▒▒▒▒    ░░▒▒▒▒        ")
				print("              ░░▒▒▒▒▒▒░░      ░░░░          ░░░░░░░░░░░░    ░░    ▒▒▓▓░░      ░░        ░░░░                  ")
				print("                ░░░░░░        ░░                              ░░▓▓▒▒░░░░░░  ▒▒▒▒          ░░░░                ")
				print("                          ░░░░░░                                ░░░░    ░░  ▒▒              ░░░░▒▒▒▒░░        ")
				print("                      ▒▒▒▒▒▒▒▒                                                              ░░░░░░░░░░        ")
				subject_message = '\nTheme \"School Subjects\" has been selected"\n'
				for char in subject_message:
					sys.stdout.write(char)
					sys.stdout.flush()
					time.sleep(0.05)
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
							
							print("You won " + (username) + "!, the word was "+ (word) + "!")
							print("\n")
							print("Would you like to play again?")
							again = str(input("Enter 1 for yes or 2 for no: "))
							if again == "1":
								hangman()
							elif again == "2":
								quit()
							
						else:
							print("Great Job " + (username) + ", that was correct!")




hangman()