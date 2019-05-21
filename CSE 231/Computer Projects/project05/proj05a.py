#############################################################################
#   Computer project 5a
#	Algorithim
#		try opening source file
#		if file does not exist, end program
#		
#		prompt for output file name
#		create output file
#		prompt for year
#		
#		find appropriate listings in source file
#		output them to the output file
#		close output file
#		close source file
#
#############################################################################







file_exists = 0

try:
	polio = open("polio.txt","r")
	file_exists = 1
except FileNotFoundError:		#If the file is not not found
	print("Source file does not exist. Ending program.")

#Runs only if file exists
while file_exists == 1:
	output_file_name = input("Enter a file name to output to: ")
	output_file = open(output_file_name,"w")

	year = input("Enter a year: ")

	for line in polio:
		if year == "" or year == "all" or year == "ALL":
			output_file.write(line)


		elif year == line[68] or year == line[68:69] or year == line[68:70] or\
		 year == line[68:71] or year == line[68:72]:
			output_file.write(line)
	output_file.close()
	polio.close()
	file_exists = False

