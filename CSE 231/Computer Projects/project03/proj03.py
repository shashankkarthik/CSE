#############################################################################
#	Computer project 3
#
#	Algorithm
#		prompt user for input
#		initialize count variables
#		while user input is not "q"
#			check to see if input is valid
#			count type of input
#			generate randomized computer input
#			print the input values of user and computer
#			check to see who wins
#				count who wins
#			promt user to enter command for next game
#		if user input is "q"
#			stop game
#			print appropiately formatted statistics
#
#############################################################################


import random
random.seed(0)

print(''' 
Welcome to the Rock-Paper-Scissors game.
Enter a single character: r, s, p, or q to quit.
Rock beats Scissors which beats Paper which beats Rock.
	''')


user_input = input("Enter a command (rpsq): ") #Gets user input


count_games = 0
count_comp_won = 0
count_user_won = 0
count_ties = 0
count_rock = 0
count_paper = 0
count_scissors = 0


while user_input != "q":

	#Checks to see if user input is in (rspq)
	if user_input == "r" or user_input == "p" or user_input == "s":
		count_games += 1

		#Counts the type of user input
		if user_input == "r":
			count_rock += 1
		if user_input == "p":
			count_paper += 1
		if user_input == "s":
			count_scissors += 1

		#Generates a random number from the values 1,2 and 3
		comp_rand = random.randint(1,3) 

		#Assigns the computer input based on the generated value above
		if comp_rand == 1:	
			comp_input = "r"
		if comp_rand == 2:
			comp_input = "s"
		if comp_rand == 3:
			comp_input = "p"
		
		print("User chose",user_input," and the computer chose",comp_input)

		

		computer_win = "Computer wins this round"
		user_win = "User wins this round"



		#Checks to see who wins
		if user_input == "r" and comp_input == "s":
			print(user_win)
			count_user_won += 1
		elif user_input == "r" and comp_input == "p":
			print(computer_win)
			count_comp_won += 1

		elif user_input == "s" and comp_input == "r":
			print(computer_win)
			count_comp_won += 1

		elif user_input == "s" and comp_input == "p":
			print(user_win)
			count_user_won += 1

		elif user_input == "p" and comp_input == "r":
			print(user_win)
			count_user_won += 1
		elif user_input == "p" and comp_input == "s":
			print(computer_win)
			count_comp_won += 1


		elif user_input == comp_input:
			print("This round is a tie")
			count_ties += 1

		print("------------------------")

	else:
		print("Error. Try again.")


	#Asks user to play again
	user_input = input("\nEnter a command (rpsq): ")



#Prints game statistics 
print("\nSummary statistics")
print("\tUser wins:",count_user_won,"(",round(count_user_won/count_games*100,\
	1),"%)")
print("\tComputer wins:",count_comp_won,"(",round(count_comp_won/count_games*\
	100,1),"%)")
print("\tTies:",count_ties,"(",round(count_ties/count_games*100,1),"%)")

print("User statistics")
print("\tRock:",count_rock,"(",round(count_rock/count_games*100,1),"%)")
print("\tPaper:",count_paper,"(",round(count_paper/count_games*100,1),"%)")
print("\tScissors:",count_scissors,"(",round(count_scissors/count_games*100,1\
	),"%)")