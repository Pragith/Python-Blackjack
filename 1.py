#6 - Results and winnings returned



import random

######## SETTINGS #########

money = 1000

##########################






######## HELPERS #########

cards = ["A","6","5","4","3","2"]
player = []
dealer = []

def total(cards):
	value = 0
	if (('A' in cards) and (value > 21)):
		value_of_a = 1
		print "inside if a and >21"
	elif (('A' in cards) and (value < 21)):
		value_of_a = 11

	for card in cards:
		if (card == 'A' or card == 'K' or card == 'Q' or card == 'J'):
			if (card == 'A'):
				value = value + value_of_a
				print "inside if to add val of a",value_of_a
			else:
				value = value + 10
		else:
			value = value + int(card)
	return value


def result(total):
	global money

	if (total > 21):
		return "BUSTED!"
	elif (total == 21):
		money = money + (bet*2)
		return "BLACK JACK!"
	else:
		return "continue"


def draw(p,count):
	global dealer
	global player
	c = random.sample(cards,count)
	if (p == "player"):
		for x in c:
			player.append(x)
	elif (p == "dealer"):
		for x in c:
			dealer.append(x)

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
	#show(dealer)
	print "("+str(total(dealer[0]))+")",dealer[0],"#\n"


	#2 - Player
	print "You:"
	draw("player",2)
	print "("+str(total(player))+")",
	show(player)


	
	#3 - Options to player - Hit, Stand, Double
	choice = input("Hit(1)  Stand(2)  Double(3) : ")

	#Hit (Double or Nothing)
	while (choice == 3):
		bet_amount = bet_amount*2
		money = money - bet_amount

		print "Balance:",money
		player.append(random.sample(cards,1)[0])
		player_total = total(player)
		print "("+str(player_total)+")",show(player)
		print result(player_total)
		choice = 2

	#Hit (Normal)
	while (choice == 1):

		print "Balance:",money
		
		player.append(random.sample(cards,1)[0])
		player_total = total(player)
		print "("+str(player_total)+")",show(player)

		if (result(player_total) == "continue"):
			choice = input("Hit(1)  Stand(2): ")
		else:
			print result(player_total)
			choice = 2


	

	#4 - Play till user hits Stand / crosses 21
	if (choice == 2):
		#5 - Dealer plays till gt Player / crosses 21
		print "Dealer's turn:"


##########################



bet()