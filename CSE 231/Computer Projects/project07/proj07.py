#############################################################################
#   Computer project 7
#       Algorithim
#           Calls function to get list of lists containing inflation data
#
#           Convert year in inflation data to int and inflation to float
#
#           Calls function to get lists of lists containing hearing data
#
#           Adjusts hearing data for inflation using inflation data
#
#           Creates lists containing name, adjusted cost and year for each entry
#           in hearings
#
#           Create list of lists containing properly grouped name, adjusted
#           cost and year data for each entry in hearings
#
#           Call function to graph data using individual lists of name and 
#           adjusted cost
#
#           Call function to write properly formatted and adjusted data to 
#           output file
#############################################################################

import pylab
def draw_bar_graph(x,y):
    '''Draw a bar graph of y values with labels from x where
       x is a list of strings; y is a list of values associated with each x'''
    number_of_bars = len(x)
    bar_width = 0.5
    #create a list (array) of indices for bars
    x_values = pylab.linspace(0,number_of_bars-1,number_of_bars)
    #associate a string label (tick) from x with each bar
    #orient the string to the middle of the bar, and rotate the label 45 degrees
    pylab.xticks(x_values+bar_width/2, x, rotation=45)
    
    #Title for the graph and labels for the axes
    pylab.title( "Inflation-adjusted Cost for Hearings" )
    pylab.ylabel( "Cost (in millions of 2015 dollars)" )
    
    pylab.bar(x_values,y,width=bar_width)
    pylab.show()




def get_cols_from_file (file_name,cols,header):
    '''
    Creates a list containing lists for each line for the specified values.
    file_name is the file name; cols is a list that contains the indeces of the 
    columns needed; header is an integer that indicated how many heaer lines to
    skip
    '''
    file = open(file_name,"r")
    #creates a list containing lists that each contain each value in the file
    file_lst = [line.split() for line in file]
    
    #lol = list of lists
    lol = []
    
    #Skips over header lines and adds list of the appropriate to lol
    for line in file_lst:
        if file_lst.index(line) >= header: 
            lst = []
            for index in cols:
                lst.append(line[index]) 
            lol.append(lst)
        
    file.close()
    return lol
    

def convert(lst):
    '''
    Lst is a list that contains lists each contianing two values.
    converts first value to an integer
    converts second value to a float
    '''
    lst_num = []

    for first,second in lst:
        lst_num.append([int(first),float(second)])
    return lst_num


    

def find_index(year,lst):
    '''
    Finds the index of the line in the list of lists that contains the year
    year is an integer value; lst is a list.
    '''
    for item in lst:
        if item[0] == int(year):    #checks if years match
            return lst.index(item) 

def adjust_for_inflation(amount,year,lst):
    '''
    Adjusts the dollar ammount for inflation calculated from the year 
    corresponding to the dollar amount to the year 2014;
    the first parameter is a float and is the orginal dollar amount;
    the second parament is an integer and is the year corresponding to the
    dolar amount;
    the third parameter is a list and contains lists that contain the inflation
    values and their corresponding year;
    
    '''
   
    year_index = find_index(year,lst)
    for item in lst[year_index+1:]:
        amount += amount * item[1]/100
    
    return round(amount,1)
           
def write_file(lst):
    #Opens output file
    hearing_file_adjusted = open("hearing_adjusted.txt","w")
    #Writes header lines to output file
    hearing_file_adjusted.write("         Congressional Hearing Cost \n")
    hearing_file_adjusted.write("{:13}{:24}{:4}".format("Name",\
    "Cost ($Million)","Year\n"))
    
    #Writes name, cost, and year to each line on file
    for item in lst:
        hearing_file_adjusted.write("{:12}{:>4}{:>25}{}".format(item[0],\
        str(item[1]), item[2],"\n"))
    '''for item in lst:
        hearing_file_adjusted.write(str(item[1]))
        hearing_file_adjusted.write("\n")'''
    
def main():   
    '''
    gets inflation and hearing data
    creates lists containing adjusted year, cost and name data
    creates one list that with lists that each contain the adjusted year,cost 
    and name data for each line. 
    
    writes adjusted data to output file
    draws graph with adjusted data
    ''' 
    #Gets the inflation values
    try:
        inflation_lst = get_cols_from_file("inflation.txt",[0,-1],1)
    except FileNotFoundError:
        print("File not found. Quitting")
        return
    try:
        inflation_lst_num  = convert(inflation_lst)
    except ValueError:
        print("Invalid data. Quitting")
        return

    #Gets orginal hearing data
    try:
        hearing_lst = get_cols_from_file("hearings.txt",[0,1,-1],2)
    except FileNotFoundError:
        print("File not found. Quitting")
        return
        
    hearing_adjusted = []
    name = []
    year = []
    
    #Creates lists containing adjusted year data, cost data and name data
    for item in hearing_lst:
        try:
            adjusted_val = adjust_for_inflation(float(item[1]),int(item[2]),\
            inflation_lst_num)
            hearing_adjusted.append(adjusted_val)
        except ValueError:
            print("Invalid data. Quitting")
            return
        
        name.append(item[0])
        year.append(item[2])
    
    hearing_adjusted_lol = []
    
    count = 0
    #Creates 1 list that contains lists with name,cost and year for each line
    while count < len(name):
        hearing_adjusted_lol.append([name[count],hearing_adjusted[count],\
        year[count]])
        count+= 1
    #Writes data to output file
    write_file(hearing_adjusted_lol)
    
    #Draws bar graph of name(x-axis) and cost(y-axis)
    draw_bar_graph(name,hearing_adjusted)
    

main()
    

    
    
    
















