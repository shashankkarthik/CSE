
##
## Demonstrate some of the operations of the Fraction class
##

import fraction

def display( arg1, arg2 ):

    print( "Display:", locals() )
    print()
    
    print( "arg1:", arg1 )
    print( "arg2:", arg2 )
    print()

    print( "arg1 + arg2:", arg1 + arg2 )
    print()
    print( "arg1 - arg2:", arg1 - arg2 )
    print()

    print( "arg1 == arg2:", arg1 == arg2 )
    print()
    print( "arg1 < arg2:", arg1 < arg2 )
    print()
    print( "arg1 > arg2:", arg1 > arg2 )
    print()

def main():

    A = fraction.Fraction( 1, 2 )
    B = fraction.Fraction( 2, 3 )

    display( A, B )

main()
