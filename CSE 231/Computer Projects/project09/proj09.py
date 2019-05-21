import cards  # required !!!

RULES = '''
Aces High Card Game:
     Tableau columns are numbered 1,2,3,4.
     Only the card at the bottom of a Tableau column can be moved.
     A card can be moved to the Foundation only if a higher ranked card
        of the same suit is at the bottom of another Tableau column.
     To win, all cards except aces must be in the Foundation.'''

MENU = '''
Input options:
    D: Deal to the Tableau (one card on each column).
    F x: Move card from Tableau column x to the Foundation.
    T x y: Move card from Tableau column x to empty Tableau column y.
    R: Restart the game (after shuffling)
    H: Display the menu of choices
    Q: Quit the game
'''
OPTION_ERROR = "Error in option: "

ILLEGAL_MOVE = "Illegal Move"


def init_game():
    '''Return a tuple (stock, tableau, foundation) for a new game, where
       - stock is a shuffled deck minus the 4 cards dealt to the tableau
       - foundation is an empty list
       - tableau is a list of lists, each containing one of the dealt cards
    '''
    stock = cards.Deck()
    stock.shuffle()
    tableau = [[], [], [], []]
    deal_to_tableau(stock, tableau)
    foundation = []

    return (stock, tableau, foundation) 


def deal_to_tableau(stock, tableau):
    '''Deal a card from the stock to each column of the tableau.'''
    for i in tableau:
        i.append(stock.deal()) 


def display(stock, tableau, foundation):
    '''Display the stock, tableau, and foundation.'''
    if len(foundation) > 0:
        last_in_foundation = foundation[-1]
        print("{}{:10}{}{:10}{}".format(" XX","",tableau,"",last_in_foundation))
    else:
        print("{}{:10}{}{:10}{}".format(" XX","",tableau,"",foundation))

# DONE
def get_option():
    '''Prompt the user for an option and check that the input has the
       form requested in the menu, printing an error message, if not.
       Return:
       - empty list, if the input is not of the requested form
       - ['D'], for Deal
       - ['F', x], for move to foundation, where x is the (int) tableau index
            of the specified column number
       - ['T', x, y], for move within the tableau, where x and y are the (int)
            tableau indices of the specified column numbers
       - ['R'], for restart
       - ['H'], for displaying the menu
       - ['Q'], for quit
    '''
    try:
        option = input("Input an option (DFTRHQ): ")
        option_up = option.upper()
        if option_up in "DRHQ:":
            return option_up
        else:

            if option_up[0] == "F":
                option_lst = option_up.split(" ")
                if option_lst[1].isdigit():
                    option_lst[1] = int(option_lst[1])
                if option_lst[1] >= 1 and option_lst[1] <= 4:
                    if len(option_lst) == 2:
                        return option_lst
                else:
                    print(OPTION_ERROR,option)
                    return False
                    

            if option_up[0] == "T":
                option_lst = option_up.split(" ")
                option_lst[1] = int(option_lst[1])
                option_lst[2] = int(option_lst[2])
                if option_lst[1] >= 1 and option_lst[1] <= 4:
                    if option_lst[2] >= 1 and option_lst[2] <= 4:
                        return option_lst
                else:
                    print(OPTION_ERROR,option)
                    return False
        

    except:
        print(OPTION_ERROR, option)
        return False

# DONE
def validate_move_to_foundation(tableau, from_col):
    '''Return True if the rules allow the bottom card in the tableau column
       specified by from_col to be moved to the foundation; False, otherwise.
       If the move is invalid, print an appropriate error message.
    '''
    bottom_cards = []
    for col in tableau:
        if len(col) > 0:
            last_card = col[-1]
        bottom_cards.append(last_card)

    card_select = bottom_cards[from_col - 1]
    # print(card_select)
    # print()
    count = 0
    for card in bottom_cards:
        if card.suit() == card_select.suit():
            # print(card,get_rank(card))
            if get_rank(card) > get_rank(card_select):
                return True
            else:
                count += 1
        else:
            count += 1
        if count == 4:
            return False  

# DONE
def move_to_foundation(tableau, foundation, from_col):
    '''If valid, move a card from the tableau column specified by from_col to
       the foundation.
    '''
    card = tableau[from_col - 1].pop(-1)
    foundation.append(card)

# DONE
def validate_move_within_tableau(tableau, from_col, to_col):
    '''Return True if the rules allow the bottom card in the tableau column
       specified by from_col to be moved to the tableau column specified by
       to_col; False, otherwise.
       If the move is invalid, print an appropriate error message.
    '''

    bottom_cards = []
    for col in tableau:
        if len(col) > 0:
            last_card = col[-1]
        else:
            last_card = []
        bottom_cards.append(last_card)
    if bottom_cards[to_col - 1] == []:
        return True
    else:
        return False  

# DONE
def move_within_tableau(tableau, from_col, to_col):
    '''If valid, move a card from the tableau column specified by from_col
       to the tableau column specified by to_col.
    '''
    card = tableau[from_col - 1].pop(-1)
    tableau[to_col - 1].append(card)  

#DONE
def check_for_win(stock, tableau):
    '''Return True if the game is won: the only cards left in the tableau are
       the 4 aces and the stock is empty.  Otherwise, return False
    '''
    if len(stock) == 0:
        card_count = 0
        for col in tableau:
            if len(col) == 1:
                card = col[0]
                if get_rank(card) == 14:
                    card_count += 1
                if card_count == 4:
                    return True
    else:
        return False    

# DONE
def get_rank(card):
    rank = card.rank()
    if rank == 1:
        rank = 14
    return rank

def main():
    stock, tableau, foundation = init_game()
    print(RULES)
    print(MENU)
    display(stock, tableau, foundation)
    option = get_option()
    while option != "Q":
        if option != False:

            if option == "D":
                if len(stock) > 0:
                    deal_to_tableau(stock,tableau)
                else:
                    print(OPTION_ERROR,option)

            elif option[0] == "F":
                from_col = option[1]
                if validate_move_to_foundation(tableau,from_col):
                    move_to_foundation(tableau,foundation,from_col)
                else:
                    print(ILLEGAL_MOVE)

            elif option[0] == "T":
                from_col = option[1]
                to_col = option[2]

                if validate_move_within_tableau(tableau,from_col,to_col):
                    move_within_tableau(tableau,from_col,to_col)
                else:
                    print(ILLEGAL_MOVE)

            elif option == "R":
                stock, tableau, foundation = init_game()
                print(RULES)
                print(MENU)

            if option == "H":
                print(MENU)


        display(stock, tableau, foundation)
        if check_for_win(stock,tableau):
            print("You Win!")
            option = "Q"
        else:
            option = get_option()       

main()