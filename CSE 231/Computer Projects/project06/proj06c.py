#############################################################################
#	Computer project 6a
#	
#	Algorithm
#		try to open input data file
#               if unable to open, end program
#
#           prompt user for number of months(N)
#           check if input is valid
#
#           create list containing lists of each line in file
#           convert list elements to integers
#           
#           for N times
#               create a tuple containing temp,year,month for each month
#               add each tupple to a list
#           sort the list of tuples
#           reverse the list of tuples
#           print out appropiately formatted data
#############################################################################




try:
    input_file = open("data_full.txt","r")
    run_program = 0
except FileNotFoundError:
    print("Input file not found. Ending program.")
    run_program = 1
    
while run_program == 0:
    valid_input = 0
    
    while valid_input == 0:
        n = input("Enter Number of months(N): ")
    
        try:
            n = int(n)
            if n > 0:
                valid_input = 1
            else:
                print("That is not a valid input.")
        except ValueError:
            print("That is not a valid input.")
        
    
    lst_all = []
    for line in input_file: 
        line_lst = line.split() #Creates a list containing each line of the file
        lst_all.append(line_lst) 
        
    
    lst_all = lst_all[1:]   #Removes title line in data file.     
    
    lst_ints = []
    for i in lst_all:
        lst = [int(a) for a in i]
        lst_ints.append(lst)
    
    lst_tuples = []
    
    for year in lst_ints:
        
        #Creats a tuple for each month of the year
        tuple_jan = (year[1],year[0],"Jan")
        tuple_feb = (year[2],year[0],"Feb")
        tuple_mar = (year[3],year[0],"Mar")
        tuple_apr = (year[4],year[0],"Apr")
        tuple_may = (year[5],year[0],"May")
        tuple_jun = (year[6],year[0],"Jun")
        tuple_jul = (year[7],year[0],"Jul")
        tuple_aug = (year[8],year[0],"Aug")
        tuple_sep = (year[9],year[0],"Sep")
        tuple_oct = (year[10],year[0],"Oct")
        tuple_nov = (year[11],year[0],"Nov")
        tuple_dec = (year[12],year[0],"Dec")
        
        #Appends each tupple to list
        lst_tuples.append(tuple_jan)
        lst_tuples.append(tuple_feb)
        lst_tuples.append(tuple_mar)
        lst_tuples.append(tuple_apr)
        lst_tuples.append(tuple_may)
        lst_tuples.append(tuple_jun)
        lst_tuples.append(tuple_jul)
        lst_tuples.append(tuple_aug)
        lst_tuples.append(tuple_sep)
        lst_tuples.append(tuple_oct)
        lst_tuples.append(tuple_nov)
        lst_tuples.append(tuple_dec)
    
    
    lst_tuples.sort()       #Sorts list in ascending order of temperature
    lst_tuples.reverse()   #Reverses list so it is in decending order of temperature
    
    
    
    title  = "{:4}{:1}{:7}{:5}".format("YEAR"," ","MONTH","TEMP.")
    print(title)
    print("-----------------")
    for i in range(n):
        x = lst_tuples[i]
        y = "{:4}{:2}{:5}{:5}".format(x[1]," ",x[2],x[0])
        print(y)
    run_program = 1



    