input_file = open("city_all.txt","r")

lst = []

for line in input_file:
    line = line.strip()
    if line.isdigit():
        lst.append(line)



count_1 = 0
count_2 = 0
count_3 = 0
count_4 = 0
count_5 = 0
count_6 = 0
count_7 = 0
count_8 = 0
count_9 = 0
    
for num in lst:
    if num[0] == "1":
    	count_1 += 1
    elif num[0] == "2":
    	count_2 += 1
    elif num[0] == "3":
    	count_3 += 1
    elif num[0] == "4":
    	count_4 += 1
    elif num[0] == "5":
    	count_5 += 1
    elif num[0] == "6":
    	count_6 += 1
    elif num[0] == "7":
    	count_7 += 1
    elif num[0] == "8":
    	count_8 += 1
    elif num[0] == "9":
    	count_9 += 1

percent_1 = round(100*count_1/len(lst),1)
percent_2 = round(100*count_2/len(lst),1)
percent_3 = round(100*count_3/len(lst),1)
percent_4 = round(100*count_4/len(lst),1)
percent_5 = round(100*count_5/len(lst),1)
percent_6 = round(100*count_6/len(lst),1)
percent_7 = round(100*count_7/len(lst),1)
percent_8 = round(100*count_8/len(lst),1)
percent_9 = round(100*count_9/len(lst),1)


print( "Digit Percent Benford" )
print( "{:>4}".format(1),": ","{:>5}{}".format(percent_1,"%"),"{:>7}".format("(30.1%)"))
print( "{:>4}".format(2),": ","{:>5}{}".format(percent_2,"%"),"{:>7}".format("(17.6%)"))
print( "{:>4}".format(3),": ","{:>5}".format(percent_3),"{:>7}".format("(12.5%)"))
print( "{:>4}".format(4),": ","{:>5}".format(percent_4),"{:>7}".format("(9.7%)"))
print( "{:>4}".format(5),": ","{:>5}".format(percent_5),"{:>7}".format("(7.9%)"))
print( "{:>4}".format(6),": ","{:>5}".format(percent_6),"{:>7}".format("(6.7%)"))
print( "{:>4}".format(7),": ","{:>5}".format(percent_7),"{:>7}".format("(5.8%)"))
print( "{:>4}".format(8),": ","{:>5}".format(percent_8),"{:>7}".format("(4.1%)"))
print( "{:>4}".format(1),": ","{:>5}".format(percent_9),"{:>7}".format("(4.6%)"))
 