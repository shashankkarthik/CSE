file_name = input("Enter file name: ")

try:
    score_file = open(file_name,"r")
except FileNotFoundError:
    print("File name invalid")
    file_name = input("Enter file name: ")
    score_file = open(file_name,"r")


data = []
    
for line in score_file:

    line_lst = line.split()
    line_lst[0] = line_lst[0]+" "+line_lst[1]
    line_lst.pop(1)
    
    line_lst[1] = int(line_lst[1])
    line_lst[2] = int(line_lst[2])
    
       
    
    exam_average = (line_lst[1]+line_lst[2])/2

    line_lst.append(exam_average)
    
    line_lst = tuple(line_lst)
    data.append(line_lst)




data.sort()


total_exam1 = 0
total_exam2 = 0

for i in data:
    total_exam1+=i[1]
    total_exam2+=i[2]
    
    
    
exam_1_average = total_exam1/len(data)
exam_2_average = total_exam2/len(data)


for i in data:
    x = "{:20}{:5}{:5}{:7}".format(i[0],i[1],i[2],i[3])
    print(x)

print("")
print("Exam 1 Class Average: ",exam_1_average)
print("Exam 2 Class Average: ",exam_2_average)



score_file.close()

