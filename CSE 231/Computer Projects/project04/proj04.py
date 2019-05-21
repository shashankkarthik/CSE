#############################################################################
#   Computer project 4
#
#   Algorithm
#       Prompt user for string to decompress.
#       Find indeces of the left & right parenthesis and the comma.
#       Check to see if string is empty or doesn't contain compressions.
#           If yes, terminate program.
#       While there are still left parenthesis remaining in the string.
#           Find the first & second numbers.
#           Splice the original string.
#           Reconstruct the original string with the spliced string.
#           Request the new indeces of the next parenthesis and comma.
#       Parse through decompressed string to find the backslashes.
#           Replace backslashes with line breaks.
#       Print final result.
#############################################################################



BACKSLASH = "\\"

string = input("Enter a string to decompress (or return to quit): ")

#Finds the indeces of the left & right parenthesis and the comma
index_left = string.find("(")
index_comma = string.find(",",index_left)
index_right = string.find(")",index_comma)

#Exits program if input doesn't contain a compression or if the input was empty 
if index_left == -1:
    print("Nothing to decompress. Exiting Program.")    


#Runs as long as there are left parenthesis remaining.
while index_left != -1:   
    
    first_num = int(string[index_left+1:index_comma])
    second_num = int(string[index_comma+1:index_right])
     
    #Finds the splice of the string based on the compression parameters
    splice_start = index_left-first_num
    splice_end = splice_start+second_num    
    string_splice = string[splice_start:splice_end]
  
    #Replaces the parenthesis and their contents with the spliced string.
    string = string[:index_left] + string_splice + string[index_right+1:]    
    
    #Requests for the next set of indeces.
    index_left = string.find("(")  
    index_comma = string.find(",",index_left)
    index_right = string.find(")",index_comma)

#Creates a line break where ever there is a backslash
for i in string:
    if i == BACKSLASH:
        string = string.replace(i,"\n")
        
        

print("The decompressed string prints as: \n")
print(string)