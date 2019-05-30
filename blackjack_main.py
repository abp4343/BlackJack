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
			blackjackClasses.Player(player_name_balance[count*2 - 2], player_name_balance[count*2 - 1])

	#increment count
		count += 1

	return player_dict

#asks players for bets
def let_us_bet (player_object_dictionary):
	#create list of player bets in order to pay out correct amount at end of game
	bet_list = []

	for player_number in player_object_dictionary:

		#create var to ensure that player has bet an allowable amount
		check_amt = player_object_dictionary[player_number].balance

		#ensure allowable bet has been placed
		while (check_amt == player_object_dictionary[player_number].balance):

			#ask for bet
			bet_amt = input("{player}, you have ${balance}, how much would you like to wager?\t"\
						.format(player = player_object_dictionary[player_number].name,\
						balance = player_object_dictionary[player_number].balance))

			#try to convert string to int, else ask for bet_amt again
			try: 
				bet_amt = int(bet_amt)

			except:
				print("\nBet must be a whole number.")
				continue

			#add bet_amt to bet_list and pass bet amt to player method, bet()
			bet_list.append(bet_amt)
			player_object_dictionary[player_number].bet(bet_amt)

	#declare what is next

	print("\n\n\n\nNow that all bets have been placed, we may begin the deal.")

	return bet_list


"""
initially deal two cards to player then to dealer.
"""

def initial_deal(deck, player_obj_dict):

	#deal cards to player
	for player in player_obj_dict:

		card1 = deck.cards.pop();
		card2 = deck.cards.pop();

		player_obj_dict[player].hand.append(card1)
		player_obj_dict[player].score += card1.value

		player_obj_dict[player].hand.append(card2)
		player_obj_dict[player].score += card2.value

		#check if player drew an Ace
		if(card1.number == 'Ace' or card2.number == 'Ace'):
			player_obj_dict[player].ace = True

		#separate players by dashes
		print("-------------------------------------------------------------------------------------")

		#consider if player wishes to use ace as 11 points rather than 1 point
		if(player_obj_dict[player].score == 11):
			player_obj_dict[player].score += 10
			print("\n{player}, you drew:\n\n\t{card1}\n\t{card2}\n\nTotal Points: {points}"\
				.format(player = player_obj_dict[player].name, card1 = card1.name,\
				card2 = card2.name, points = player_obj_dict[player].score))
		
		elif(player_obj_dict[player].ace):
			print("\n{player}, you drew:\n\n\t{card1}\n\t{card2}\n\nTotal Points: {points}"\
				.format(player = player_obj_dict[player].name, card1 = card1.name,\
				card2 = card2.name, points = player_obj_dict[player].score))

			print("(or {points_a} points if you wish to make your Ace worth 11 points)"\
				.format(points_a = player_obj_dict[player].score + 10))

		else:

			print("\n{player}, you drew:\n\n\t{card1}\n\t{card2}\n\nTotal Points: {points}"\
				.format(player = player_obj_dict[player].name, card1 = card1.name,\
				card2 = card2.name, points = player_obj_dict[player].score))

		print("-------------------------------------------------------------------------------------")

	#return list of dealer's cards
	dealer_cards = []
	card1 = deck.cards.pop();
	card2 = deck.cards.pop();

	dealer_cards.append(card1)
	dealer_cards.append(card2)

	print("\nThe dealer's visible card is the {card}".format(card = card1.name))
	print("-------------------------------------------------------------------------------------")

	return dealer_cards

"""
Create function based on whether player wants to hit or stand
"""

