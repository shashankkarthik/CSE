
M = dict()
M[ "Joyce" ] = 7
M[ "Mike" ] = 12
M[ "Bea" ] = 9

print( "M:", M )              # M: 

M[ "Mike" ] = 33
M[ "Bea" ] = M[ "Bea" ] * 5

print( "M:", M )              # M:

if "Bea" in M:
    A = M[ "Bea" ]
    print( "A:", A )          # A:

if "Will" in M:
    B = M[ "Will" ]
    print( "B:", B )          # B:

C = M.get( "Bea" )
print( "C:", C )              # C:

D = M.get( "Will" )
print( "D:", D )              # D:

if "Joyce" in M:
    del M[ "Joyce" ]

if "Will" in M:
    del M[ "Will" ]

print( "M:", M )              # M:

E = M.pop( "Mike", None )
print( "E:", E )              # E:

F = M.pop( "Will", None )
print( "F:", F )              # F:

print( "M:", M )              # M:
