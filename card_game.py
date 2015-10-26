import random as r
deck = [6, 7, 8, 9, 10, 2, 3, 4,11]*4
dealer = []
player = []
c = ''
    
def Hand():
    hand = 0
    for i in player: 
        hand += i #Tally up the total
    #print "The dealer has  %d" % dealer[0]
    print "Your hand totals: %d (%s)" % (hand, player)

#Gives player and dealer their cards
def setup():
    for i in range(2):
        dealDealer = r.choice(deck)
        dealPlayer = r.choice(deck)
        dealer.append(dealDealer)
        player.append(dealPlayer)
        deck.pop(dealDealer)
        deck.pop(dealPlayer)

setup()
while c != 'q':
    Hand()
    answer = raw_input("[H]it [S]tand [Q]uit: ").lower()
   # clear()
    if answer == 'h':
        dealPlayer = r.choice(deck)
        player.append(dealPlayer)
        deck.pop(dealPlayer)
        hand1 = 0
        for i in dealer: hand1 += i
        if not hand1 > 17:   #Dealer strategy.
            dealDealer = r.choice(deck)
            dealer.append(dealDealer)
            deck.pop(dealDealer)
        hand1 = 0
        for i in player: 
            hand1 += i
            if hand1 > 21:
                print "Dealer won"
                player = []     #Clear player hand
                dealer = []     #Clear dealer's hand
                setup()         #Run the setup again
        hand1 = 0
        for i in dealer: 
            hand1 +=i
            if hand1 > 21:
                print "Dealer lost!"
                player = []
                dealer = []
                setup()
    elif answer == 's':
        dHand = 0           #Dealer's hand total
        pHand = 0           #Player's hand total
        for i in dealer: dHand += i
        for i in player: pHand += i
        if pHand > dHand:
            print "You won. Congradulations"    #If playerHand (pHand) is greater than dealerHand (dHand) you win...
        elif pHand == dHand:
            print "Choice"    #If playerHand (pHand) is greater than dealerHand (dHand) you win...
        else:
            print "You lost. I`m sorry." 
            print 'Dealers hand is ' + str(dHand)
        dealer = []
        player = []
        setup()
    else:
        if answer == 'q':
            bye = raw_input("Bye. [Hit Enter]")
        else:
            print "Invalid choice."
