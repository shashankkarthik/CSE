odef squares(start,num):
    count = 1
    total = 0
    while count <= num:
        total += start**2
        start += 1
        count += 1
    
    return total
    

def cubes(start,num):
    count = 1
    total = 0
    while count <= num:
        total += start**3
        start += 1
        count += 1
    return total

def main():
    user_input = input("Squares or cubes: ")
    while user_input != "exit":
        if user_input != "squares" and user_input != "cubes":
            print("***Invalid Choice***")
        
        if user_input == "squares":
                start = int(input("Enter initial integer: "))
                num = int(input("Enter number of terms: "))
                print(squares(start,num))
                
                
        elif user_input == "cubes":
                start = int(input("Enter initial integer: "))
                num = int(input("Enter number of terms: "))
                print(cubes(start,num))
                
                
        user_input = input("Squares or cubes: ")
    
    print("Program Halted Normaly")
                

main()