def hit_or_stand(deck, player_obj_dict):

	#go through each player until each player wants to stand or goes over 21
	for player in player_obj_dict:

		#create boolean for as long as player wants to hit
		is_hit = True;

		#separate players by dashes
		print("-------------------------------------------------------------------------------------\n")

		#while player wants more cards and player value <= 21, loop
		while(is_hit):

			#check bust
			if(player_obj_dict[player].score > 21):
				print("{player}, you have busted.".format(player = player_obj_dict[player].name))
				break

			if(player_obj_dict[player].score == 21):
				print("{player}, you have automatically won!".format(player = player_obj_dict[player].name))
				break

			#loop until valid answer is given
			while(True):

				#ask player for hit/stand
				y_or_n = input("{player}, would you like to hit or stand? ('Y' for hit, 'N' for stand)\t"\
							.format(player = player_obj_dict[player].name)).capitalize()

				#check if valid answer is given
				if(y_or_n != "Y" and y_or_n != "N"):
					print("Invalid Choice! Try again!\n")
					continue

				else:
					break

			#check if user said they wished to hit or not
			if(y_or_n == "Y"):
				card1 = deck.cards.pop();

				#add card to hand and add value of card to player's point total
				player_obj_dict[player].hand.append(card1)
				player_obj_dict[player].score += card1.value

				#check if player drew an ace
				if(card1.number == 'Ace'):
					player_obj_dict[player].ace = True

				#consider if player wishes to use ace as 11 points rather than 1 point
				if(player_obj_dict[player].ace and player_obj_dict[player].score + 10 < 21):
					print("\n{player}, you have drawn the {card1},\nwith a new point total of {points} points."\
						.format(player = player_obj_dict[player].name, card1 = card1.name, points = player_obj_dict[player].score))

					print("(or {points_a} points if you wish to make your Ace worth 11 points)"\
						.format(points_a = player_obj_dict[player].score + 10))

					continue

				elif(player_obj_dict[player].ace and player_obj_dict[player].score + 10 == 21):

					#assign an ace as 11
					player_obj_dict.score += 10

					print("\n{player}, you have drawn the {card1},\nwith a new point total of {points} points."\
						.format(player = player_obj_dict[player].name, card1 = card1.name, points = player_obj_dict[player].score))

				else:
					print("\n{player}, you have drawn the {card1},\nwith a new point total of {points} points."\
						.format(player = player_obj_dict[player].name,\
						card1 = card1.name, points = player_obj_dict[player].score))

					continue

			else:
				is_hit = False
			
		print("-------------------------------------------------------------------------------------")	

'''
Allow dealer to draw until he exceeds 17 points
'''

def dealer_draws(deal_cards, deck):

	dealer_points = deal_cards[0].value + deal_cards[1].value
	has_ace = False

	#check if dealer cards contains an ace
	for card in deal_cards:
		if(card.number == 'Ace'):
			has_ace = True

	#if dealer initial hand value is at least 17
	if(dealer_points >= 17):

		#explain that dealer will stand because his hand value is at least 17
		print("The dealer's initial cards are:\n{card1}\n{card2}\n"\
			.format(card1 = deal_cards[0].name, card2 = deal_cards[1].name))

		print("-------------------------------------------------------------------------------------")

		print("The dealer has at least 17 points ({points_a} points to be exact)."\
			.format(points_a = dealer_points))
		print("And so, the dealer will stand with the cards he has.\n")

		print("-------------------------------------------------------------------------------------")

		#return dealer points
		return dealer_points

	#if dealer uses ace as 11 and hand value is at least 17
	elif(has_ace and dealer_points + 10 >= 17):

		dealer_points += 10
		#explain that dealer will stand because his hand value is at least 17
		print("The dealer's initial cards are:\n{card1}\n{card2}\n"\
			.format(card1 = deal_cards[0].name, card2 = deal_cards[1].name))

		print("-------------------------------------------------------------------------------------")

		print("By using the Ace as 11 points, the dealer has at least 17 points ({points_a} points to be exact)."\
			.format(points_a = dealer_points))
		print("And so, the dealer will stand with the cards he has.\n")

		print("-------------------------------------------------------------------------------------")

		#return dealer points
		return dealer_points

	#if dealer has ace and hand value is less than 17
	elif(has_ace and dealer_points + 10 < 17):

		#print initial cards and points
		print("The dealer's initial cards are:\n{card1}\n{card2}\n"\
			.format(card1 = deal_cards[0].name, card2 = deal_cards[1].name))

		print("-------------------------------------------------------------------------------------")

		print("The dealer does not have at least 17 points (currently, {points_a} points to be exact)."\
			.format(points_a = dealer_points + 10))
		print("And so, the dealer will draw another card until he gets at least 17 points or he busts.\n")

		print("-------------------------------------------------------------------------------------")

		#draw until dealer has at least 17 points
		while(dealer_points < 17):

			#draw card, add to dealer's hand, add worth of card to dealer's points
			card1 = deck.cards.pop();
			deal_cards.append(card1)
			dealer_points += card1.value

			#report to player's what dealer drew along with new point total
			if(dealer_points + 10 >= 17 and dealer_points + 10 <= 21):

				dealer_points += 10

				#explain that dealer will stand because his hand value has hit at least 17
				print("The dealer drew the card:\n{card}\n"\
					.format(card = card1.name))

				print("-------------------------------------------------------------------------------------")

				print("By using the Ace as 11 points, the dealer has at least 17 points ({points_a} points to be exact)."\
					.format(points_a = dealer_points))
				print("And so, the dealer will stand with the cards he has.\n")

				print("-------------------------------------------------------------------------------------")

				#return dealer points
				return dealer_points

			elif(dealer_points >= 17):

				if(dealer_points <= 21):

					#explain that dealer will stand because his hand value has hit at least 17
					print("The dealer drew the card:\n{card}\n"\
						.format(card = card1.name))

					print("-------------------------------------------------------------------------------------")

					print("The dealer has at least 17 points ({points_a} points to be exact)."\
						.format(points_a = dealer_points))
					print("And so, the dealer will stand with the cards he has.\n")

					print("-------------------------------------------------------------------------------------")

					#return dealer points
					return dealer_points

				else:

					#explain that dealer will stand because his hand value has hit at least 17
					print("The dealer drew the card:\n{card}\n"\
						.format(card = card1.name))

					print("-------------------------------------------------------------------------------------")

					print("The dealer has at least 17 points, but has exceeded 21 points ({points_a} points to be exact)."\
						.format(points_a = dealer_points))
					print("And so, the dealer has busted.\n")

					print("-------------------------------------------------------------------------------------")

					#return dealer points
					return dealer_points

			else:
				continue

	else:

		#print initial cards and points
		print("The dealer's initial cards are:\n{card1}\n{card2}\n"\
			.format(card1 = deal_cards[0].name, card2 = deal_cards[1].name))

		print("-------------------------------------------------------------------------------------")

		print("The dealer does not have at least 17 points (currently, {points_a} points to be exact)."\
			.format(points_a = dealer_points))
		print("And so, the dealer will draw another card until he gets at least 17 points or he busts.\n")

		print("-------------------------------------------------------------------------------------")

		#draw until dealer has at least 17 points
		while(dealer_points < 17):

			#draw card, add to dealer's hand, add worth of card to dealer's points
			card1 = deck.cards.pop();
			deal_cards.append(card1)
			dealer_points += card1.value

			#check if card is an ace
			if(card1.name == 'Ace'):
				has_ace = True

			#report to player's what dealer drew along with new point total
			if(has_ace and dealer_points + 10 >= 17 and dealer_points + 10 <= 21):

				dealer_points += 10

				#explain that dealer will stand because his hand value has hit at least 17
				print("The dealer drew the card:\n{card}\n"\
					.format(card = card1.name))

				print("-------------------------------------------------------------------------------------")

				print("By using the Ace as 11 points, the dealer has at least 17 points ({points_a} points to be exact)."\
					.format(points_a = dealer_points))
				print("And so, the dealer will stand with the cards he has.\n")

				print("-------------------------------------------------------------------------------------")

				#return dealer points
				return dealer_points

			elif(dealer_points >= 17):

				if(dealer_points <= 21):

					#explain that dealer will stand because his hand value has hit at least 17
					print("The dealer drew the card:\n{card}\n"\
						.format(card = card1.name))

					print("-------------------------------------------------------------------------------------")

					print("The dealer has at least 17 points ({points_a} points to be exact)."\
						.format(points_a = dealer_points))
					print("And so, the dealer will stand with the cards he has.\n")

					print("-------------------------------------------------------------------------------------")

					#return dealer points
					return dealer_points

				else:

					#explain that dealer will stand because his hand value has hit at least 17
					print("The dealer drew the card:\n{card}\n"\
						.format(card = card1.name))

					print("-------------------------------------------------------------------------------------")

					print("The dealer has at least 17 points, but has exceeded 21 points ({points_a} points to be exact)."\
						.format(points_a = dealer_points))
					print("And so, the dealer has busted.\n")

					print("-------------------------------------------------------------------------------------")

					#return dealer points
					return dealer_points

			else:
				continue

