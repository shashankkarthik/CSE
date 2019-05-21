################################################################################
# Computer Project 11
#   Algorithim
#       import module Time from times.py
#       Call function to test each method in module Time
################################################################################

from times import Time
import sys

sys.stdout = open('log.txt','w')
def test(Test):
    '''
    Tests each method in Time module
    '''

    #Tests __init__ method
    A = Time(6,15,30,5)
    B = Time(8,9,15,-4)
    C = Time(14,20,45)
    D = Time(23,59)
    E = Time(12)
    F = Time() 

    try:
        Time("a", "b", "c", "d")
    except ValueError:
        print("Time(a, b, c, d) generated Value Error")

    print()
    print("-"*60)
    print()

    #Tests __str__ and __repr__ methods
    print("A",str(A))
    print("B",repr(B))
    print("C",str(C))
    print("D",repr(D))
    print("D",str(E))
    print("D",repr(F))

    print()
    print("-"*60)
    print()

    #Tests from_str method
    T = Time()
    T.from_str("06:15:30+05")
    print("After T.from_str('06:15:30+05'), T is", T)

    print()

    try:
        T.from_str("12:79:00+00")
    except ValueError:
        print("T.from_str('12:79:00+00') generated a Value Error")

    print()
    print("-"*60)
    print()

    #Tests get_as_local method
    a = A.get_as_local()
    b = B.get_as_local()
    c = C.get_as_local()
    d = D.get_as_local()
    e = E.get_as_local()
    f = F.get_as_local()

    print("A: {}; A.get_as_local(): {}".format(A,a))
    print("B: {}; B.get_as_local(): {}".format(B,b))
    print("C: {}; C.get_as_local(): {}".format(C,c))
    print("D: {}; D.get_as_local(): {}".format(D,d))
    print("E: {}; E.get_as_local(): {}".format(E,e))
    print("F: {}; F.get_as_local(): {}".format(F,f))

    print()
    print("-"*60)
    print()    

    #Tests methods __eq__, __ne__, __lt__, __gt__, __le__ and __ge__
    T1 = Time( 7, 35, 15, -6 )
    T2 = Time( 7, 21, 30, -5 )
    print("T1, T2:", T1, "," , T2)

    print("T1 == T2 is,", T1 == T2)
    print("T1 != T2 is,", T1 != T2) 
    print("T1 < T2 is,", T1 < T2)
    print("T1 <= T2 is,", T1 <= T2) 
    print("T1 > T2 is,", T1 > T2)
    print("T1 >= T2 is,", T1 >= T2) 

    print()

    try:
        T1 == 3
        T1 != 3
        T1 < 3
        T1 <= 3
        T1 > 3
        T1 >= 3
    except TypeError:
        print("T1 == 3 generated a ValueError")
        print("T1 != 3 generated a ValueError")
        print("T1 < 3 generated a ValueError")
        print("T1 <= 3 generated a ValueError")
        print("T1 > 3 generated a ValueError")
        print("T2 >= generated a ValueError")

    print()
    print("-"*60)
    print()

    #Tests module __add__ 
    T1 = Time( 23, 15, 0, 5 )
    print("T1:",T1) 
    T2 = T1 + 300
    print("T2 = T1 + 300:", T2)
    T3 = T1 + 3600
    print("T3 = T1 + 3600:", T3)
    T4 = T1 + -90000
    print("T4 = T3 + -9000:", T4)

    print()

    try:
        T5 = 360 + T1
    except TypeError:
        print("T5 = 360 + T1 generated a TypeError")

    print()
    print("-"*60)
    print()

    #Tests module __sub__
    T1 = Time( 14, 20, 45 ) 
    T2 = Time( 14, 18, 15 )

    print("T1,T2: ",T1,",",T2)
    print()
    print("T1-T2:",T1-T2)
    print("T2-T2:",T2-T1) 

    print("-"*30)

    T1 = Time( 7, 35, 15, -6 ) 
    T2 = Time( 7, 21, 30, -5 )

    print("T1,T2: ",T1,",",T2)
    print()
    print("T1-T2:",T1-T2)
    print("T2-T2:",T2-T1) 

    print()
    print("-"*60)
    print()


def main():
    test(Time)


main()
