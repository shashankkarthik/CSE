def calc( X=1, Y=2 ):

    try:
        return X % Y
        
    except TypeError:
        return 5

def process( A=0, B=0 ):

    V, Z = (0, 0)

    try:
        Z = calc( int(A), B )

    except ValueError:
        V += 16

    except ZeroDivisionError:
        V += 8

    except:
        V += 4

    else:
        V += 2

    finally:
        V += 1

    return (V, Z)

def main():

    print( process( 4.75 ) )        # _______________________

    print( process( 10.5, 3 ) )     # _______________________

    print( process( "one", 4 ) )    # _______________________

    print( process( 8, "two" ) )    # _______________________

main()
