
def get_integer( prompt ):
    value_str = input( prompt )
    #try:
    value_int = int( value_str )
    #except ValueError:
     #   print ( "** Invalid input, assuming 0 **" )
      #  value_int = 0
    return value_int

def main():
    try:
        try:
            numer = get_integer( "Enter the numerator: " )
        except ValueError:
            print("** Invalid Input, asuming 0 **")
            numer = 0
        
        try:
            denom = get_integer( "Enter the denominator: " )
        except ValueError:
            print("** Invalid Input, asuming 0 **")
            denom = 0
       
       
        result = numer/denom       
        print( numer, "divided by", denom, end=" " )
        print( "yields", result )

    except ZeroDivisionError:
        print( "** Invalid: attempted to divide by zero **" )

    print( "Program halted" )

main()
