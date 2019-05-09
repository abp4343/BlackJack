"""

Name: Alexander Parker
Date: 04/03/2019
File Name: blackjack_main.py

Description: This script executes the gameplay of the BlackJack Game.
"""
#before anything else, import the modules from the blackjack_components package.
from blackjack_components import blackjack_classes as blackjackClasses

#Welcome the users
def welcome():
	print("Hello, welcome to the virtual Blackjack game! Each player will start with a balance of $1000. Let us begin.")


#how many people are playing?
def how_many():
	while True:

		#continue to loop until a valid number between 1 and 4 is entered.
		number_of_players = input("How many players are there? Enter a number between 1 and 4. \n\n")
		if number_of_players == "1" or number_of_players == "2" \
		or number_of_players == "3" or number_of_players == "4":
			number_of_players = int(number_of_players)
			break
		else:
			print("Number of players must be between 1 and 4. \n")
			continue
	return number_of_players


#puts all player's names and balances into a list
def name_balance_assignment(number):

	#declare list that will be returned
	assigned_values = []

	#ask for number of players
	number_of_players = number()

	#for each player, add their name and balance to list
	for player in range(number_of_players):
		player_name = input("What is player " + str(player + 1) + "'s name?\t")
		assigned_values.append(player_name)
		assigned_values.append(1000)

	#return desired list containing player instances
	return assigned_values

#creates a player class instance for each player for 1-4 players and stores in dict
def player_dictionary (player_name_balance):

	count = 1
	player_dict = {}

	while(count <= len(player_name_balance) / 2):

		#convert count number to string
		temp_string = str(count)

		#assign each dict key with a player object as its value
		player_dict['player' + temp_string] = \
				blackjackClasses.Player\
				(player_name_balance[count*2 - 2], player_name_balance[count*2 - 1])

	#increment count
		count += 1

	return player_dict

#asks players for bets
def let_us_bet (player_object_dictionary):
	for player_number in player_object_dictionary:

		#create var to ensure that player has bet an allowable amount
		check_amt = player_object_dictionary[player_number].balance

		#ensure allowable bet has been placed
		while (check_amt == player_object_dictionary[player_number].balance):

			#ask for bet
			bet_amt = input(player_object_dictionary[player_number].name + ", make a bet:\t")

			#try to convert string to int, else ask for bet_amt again
			try: 
				bet_amt = int(bet_amt)

			except:
				print("\nBet must be a whole number.")
				continue

			#pass bet amt to player method, bet()	
			player_object_dictionary[player_number].bet(bet_amt)


#begin main program
welcome()

player_instances = name_balance_assignment(how_many)

player_dict = player_dictionary(player_instances)

let_us_bet(player_dict)