'''
calculate final player points
'''

def final_points (player_obj_dict):

	#cycle through players
	for player in player_obj_dict:

		#check if player has ace
		if(player_obj_dict[player].ace == True and player_obj_dict[player].score <= 11):
			player_obj_dict[player].score += 10

'''
determine winners and losers of the game and payout to winners
'''

def win_or_loss(player_obj_dict, dealer_points, bet_amts):

	#cycle through players
	for player in player_obj_dict:

		#convert digit in player key to an index beginning at 0
		bet_number = int(player[-1]) - 1

		#case 1: player busts, player loses
		if(player_obj_dict[player].score > 21):
			print("\n{player}, you have lost the game.".format(player = player_obj_dict[player].name))

		#case 2: player wins automatically
		elif(player_obj_dict[player].score == 21):
			print("\n{player}, you have automatically won the game.".format(player = player_obj_dict[player].name))

			#add bet to player balance
			player_obj_dict[player].balance += (2 * bet_amts[bet_number])

		#case 3: dealer busts, player wins
		elif(dealer_points > 21):
			print("\n{player}, the dealer has busted and you have not, so you have won.".format(player = player_obj_dict[player].name))

			#add bet to player balance
			player_obj_dict[player].balance += (2 * bet_amts[bet_number])

		#case 4: player score > dealer score, player wins
		elif(player_obj_dict[player].score > dealer_points):
			print("\n{player}, your score is higher than the dealer's, so you have won.".format(player = player_obj_dict[player].name))

			#add bet to player balance
			player_obj_dict[player].balance += (2 * bet_amts[bet_number])

		#final case: dealer score > player score, player loses
		else:
			print("\n{player}, the dealer's score is higher than yours, so you have lost.".format(player = player_obj_dict[player].name))

		print("-------------------------------------------------------------------------------------")

