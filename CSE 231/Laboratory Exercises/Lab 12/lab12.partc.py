
import cards

# Create the deck of cards

the_deck = cards.Deck()
the_deck.shuffle()

the_deck.display()


print( "Dealt five cards to each player (alternating)" )
print()

player1_list=[]
player2_list=[]
for i in range( 5 ):
    player1_list.append( the_deck.deal() )
    player2_list.append( the_deck.deal() )
    
print("Player 1's stack: ",player1_list)
print("Player 2's stack: ",player2_list)

if input("Continue(ENTER) or quit(x)?: ").lower() != "x":
    battle = True
else:
    battle = False
    

while battle:
    
    if len(player1_list) > 0 and len(player2_list) > 0:    
        player1_card = player1_list.pop(0)
        player2_card = player2_list.pop(0)
    
    print("Player 1's card: ",player1_card)
    print("Player 2's card: ",player2_card)

    
    if player1_card.rank() == 1 or player2_card.rank() == 1:
        if player1_card.rank() == 1:
            print("Player 1 wins this round")
            player1_list.append(player1_card)
            player1_list.append(player2_card)
        elif player1_card.rank() == player2_card.rank():
            print("Both players tie.")
            player1_list.append(player1_card)
            player2_list.append(player2_card)
        elif player2_card.rank() == 1:
            print("Player 2 wins this round")
            player2_list.append(player1_card)
            player2_list.append(player2_card)
    else:    
        if player1_card.rank() == player2_card.rank():
            print("Both players tie.")
            player1_list.append(player1_card)
            player2_list.append(player2_card)
            
            
        elif player1_card.rank() > player2_card.rank():
            print("Player 1 wins this round")
            player1_list.append(player1_card)
            player1_list.append(player2_card)
        else:
            print("Player 2 wins this round")
            player2_list.append(player1_card)
            player2_list.append(player2_card)
        
        
    print("Player 1's stack: ",player1_list)
    print("Player 2's stack: ",player2_list)
    
    if len(player2_list) == 0:
        print("Player 1 wins the game")
        battle = False
    elif len(player1_list) == 0:
        print("Player 2 wins the game")
        battle = False

    
    elif input("Continue(ENTER) or quit(x)?: ").lower() != "x":
        battle = True
    else:
        battle = False
    
    

