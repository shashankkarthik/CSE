#########################
def prime_factors(n):
# this function returns prime factors of n
    import math
    import time
    i = 2
    m = n
    s = ''
    x = math.sqrt(n)
    while n!=1:
        if n <= 0: break                #To prevent infinite loop by bad input
        if i > x:
               s = s + str(n)
               break

        if n%i == 0:
               s = s + str(i) + '*'
               n = n//i
        else:
               i=i+1

    print (s)
    return s


def main():
    n = int(input("Enter number: "))
    prime_factors(n)

main()