'''
output player balances, remove players with no money left, ask if remaining players wish to play again
'''
def new_values(player_obj_dict):
	print("| Player Name | Player Balance |")
	print("--------------------------------")

	#print player name and balance
	for player in player_obj_dict:

		#count digits of player balance to have properly formatted table
		count = 0
		new_balance = player_obj_dict[player].balance

		#check if balance is 0
		if(new_balance == 0):
			count = 1

		else:
			while(new_balance != 0):
				new_balance = new_balance // 10
				count += 1

		player_length = len(player_obj_dict[player].name)
		#check to see if player name is short enough to fit the table
		if(player_length > 11):

			#ensure proper alignment of table
			print("| {player}.. |".format(player = player_obj_dict[player].name[:9]),\
				"{balance}".format(balance = player_obj_dict[player].balance),\
				" " * (13 - count), "|")

		else:

			#ensure proper alignment of table
			print("| {player}".format(player = player_obj_dict[player].name),\
				" " * (10 - player_length), "|", "{balance}".format(balance = player_obj_dict[player].balance),\
				" " * (13 - count), "|")

'''
Asks player what they wish to do next
Case 1: End Game
Case 2: Reset Game (entire game resets)
Case 3: Play again (players with $0 will be dropped)
'''

def now_what(player_obj_dict):

	#create a sort of menu
	print("What do you wish to do next? (3 options)\n")

	print("1: End Game")
	print("2: Reset Game (entire game resets)")
	print("3: Play Again (players with $0 will be dropped)\n\n")

	while(True):
		
		will_run = True
		will_play = True

		#continue to loop until a valid number between 1 and 3 is entered.
		game_choice = input("Choose an option (must be a number between 1 and 3)\n\n")

		if game_choice == "1" or game_choice == "2" \
		or game_choice == "3":
			game_choice = int(game_choice)

		else:
			print("Choice must be between 1 and 3. \n")
			continue

		if (game_choice == 1):

			print("\n\nThank you for playing!")

			will_run = False
			will_play = False

			break

		elif(game_choice == 2):

			y_or_n = input("You are wishing to reset the game. Are you sure? ('Y' for yes.  Any other key for no.)")

			if(y_or_n.capitalize() == "Y"):
				
				break

			else:
				continue

		else:

			print("You are wishing to play again. All players with $0 will be unable to play.")
			y_or_n = input("Are you sure? ('Y' for yes.  Any other key for no.)\n")

			if(y_or_n.capitalize() == "Y"):
				
				#delete players from dict if players have $0
				for player in player_obj_dict:

					#check player balance
					if(player_obj_dict[player].balance == 0):

						print("{player} is being removed from the game.".format(player = player_obj_dict[player].name))

						#delete players with a balance of $0
						del player_obj_dict[player]
						continue

				will_run = False

			else:
				continue

	run_list = [will_run, will_play]

	return run_list


#begin main program

is_running = True
is_playing = True
running_list = []

while(True):

	while(is_running):
		welcome()

		#create and shuffle deck
		blackjack_deck = blackjackClasses.Deck()
		blackjack_deck.build_deck()
		blackjack_deck.shuffle_deck()


		#create list of player object arguments
		player_instances = name_balance_assignment(how_many)

		#assign player arguments to each player object, store in a dictionary
		player_dict = player_dictionary(player_instances)

		break

	while(is_playing):

		#ask for bets
		bet_amounts = let_us_bet(player_dict)

		#deal initial cards
		dealer_cards = initial_deal(blackjack_deck, player_dict)

		#ask players to hit or stand
		hit_or_stand(blackjack_deck, player_dict)

		#dealer draws until he reaches at least 17
		dealer_points = dealer_draws(dealer_cards, blackjack_deck)

		#calculate final points (including Aces)
		final_points(player_dict)

		#determine whether each player won or lost
		win_or_loss(player_dict, dealer_points, bet_amounts)

		#print player names and balances
		new_values(player_dict)

		#determine what player wishes to do next
		running_list = now_what(player_dict)

		break

	#game will be ended
	if(running_list[0] == False and running_list[1] == False):

		break

	#players with money left will play again
	elif(running_list[0] == False and running_list[1] == True):

		#print remaining players
		print("After deleting players with $0, here are the remaining players:\n\n")
		new_values(player_dict)
		print("\n\nGood luck to these players as they play once more.\n")

		#ensure remaining players are not welcomed once again...go directly to player bets
		is_running = False
		continue

	#game will reset
	else:
		print("The game will now be reset.")
