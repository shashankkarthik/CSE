
import random

def sub1( size ):

    values = list()
    for i in range(size):
        values.append(0)
    return values

def sub2( values, size ):

    for n in range(100000):
        i = random.randint(0,size-1)
        values[i] += 1

def sub3( values, size ):
    
    for i in range(size):
        
        print( "\t","{:>3}".format(i),":","{:>7}".format(values[i]) )

def main():

    try: 
        num = int(input("Enter a number:"))
    except ValueError:
        print("Invalid Input. Assuming 10.")
        num = 10
    
    count = sub1( num )

    sub2( count, num )

    sub3( count, num )

main()
