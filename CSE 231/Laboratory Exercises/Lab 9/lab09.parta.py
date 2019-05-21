
def display( y ):
    
    x = 2
    print( "\nIn display, x:", x )
    print( "\nIn display, y:", y )
    
    print( "\n\tNamespace for function display:" )
    for k,v in locals().items():
        print( "{:>10} {}".format( k, v ) )

    return

def main():
    
    x = 6
    display( x+2 )

    print( "\nIn main, x:", x )

    print( "\n\tNamespace for function main:" )
    for k,v in locals().items():
        print( "{:>10} {}".format( k, v ) )

    return

main()
