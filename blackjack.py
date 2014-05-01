######### Python Blackjack ##########
#	Author: Pragith
#	Website: http://pragith.net
#	GitHub: http://github.com/Pragith
#####################################




import random

######## SETTINGS #########

money = 1000

##########################







######## HELPERS #########

#cards = ["A","K","Q","J","10","9","8","7","6","5","4","3","2"]
cards = ["A","J"]
player = []
dealer = []
player_total = 0
dealer_total = 0

def total(cards):
	value = 0

	for card in cards:
		if (card == 'K' or card == 'Q' or card == 'J'):
			value = value + 10
		elif (card == 'A'):
			value = value + 11
		else:
			value = value + int(card)
	
	if (value > 21):
		value = 0
		
		for card in cards:
			if (card == 'K' or card == 'Q' or card == 'J'):
				value = value + 10
			elif (card == 'A'):
				value = value + 1
			else:
				value = value + int(card)

	return value

def result(total):
	global money

	if (total > 21):
		return "BUSTED!"
	elif (total == 21):
		money = money + (bet_amount*2.5)
		return "BLACK JACK!"
	else:
		return "continue"


def draw(p,count):
	global dealer
	global player
	global player_total
	global dealer_total

	c = random.sample(cards,count)
	if (p == "player"):
		for x in c:
			player.append(x)
			player_total = total(player)
	elif (p == "dealer"):
		for x in c:
			dealer.append(x)
			dealer_total = total(dealer)

def show(p):
	for card in p:
		print card,
	print "\n"
##########################







######## MAIN #########


#0 - Betting for the round
def bet():
	global money
	global bet_amount
	
	print "Balance:",money
	#bet_amount = input("Your bet:")
	bet_amount = 50
	money = money - bet_amount
	play()	




def play():
	global money
	global bet_amount
	global dealer
	global player

	print "\n"



	#1 - Dealer (1 open, 1 closed)
	print "Dealer:"
	draw("dealer",2)
	print "("+str(total(dealer[0]))+")",dealer[0],"#\n"



	#2 - Player
	print "You:"
	draw("player",2)
	print "("+str(total(player))+")",
	show(player)


	### Declare result if the user already hits BlackJack
	if (result(player_total) != "continue"):
		print result(player_total)
		print "Balance:",money
		choice = 2

	else:

		#3 - Options to player - Hit, Stand, Double
		choice = input("Hit(1)  Stand(2)  Double(3) : ")


		#### Choice - Hit (Double or Nothing)
		while (choice == 3):
			bet_amount = bet_amount*2
			money = money - bet_amount

			print "Bet:",bet_amount
			print "Balance:",money
			draw("player",1)
			print "("+str(player_total)+")",show(player)
			print result(player_total)
			choice = 2


		#### Choice - Hit (Normal)
		while (choice == 1):

			print "Bet:",bet_amount
			print "Balance:",money
			
			draw("player",1)
			print "("+str(player_total)+")",show(player)

			if (result(player_total) == "continue"):
				choice = input("Hit(1)  Stand(2): ")
			else:
				print result(player_total)
				choice = 2


	

	#4 - Play till user hits Stand / crosses 21
	if (choice == 2):
		#5 - Dealer plays till lt or eq to Player / crosses 21
		dealer_total = total(dealer)

		print "Dealer's turn:"
		print "("+str(dealer_total)+")",show(dealer)
		#print "~~~~ Player Total:",player_total
		
		if (dealer_total > player_total and dealer_total <= 21):
			print "***** Dealer wins! ****"
		

		while (dealer_total <= 21):
			
			if (dealer_total != 21):
				draw("dealer",1)
				dealer_total = total(dealer)

			print "("+str(dealer_total)+")",show(dealer)

			if (dealer_total > player_total and dealer_total <= 21):
				print "***** Dealer wins! ****"
				break

			elif (dealer_total == player_total):
				######## Bring random choice to continue or stand if eq to Player
				print "***** Push ****"
				money = money + bet_amount
				break

			elif (dealer_total < player_total):
				print "***** You win! ****"
				money = money + (2*bet_amount)
				break

		print "Balance:",money

##########################



bet()