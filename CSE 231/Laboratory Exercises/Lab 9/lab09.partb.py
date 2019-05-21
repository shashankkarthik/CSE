
def show( x, y ):

    def square( n ):

        print( "\n\tNamespace for function square:" )
        for k,v in locals().items():
            print( "{:>10} {}".format( k, v ) )
            
        return n*n

    def sum( x, y ):
        
        s = square( x )
        t = square( y )

        print( "\n\tNamespace for function sum:" )
        for k,v in locals().items():
            print( "{:>10} {}".format( k, v ) )

        return s + t
        
    z = sum( 2*x, 2*y )
    
    print( "\nValue of x:", x )
    print( "\nValue of y:", y )
    print( "\nValue of z:", z )
    
    print( "\n\tNamespace for function show:" )
    for k,v in locals().items():
        print( "{:>10} {}".format( k, v ) )

def main():

    a = 3
    b = 7
    show( a+1, b-2 )

    print( "\n\tNamespace for function main:" )
    for k,v in locals().items():
        print( "{:>10} {}".format( k, v ) )

main()
