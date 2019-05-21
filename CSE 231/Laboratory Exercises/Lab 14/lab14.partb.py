
##
## Demonstrate some of the operations of the Pet classes
##

import pets

def main():
    
    try:

        # Hamster
        A = pets.Pet( "Hamster" )
        print( A )       
        
        # Dog named Fido who chases Cats
        B = pets.Dog( "Fido","Rocks" )
        print( B )

        # Cat named Fluffy who hates everything
        C = pets.Cat( "Fluffy", "severything" )
        print( C )
        
        R = pets.Pet("Rock")

    except pets.PetError:
        print( "Got a pet error." )

main()

