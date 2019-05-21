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

def init_game():
    '''Return a tuple (stock, tableau, foundation) for a new game, where
       - stock is a shuffled deck minus the 4 cards dealt to the tableau 
       - foundation is an empty list
       - tableau is a list of lists, each containing one of the dealt cards
    '''
    return (None, None, None)  # stub so that the skeleton compiles; delete 
                               # and replace it with your code
    
def deal_to_tableau( stock, tableau ):
    '''Deal a card from the stock to each column of the tableau.'''
    # Remember to consider the case when the stock has fewer than 4 cards.
    pass  # stub; delete and replace it with your code


def display( stock, tableau, foundation ):
    '''Display the stock, tableau, and foundation.'''
    # See the specifications for display requirements
    pass  # stub; delete and replace it with your code   

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
    return []   # stub; delete and replace with your code
            
def validate_move_to_foundation( tableau, from_col ):
    '''Return True if the rules allow the bottom card in the tableau column  
       specified by from_col to be moved to the foundation; False, otherwise.
       If the move is invalid, print an appropriate error message.
    '''
    # A card can be moved to the foundation only if a higher ranked card 
    # of the same suit is at the bottom of a Tableau column.
    return False  # stub; delete and replace it with your code   

    
def move_to_foundation( tableau, foundation, from_col ):
    '''If valid, move a card from the tableau column specified by from_col to 
       the foundation.
    '''
    pass  # stub; delete and replace it with your code   


def validate_move_within_tableau( tableau, from_col, to_col ):
    '''Return True if the rules allow the bottom card in the tableau column  
       specified by from_col to be moved to the tableau column specified by
       to_col; False, otherwise.
       If the move is invalid, print an appropriate error message.
    '''
    return False  # stub; delete and replace it with your code



def move_within_tableau( tableau, from_col, to_col ):
    '''If valid, move a card from the tableau column specified by from_col 
       to the tableau column specified by to_col. 
    '''
    pass  # stub; delete and replace it with your code   

        
def check_for_win( stock, tableau ):
    '''Return True if the game is won: the only cards left in the tableau are
       the 4 aces and the stock is empty.  Otherwise, return False
    '''
    return False  # stub; delete and replace it with your code   

        
stock, tableau, foundation = init_game()
print( MENU )
display( stock, tableau, foundation )

while True:
    # Your code goes here
    display( stock, tableau, foundation)



