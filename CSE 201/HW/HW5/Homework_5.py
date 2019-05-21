def convert_input(user_input):
	input_lst = [i for i in user_input.split("-")] #Splits input into a list based on location of hyphens
	input_split = [x for b in input_lst for x in b] #Splits split input into list containing individual digits

	if input_split[-1] == "X":	#Check if the last digit is 'X' 
		input_split[-1] = 10	#If it is, changes it to 10 (int)
	
	input_lst_int = [int(i) for i in input_split] #Converts each digit to int type
	
	return input_lst_int 

def sum(isbn_lst):
#Formula: check sum = 10*d1+9*d2+8*d3+....+1*d10
	check_sum = 0 
	mult = 10
	for i in isbn_lst:
		check_sum += mult*i
		mult -= 1
	return check_sum
	

def sum_check(check_sum):
	return check_sum % 11 == 0 #Checks if check_sum is a multiple of 11

def validate_key(key):
	input_lst = convert_input(key) #Converts input to list containing each digit in int type
	check_sum = sum(input_lst) #Calculates the sum according the formula
	valid_key = sum_check(check_sum) #Checks if key is valid
	if valid_key: #Print appropriate reply
		print("The number is valid")
	else:
		print("The number is not valid")

def main():
	user_input = str(input("Enter ten-character ISBN number: ")) #Gets user input
	validate_key(user_input) #Validates key

main()