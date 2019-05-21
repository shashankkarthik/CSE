#############################################################################
#	Computer project 6a
#	
#	Algorithm
#		try
#			prompt user for file name
#			open file object
#			initialize count variable
#			intialize lists for years and temps
#			iterate through each line in file
#				increase count by 1
#				append the first 4 chars. in each line to years list
#				append the last 4 chars. in each line to temp list
#			if count > 0
#				call function to draw graph
#			else
#				display empty file message. 
#		except FileNotFoundError
#			print error message
#			end program
#############################################################################

import pylab

def draw_graph( x, y ):
    '''Plot x vs. y (lists of numbers of same length)'''

    # Title for the graph and labels for the axes
    pylab.title( "Change in Global Mean Temperature" )
    pylab.xlabel( "Year" )
    pylab.ylabel( "Temperature Deviation" )

    # Create and display the plot
    pylab.plot( x, y )
    pylab.show()

try:
	file_name = input("Enter File Name: ")
	data_file = open(file_name,"r")

	count_lines = 0		#Counts how many lines are in the input file.

	year = []
	temp = []


	for line in data_file:
		count_lines += 1
		year.append(int(line[:4]))	#Gets the first 4 charecters from each line
		temp.append(int(line[-4:])) #Gets the last 4 charecters from each line
	if count_lines > 0:
		draw_graph(year,temp)
	else:
		print("The file is empty.")
		print("Ending program.")
except FileNotFoundError:
	print("Unable to open file.")
	print("Ending program.")