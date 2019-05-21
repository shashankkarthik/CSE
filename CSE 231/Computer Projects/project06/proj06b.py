#############################################################################
#   Computer project 6b
#	
#   Algorithm
#       function get_data:
#          Takes input file as arguement
#           Creates list of all lines in file
#           prompt user for starting year 
#           if the user input is any variation of "all"
#           select the entire file
#           finds index of line with starting year
#           prompts user to input integer number
#           if integer number is invalid
#           prompt user to re-enter number
#           append the line of the starting year to a list
#           append each of the consecutinve years to same list
#           return above list
#           close input file.
#
#       function process_data:
#           takes list with all the data for the years selected
#           creates new list with all the values stored as integers
#           sums the temperature(last 12 values of each list)
#           removes the individuals temperatures from each list leaving the year
#           averages temps and rounds them to 0 decimal places.
#           convert rounded averages to integers
#           append the rounded averages to the lists with just the year
#           returns this list.
#
#       function output_data:
#           takes takes processed data and output file as arguments
#           formats data appropialtely
#           writes formatted data to output file
#           returns output file
#           closes output file
#       
#       function main:
#           creates file object for input file
#           if input file can't be opened
#           end program
#           prompts user for output file name
#           creates file object for output file
#           calls get_data on input file
#           calls process_data
#           calls output_data
#       
#       call main
#############################################################################



def get_data(input_file):
    '''
    Takes input file as arguement
    Creates list of all lines in file
    prompt user for starting year 
    if the user input is any variation of "all"
        select the entire file
    finds index of line with starting year
    prompts user to input integer number
    if integer number is invalid
        prompt user to re-enter number
    append the line of the starting year to a list
    append each of the consecutinve years to same list
    return above list
    close input file.
    '''
    lst_all = []
    lst_select = []
    lst_years = []
    line_count = 0
    for line in input_file: 
        line_count += 1
        line_lst = line.split() #Creates a list containing each line of the file
        lst_all.append(line_lst) 
        for i in line:
            lst_years.append(i[0])
    
    
    year = input("Enter a year: ")
    
    if year.lower() == "all":
        lst_select = lst_all[1:]
        
    else:
        for i in lst_all:
            if i[0] == year:
                year_index = lst_all.index(i)   #Gets index of starting line
        if year not in lst_years:
            print("Year not found. Ending program.")
            return
                
        n = input("Enter an integer number: ")
        x = 0
        while x == 0:
            try:
                n = int(n)
                x += 1
            except ValueError:
                 print("Invalid entry")
                 n = input("Enter an integer number: ")  
            
        count = 0
        while count < n:
            next_year_index = year_index + count
            try:
                next_year = lst_all[next_year_index]  #Gets index of next line
                lst_select.append(next_year)
            except IndexError:
                pass     
            count += 1
            
    return lst_select
    input_file.close()



def process_data(lst_select):
    '''
    takes list with all the data for the years selected
    creates new list with all the values stored as integers
    sums the temperature(last 12 values of each list)
    removes the individuals temperatures from each list leaving the year
    averages temps and rounds them to 0 decimal places.
    convert rounded averages to integers
    append the rounded averages to the lists with just the year
    returns this list.           
    '''
    try:
        lst_select2 = []
        
        #creats new list with the values stored as integers
        for i in lst_select:
            lst = [int(a) for a in i]
            lst_select2.append(lst)
       
        lst_select3 = []   
        for i in lst_select2:
            temps = i[1:]        #Gets all the temps
            i = i[0:1]    #Removes all temps from list leaving behind the year 
            average = int(round(sum(temps)/12,0)) 
            i.append(average)
            lst_select3.append(i)      
           
              
        return(lst_select3)
    except TypeError:
        pass
    
def output_data(lst_select3,output_file):
    '''
    takes takes processed data and output file as arguments
    formats data appropialtely
    writes formatted data to output file
    returns output file
    closes output file
    '''
    try:
        for i in lst_select3:
            #Formats the output
            x = "{:4}{:1}{:4}".format(str(i[0]),"",str(i[1]))+"\n" 
            output_file.write(x) #Writes output to file
    except TypeError:
        pass

    output_file.close()
    
              
def main():
    '''
    creates file object for input file
    if input file can't be opened
        end program
    prompts user for output file name
    creates file object for output file
    
    calls get_data on input file
    calls process_data
    calls output_data    
    '''
    try:
        input_file = open("data_full.txt","r")
    except FileNotFoundError:
        print("Input file not found. Ending program")
        return        
    file_name = input("Enter output file name: ")
    output_file = open(file_name,"w")
    
    data = get_data(input_file)
    data_processed = process_data(data)
    output_data(data_processed,output_file)
    
    
main()