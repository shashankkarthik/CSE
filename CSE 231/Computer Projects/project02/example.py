
# The following two statements must appear in Project #2

import random
random.seed( 0 )

for value in range( 5 ):

    # Function gauss expects two arguments:
    #   the desired mean and the desired standard deviation
    
    dist = random.gauss( 100.0, 15.0 )

    # Display the distribution rounded to 4 digits of accuracy
    #   and without rounding
    
    print( )
    print( "Rounded:  ", round( dist, 4) )
    print( "Unrounded:", dist )
