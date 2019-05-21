#############################################################################
#   Computer Project 8
#       Algorith
#           Displays menu
#           Initialized empty contact dicionary
#           Prompts user for choice (A-G, X)
#           While user's choice is not X
#               Print which option was chosen
#               Call function for appropriate choice.
#           If user's choice is X
#               End program
#############################################################################

MENU = '''
A) Read collection of contacts from file
B) Write collection of contacts to file
C) Add new contact
D) Remove existing contact
E) Update existing contact's phone number
F) Update existing contacts's email address
G) Display contacts by prefix
X) Exit from the program \n'''

def validate_number(num):
    '''
    Checks to see if the hyphens are in the correct places
    Checks to see if there are enough charecters and if they are digits.
    '''
    try:
        true_count = 0
        if num[3] == "-" and num[7] == "-":
            true_count += 1
        for i in num:
            if i != "-":
                if i.isdigit():
                    true_count += 1
        if true_count == 11:
            return True
        else:
            return False
    except IndexError:
        return False

def validate_email(email):
    '''
    Checks to see if the the email is in the correct format and has a @ symbol
    '''
    if len(email.split("@")) == 2:
        if "." in email.split("@")[1]:
            return True
        else:
            return False
    else:
        return False    

        
def option_a():
    '''
    Function takes no input
    Initialized empty dictionary
    Request user for file name and opens file
    Iterates through file and creates list with contact name, number and email
    Creates dictionary entry with the key being the name and value a list
    containing just the phone number and email address.
    Returns dictionary
    '''
    contacts_dict= {}
    input_file = open(input("Enter input file name: "),"r")
    for line in input_file:
        line = line.strip("\n")
        contacts_list = line.split(";")
        contacts_name = contacts_list[0]
        contacts_list.pop(0)
        contacts_dict[contacts_name] = contacts_list
    input_file.close()
    return(contacts_dict)

def option_b(contacts_dict):
	'''
	Function takes dictionary of contacts as input
	Requests user for file name and opens file
	Creates properly formatted string containing name, number and email for each 
	contact.
	Writes each string to file
	Closes file.
	'''
	output_file = open(input("Enter output file name: "),"w")
	for contact in contacts_dict:
		number = contacts_dict[contact][0]
		email = contacts_dict[contact][1]
		line = "{}{}{}{}{}{}".format(contact,";",number,";",email,"\n")
		output_file.write(line)
	output_file.close()

def option_c(contacts_dict):
    '''
    Function takes dictionary of contacts as input
    Prompts user for name of new contacts_dict
    Checks if contact already exists
    If not, prompts and validates number and email
    If both are valid, adds contact to dictionary
    Returns dictionary
    '''
    new_name = input("Enter new contact's name: ")
    if new_name not in contacts_dict:
        new_number = input("Enter new contact's number: ")
        if validate_number(new_number):
            new_email = input("Enter new contact's email: ")
            if validate_email(new_email):
                contacts_dict[new_name] = [new_number,new_email]
                return contacts_dict
            else:
                print("Invalid email")
        else:
            print("Invalid number")
    else:
        print("That person is already in your contacts")

def option_d(contacts_dict):
    '''
    Function takes dictionary of contacts as input
    Prompts user for name of contact to remove
    Checks if contact exists
    If so, deletes contact.
    Returns dictionary
    '''
    contact_name = input("Enter name of contact to remove: ")
    if contact_name in contacts_dict:
        del(contacts_dict[contact_name])
        return contacts_dict
    else:
        print("That contact does not exist")

def option_e(contacts_dict):
    '''
    Function takes dictionary of contacts as input
    Prompts user for name of contact
    Checks if contact is in dictionary of contacts
    Prompts user for new phone number
    Validates phone number
    Replaces phone number of contact
    Returns dictionary
    '''
    contact_name = input("Enter name of contact: ")
    if contact_name in contacts_dict:
        new_number = input("Enter the new phone number: ")
        if validate_number(new_number):
            contacts_dict[contact_name][0] = new_number
            return contacts_dict
        else:
            print("Invalid phone number")
    else:
        print("That contact does not exist.") 

def option_f(contacts_dict):
    '''
    Function takes dictionary of contacts as input
    Prompts user for contact name
    Checks if contact exists in dictionary of contacts
    Prompts user for new email address
    Validates email address
    Replaces email address
    Returns dictionary
    '''
    contact_name = input("Enter name of contact: ")
    if contact_name in contacts_dict:
        new_email = input("Enter the new email address: ")
        if validate_email(new_email):
            contacts_dict[contact_name][1] = new_email
            return contacts_dict
        else:
            print("Invalid email")
    else:
        print("That contact does not exist")

def option_g(contacts_dict):
    prefix = input("Enter name prefix: ")
    contacts_list = []
    for contact in contacts_dict:
        if prefix in contact:
            contacts_list.append(contact)
    if len(contacts_list) >0:
        contacts_list.sort()
        print(contacts_list)
    else:
        print("No contacts found.")
 

def main():
    print(MENU)
    contacts_dict = {}
    choice = input("Choice: ").upper()
    while choice != "X":
        if choice == "A":
           print("Selected A")
           contacts_dict = option_a()
        if choice == "B":
            print("Selected B")
            option_b(contacts_dict)
        if choice == "C":
            print("Selected C")
            option_c(contacts_dict)
        if choice == "D":
            print("Selected D")
            option_d(contacts_dict)
        if choice == "E":
            print("Selected E")
            option_e(contacts_dict)
        if choice == "F":
            print("Selected F")
            option_f(contacts_dict)
        if choice == "G":
            print("Selected G")
            option_g(contacts_dict)
        print(MENU)
        choice = input("Choice: ").upper()
main()

