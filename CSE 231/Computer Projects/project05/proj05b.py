#############################################################################
#   Computer project 5b
#	Algorithim
#		open_file(function)
#			prompts user for input file name
#			opens file
#			return file
#
#		process_file(function)
#			takes input file as arg.
#			processes file
#			prints results
#
#		call function open_file
#		call functionprocess_file
#############################################################################




def open_file():
	'''
	Prompts user for input file name
	Opens input file
	Returns: input file
	'''

	file_exists = 0

	while file_exists == 0:

		try:
			input_file_name = input("Enter input file name: ")
			input_file = open(input_file_name,"r")
			file_exists = 1
		except FileNotFoundError:		#If the file does not exist
			print("File does not exist.")
	return input_file



def process_file(input_file):
	'''
	Prompts user for year
	Prompts user for income number(1,2,3,4)
	Associates income number with proper World Bank income level code
	Initialize variables
		count: number of records that match requirments
		sum_percentages: sum of the sum_percentages
		lowest_percentage: the lowest percentage percentage value
		highest_percentage: the highest percentage value
		current_lowest: the current country with the lowest percentage
		current_highest: the curr country with the highest percentage
	For each line in the input_file
		if the year and the income level match the user inputs
			increase count by 1
			find the percentage from the last 3 characters from the line
			add percentage to sum_percentages
			finds lowest percentage
			finds highest percentage

	average_percentage: the average of all percentages
	print count
	print average_percentage
	print current_highest
	print current_lowest

	close input_file
	'''

	year = input("Enter a year:")
	income_number = input("Enter an income level (1,2,3,4): ")
	#Keeps prompting user for valid income level
	while income_number not in "1234":
		print("That is not a valid income level")
		income_number = input("Enter an income level (1,2,3,4): ")

	#Assigns input number to input level code
	if income_number == "1":
		income_level = "WB_LI "
	elif income_number == "2":
		income_level = "WB_LMI"
	elif income_number == "3":
		income_level = "WB_UMI"
	elif income_number == "4":
		income_level = "WB_HI "

	count_records = 0
	sum_percentages = 0
	lowest_percentage = 100
	highest_percentage = 0

	current_lowest = "-"
	current_highest = "-"


	for line in input_file:
		if line[68:72] == year and line[0:6] == income_level:
			count_records += 1
			percentage = int(line[-3:])
			sum_percentages += percentage
			if percentage <= lowest_percentage:
				lowest_percentage = percentage
				current_lowest = line
			if percentage >= highest_percentage:
				highest_percentage = percentage
				current_highest = line



#Replaces income code with income level and regiion code with region
	if current_lowest[0:6] == "WB_LI":
		current_lowest = current_lowest.replace("WB_LI","Low Income")
	elif current_lowest[0:6] == "WB_LMI":
		current_lowest = current_lowest.replace("WB_LMI","Lower middle income")
	elif current_lowest[0:6] == "WB_UMI":
		current_lowest = current_lowest.replace("WB_UMI","Upper middle income")
	elif current_lowest[0:6] == "WB_HI":
		current_lowest = current_lowest.replace("WB_HI","High income")

	if current_lowest[7:11] == "AFR":
		current_lowest = current_lowest.replace("AFR","Africa")
	elif current_lowest[7:11] == "AMR":
		current_lowest = current_lowest.replace("AMR","Americas")
	elif current_lowest[7:11] == "EMR":
		current_lowest = current_lowest.replace("EMR","Easter Mediteranian")
	elif current_lowest[7:11] == "EUR":
		current_lowest = current_lowest.replace("EUR","Europe")
	elif current_lowest[7:11] == "SEAR":
		current_lowest = current_lowest.replace("SEAR","South-East Asia")
	elif current_lowest[7:11] == "WPR":
		current_lowest = current_lowest.replace("WPR","Western Pacific")



	if current_highest[0:6] == "WB_LI":
		current_highest = current_highest.replace("WB_LI","Low Income")
	elif current_highest[0:6] == "WB_LMI":
		current_highest = current_highest.replace("WB_LMI","Lower middle income")
	elif current_highest[0:6] == "WB_UMI":
		current_highest = current_highest.replace("WB_UMI","Upper middle income")
	elif current_highest[0:6] == "WB_HI":
		current_highest = current_highest.replace("WB_HI","High income")

	if current_highest[7:11] == "AFR":
		current_highest = current_highest.replace("AFR","Africa")
	elif current_highest[7:11] == "AMR":
		current_highest = current_highest.replace("AMR","Americas")
	elif current_highest[7:11] == "EMR":
		current_highest = current_highest.replace("EMR","Easter Mediteranian")
	elif current_highest[7:11] == "EUR":
		current_highest = current_highest.replace("EUR","Europe")
	elif current_highest[7:11] == "SEAR":
		current_highest = current_highest.replace("SEAR","South-East Asia")
	elif current_highest[7:11] == "WPR":
		current_highest = current_highest.replace("WPR","Western Pacific")



	#Incase count = 0
	try:
		average_percentage = sum_percentages/count_records
		print(count_records)
		print("Average Percentage: ",average_percentage)
		print(current_highest)
		print(current_lowest)
	except ZeroDivisionError:
		print("There were no listings matching the requirments")
	input_file.close()


def main():
	'''
	calls open_file and open input_file
	'''
	process_file(open_file())

main()


