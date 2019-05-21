
S = set()

S.add( 900 )
S.add( 400 )
S.add( 700 )
S.add( 800 )

print( "len(S):", len(S) )       # len(S):

print( "S:", S )                 # S:

S.add( 900 )
print( "S:", S )                 # S:

S.discard( 400 )
print( "S:", S )                 # S:

item = 300
S.discard( item )
print( "S:", S )                 # S:

print( "len(S):", len(S) )       # len(S):

A = 700 in S
print( "A:", A )                 # A:

item = 200
B = item not in S
print( "B:", B )                 # B:
