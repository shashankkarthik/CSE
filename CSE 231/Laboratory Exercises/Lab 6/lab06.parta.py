
file_name = input("Enter name of file: ")
input_file = open( file_name, "r" )

for line in input_file:
    line = line.rstrip()
    print( line )

input_file.close()
