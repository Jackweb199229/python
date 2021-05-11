# first section
day =0
squats=0
total=0
print("Enter the number of squats you did on each day for the last one week:")
#second section
#while loop
while (day<= 6):
	day=day+1
	squats = int(input("enter squats on a day {} : ".format(day)))
	total=total+squats
# third section outer the loop and print
avg=total/day
print("In the last {} day , you did on average of {} squats ! ".format(day,avg))


	