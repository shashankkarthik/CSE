#############################################################################
#  Computer Project #1
#
#  Algorithm
#    promt for total distance and tortoise's speed
#
#    calculate time taken by tortoise
#      convert speed to miles/hour
#      divide total distance by speed
#      print time taken by tortoise
#
#    promt for details about hare's racing
#
#    calculate time taken by hare    
#      calculate distance run between rests
#      calculate number of rests througout the race
#      calculate total time spent resting
#      calculate total time running
#      sum time spent running and resting to get total time 
#      print time taken by hare  
#
#############################################################################
import math

#Prompts user for distance of the the race and the speed of the tortoise.

total_distance = float(input("How many miles will the tortoise and the hare \
race? "))
tortoise_speed = float(input("How many inches can the tortoise cover in one \
minute? "))

#Calculates and prints the time taken for the tortoise to complete the race.

tortoise_speed_mph = tortoise_speed / 63360 * 60 
    
total_time_tortoise = total_distance / tortoise_speed_mph    

print("The tortoise takes",total_time_tortoise,"hours to finish the race.")

#Prompts user for details about the hare's racing method.

hare_speed = float(input("How many miles can the hare run in one hour? "))
rest_duration = float(input("How long does the hare rest (in min)? "))
run_duration = float(input("How long does the hare run at a time (in min)? "))

#Calculates and prints the time taken for the hare to complete the race

run_distance = (run_duration/60)*hare_speed     
number_rests = math.ceil(total_distance/run_distance) - 1        
time_resting = number_rests * (rest_duration/60)   
time_running = total_distance/hare_speed   

total_time_hare = time_resting + time_running

print("The hare takes", total_time_hare, "hours to finish the race.")


