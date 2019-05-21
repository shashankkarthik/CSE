
import times

A = times.Time( 6, 15, 30, 5 )
B = times.Time( 8, 9, 15, -4 )
C = times.Time( 14, 20, 45 )
D = times.Time( 23, 59 )
E = times.Time( 12 )
F = times.Time()

S = str(A)
S = repr(A)

F.from_utc( "06:15:30+05" )
F.from_seconds( 2300 )

R = A == B
R = A != B
R = A < B
R = A <= B
R = A > B
R = A >= B

G = A + 300

N = A - B

