This text-based python game was made for prelim school assignment.


Documentation | Python3 - Hangman
Statement of Intent
To develop a sophisticated program that allows the user to interact with a text-based hangman game developed in python3 and written in sublime text using programming knowledge using different variables, functions and methods in order to create a text-based hangman game.
Gantt Chart
*Is in image format*
Algorithm
The program then first defines and encases everything but the print hangman function in a hangman function. The program imports the “random” module to be used for randomly selecting a word from a list variable depending on the selected theme. The hangman program takes in user input which is then error checked by the program and checks if the user input is either larger than 1 letter or checks if the user has not input anything, otherwise it will add the user’s input into a list variable as a string through the append function and checks if the user input has not already been guessed by checking if the letter is in the list variable. The blanks are shown through the use of a variable which is multiplied by the length of the word selected. Each blank or underscore is then put into a list variable. The print game function is now called which prints the hangman art depending on what value the attempts variable is currently on. The join function is then used to separate the blanks with a space, a while loop is then called whilst the attempts variable is less then 6 and allows the user to give user input. The user input is then turned into lower case using the lower function to match the given word to ensure capital letters do not affect the attempts variable and is not seen as incorrect. The program then uses a while loop to increment through the word to check if the given user input is the same as one of the letters in the word. The program checks to see if the current list of blanks is equal to the old amount of list blanks, if it is then the program will print incorrect guesses and increment the attempted value. If the amount of letters in the word is not equal to the amount of blanks, the amount of blanks will be made equal to the new amount of blanks variable. If the amount of letters in the word is equal to the amount of blanks, the program will print “You won” and will increment the score variable that was defined at the beginning of the program. The program will print the score variable then open the score.txt file (highscore system) and write the user's username, word theme selected and score. The file will then be read and will prompt the user if they want to reset the high score table by using the truncate function. The user will then be prompted if they want to play again and will call the hangman function.

Pseudocode
START
SCORE = 0
PRINT “Hangman”
USERNAME = USER_INPUT
PRINT Hello “Username”

FUNCTION PRINT_GAME
		If ATTEMPTS = 0 THEN
			PRINT "_____"
			PRINT "║░░\█
			PRINT "   ░░█
			PRINT “   ░░█
			PRINT “   ░░█
			PRINT “   ░░█
			PRINT “════════
		ELSE IF ATTEMPTS = 1 THEN
			PRINT "_____"
			PRINT "║░░\█
			PRINT "O░░█
			PRINT “   ░░█
			PRINT “   ░░█
			PRINT “   ░░█
			PRINT “════════
		ELSE IF ATTEMPTS = 2 THEN
			PRINT "_____"
			PRINT "║░░\█
			PRINT "O░░█
			PRINT “   ░░█
			PRINT “   ░░█
			PRINT “   ░░█
			PRINT “════════
		ELSE IF ATTEMPTS = 3 THEN
			PRINT "_____"
			PRINT "║░░\█
			PRINT "O░░█
			PRINT “/| ░░█
			PRINT “   ░░█
			PRINT “   ░░█
			PRINT “════════
		ELSE IF ATTEMPTS = 4 THEN
			PRINT "_____"
			PRINT "║░░\█
			PRINT "O░░█
			PRINT “/|\ ░ █
			PRINT “   ░░█
			PRINT “   ░░█
			PRINT “════════
		ELSE IF ATTEMPTS = 5 THEN
			PRINT "_____"
			PRINT "║░░\█
			PRINT "O░░█
			PRINT “/|\ ░ █
			PRINT “/  ░░█
			PRINT “   ░░█
			PRINT “════════
		ELSE IF ATTEMPTS = 6 THEN
			PRINT "_____"
			PRINT "║░░\█
			PRINT "O░░█
			PRINT “/|\ ░ █
			PRINT “/ \░░█
			PRINT “   ░░█
			PRINT “════════
			PRINT “Game Over, would you like to play again?”					AGAIN = USER_INPUT
			IF AGAIN = "1" THEN
			  CALL HANGMAN FUNCTION
			RETURN

FUNCTION HANGMAN THEN
		PRINT "Decide on a theme, enter Fruit, Subjects or Celebrations.
		THEME = USER_INPUT
		IF WORD_THEME = "Fruit" THEN
		WORD = RANDOM WORDS_FRUIT
		PRINT “Fruits has been selected”
			ELSE IF WORDS_THEME = "Celebrations" THEN
				WORD = RANDOM WORDS_CELEBRATION
				PRINT “Celebrations have been selected.”
				elif word_theme == "Subjects":
				        word = random.choice(words_subject)
				        PRINT “School Subjects has been selected”
			ATTEMPTS = 0
			LIST_WORD = LIST WORD
			BLANK = "_" * LETTERS IN WORD
			LIST_BLANK = LIST BLANK
			NEW_LISTBLANK = LIST BLANK
			ATTEMPT_LIST = []
			CALL PRINT_GAME FUNCTION
			WHILE ATTEMPTS < 6 THEN
				ATTEMPT = USER_INPUT
				IF LETTERS IN ATTEMPT > 1 THEN
					PRINT "Invalid guess. Enter at least 1 letter"
				ELSE IF ATTEMPT = "" THEN
					PRINT "Please enter a guess."
				ELSE IF ATTEMPT IN ATTEMPT_LIST THEN
					PRINT "Invalid Guess”
				OTHERWISE THEN
					ATTEMPT_LIST + ATTEMPT
					i = 0
					WHILE i < LETTERS IN WORD THEN
						IF ATTEMPT = WORD INCREMENT THEN
							NEW_LISTBLANK INCREMENT = LISTWORD INCREMENT
						i = i + 1

					if NEW_LISTBLANK = LISTBLANK THEN
						PRINT "Incorrect Guess, try again."
						ATTEMPTS = ATTEMPTS + 1
						CALL PRINT_GAME FUNCTION

						IF ATTEMPTS < 6 THEN
							PRINT "Guess again."

					ELSE IF LISTWORD != LISTBLANK THEN

						LISTBLANK = NEW_LISTBLANK

						if LISTWORD = LISTBLANK THEN
							SCORE = SCORE + 1
							PRINT "You won!”							                        PRINT "Log/Highscore Table"
							OPEN “score.txt" 
							PRINT "Play again? Yes?")
							AGAIN = USER_INPUT							            IF AGAIN = "1" THEN
								CALL HANGMAN FUNC
							ELSE IF AGAIN == "2: THEN
								QUIT FUNCTION

						OTHERWISE THEN
							PRINT "Great Job!”
CALL HANGMAN FUNCTION
END
Data structure/type
String Variables
Integer Variables
List Variables

String Variables
I used string variables to store different text such as the username that was input from the user or the blank variable which was used to store the “_”’/blanks.

Integer Variables
I used integer variables to store the score variable and the amount of letters or amount of blanks in different variables or for the attempts variable to check how many times the user has guessed.

List Variables
I used list variables for both encasing the words in different themed variables as well as using list variables for appending the users input to check if the letter had already been guessed.
Logbook


Date/Time
Logged Task
19/11/2020 | 9:42am
Received assessment task.
Basic startup, downloading python3, sublime text.
Worked on basic user input (asking user to enter username) and storing user input info via variable (“username”).

20/11/2020 | 2:51pm
Started defining functions such as “hangman()” and specifically “print_game()” function to print hangman text art.

20/11/2020 | 10:17pm
Started and finished working on basic functionality such as replacing blank spaces with letters from the word using the len() function.

21/11/2020 | 8:48pm
Made basic error testing such as testing if the letter had already been guessed through adding user input to a list variable. 
Also implemented error testing to detect if user input is valid or not.

23/11/2020 | 5:42pm
Started and finished work on theme selection and difficulty.

29/11/2020 | 2:12pm
Started and finished score functionality and started working on highscore and saving high score in a separate txt file.


Test data
In order to test my program I used just three words for each theme and tried them all with 3 attempts to correctly make sure each theme is working. “apple”, “fruit”, “birthday” and commented the ‘random’ function out in order to quickly test my program. For the username I entered my name “Richard” to show if the username was displaying as proper. I also then entered all the letters in each word, eg. for apple “a”, “p”, “l”, “e”. When prompted if I wanted to reset the table I had entered “Reset” and when prompted to play again played again another two times in order to test the two other themes and then entered to quit on the third run of the program. Everything had worked successfully with no errors.


Evaluation
Therefore I have successfully created a hangman text-based game using python which has greatened my knowledge of programming language python as well as similarities to other programming languages.
