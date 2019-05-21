def getoption():
    option = input("")
    option_up = option.upper()
    if option_up[0] == "F":
       option_lst = option_up.split(" ")
       return option_lst

x = getoption()
print(x)