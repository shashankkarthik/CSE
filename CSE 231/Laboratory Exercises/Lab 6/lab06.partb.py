file_name = input("Enter File Name:" )

output_file = open( file_name, "w")

user_output = input()

while user_output != ".":
    print(user_output,file=output_file)
    user_output = input()

output_file.close()