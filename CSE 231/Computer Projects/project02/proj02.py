#############################################################################
#  Computer Project #2
#
#  Algorithm
#   request mean, std. deviations and num
#      
#   run the following loop num times:
#       run the gauss function witht given mean and std dev.  
#       if the current dist is less than the current min value:
#           the new min value is the current dist
#       if the current dist is greater than the current max value:
#           the new max value is the current dist
#       if the dist is greater than mean by more than 2 std. deviations:
#           do apropriate calculations
#       if the dist is greater than mean and within 2 std. deviations:
#           do apropriate calculations
#       if the dist is greater than mean and within 1 std. deviation:
#           do apropriate calculations
#       if the dist is equal to the mean:
#           do apropriate calculations
#       if the dist is less than the mean and within 1 std. deviation:
#           do apropriate calculations
#       if the dist is less than the mean and within 2 std. deviation:
#           do apropriate calculations
#       if the dist is less than the mean less than 2 std. deviations:
#           do apropriate calculations
#   print appropriately formatted values
###############################################################################


import random
random.seed(0)

print("This program analyzes Python's Guassian distribution algorithim.")
print("")


mean = float(input("Enter the desired mean: "))
std_dev = float(input("Enter the desired standard deviation: " ))
num = int(input("Enter the number of values to generate: "))
print("")

print("The requested mean: ", mean)
print("The requested standard deviation: ", std_dev)
print("The number of values generated: ", num)
print("")

total = 0
min = 10**6
max = 0


#The following 7 variables are counts

high_2std_dev = 0     #Vaulues higher than mean by more than 2 std. deviations
high_1std_dev = 0     #Values higher than mean and within 2 std. deviations
high_mean = 0         #Values higher than mean and within 1 std. deviation
at_mean = 0           #At mean
low_mean =  0         #Values lower than mean and within 1 std. deviation
low_1std_dev = 0      #Values lower than mean and within 2 std. deviations
low_2std_dev = 0      #Values lower than mean by more than 2 std. deviations





for val in range(num):
    dist = random.gauss(mean, std_dev)
    total += dist
    if dist < min:
        min = dist
    if dist > max:
        max = dist
        
    if dist > mean + (2 * std_dev):
        high_2std_dev += 1
    if dist > mean and dist <= mean + (2 * std_dev):
        high_1std_dev += 1
    if dist > mean and dist <= mean + std_dev:
        high_mean += 1
    
    if dist == mean:
        at_mean += 1
    
    if dist < mean and dist >= mean - std_dev:
        low_mean += 1
    if dist <  mean and dist >= mean - (2 * std_dev):
        low_1std_dev += 1
    if dist < mean - (2 * std_dev):
        low_2std_dev += 1
    
    
actual_mean = total/num

#Gets the percentages.
perc_high_2std_dev = (high_2std_dev / num) * 100
perc_high_1std_dev = (high_1std_dev / num) * 100
perc_high_mean = (high_mean / num) * 100

perc_at_mean = (at_mean / num) * 100

perc_low_mean = (low_mean / num) * 100
perc_low_1std_dev = (low_1std_dev / num) * 100
perc_low_2std_dev = (low_2std_dev / num) * 100


print("The values ranged from",round(min,2),"to",round(max,2))
print("The actual mean was",round(actual_mean, 2))
print("")

print("The values distributed as follows:")

print("  ",int(perc_high_2std_dev),"percent were higher than the mean by \
more than two standard deviations.")
print("  ",int(perc_high_1std_dev),"percent were higher than the mean and \
within two standard deviations.")
print("  ",int(perc_high_mean),"percent were higher than the mean and \
within one standard deviation.")

print("  ",int(perc_at_mean),"percent were at the mean")

print("  ",int(perc_low_mean),"percent were lower than the mean and \
within one standard deviation.")
print("  ",int(perc_low_1std_dev),"percent were lower than the mean and \
within two standard deviations.")
print("  ",int(perc_low_2std_dev),"percent were lower than the mean by \
more than two standard deviations.")

    
    
        
    
    
