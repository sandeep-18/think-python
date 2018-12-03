# Sandeep Sadarangani 3/12/18
# Use the time module (returns GMT) and convert it to time of day in hours, minutes, and seconds

import time

time_since_1970 = int(time.time())

number_of_seconds = time_since_1970
number_of_minutes = time_since_1970 / 60
number_of_hours = number_of_minutes / 60
days_since_epoch = number_of_hours / 24


current_time = days_since_epoch - int(days_since_epoch)

current_time_hours = current_time * 24
current_time_mins = (current_time_hours - int(current_time_hours))*60
current_time_secs = (current_time_mins - int(current_time_mins))*60


current_time_hours = int(current_time_hours)
current_time_mins = int(current_time_mins)
current_time_secs = int(current_time_secs)


print("Current Time: " + str(current_time_hours) + " hrs " + str(current_time_mins)+ " mins " + str(current_time_secs)+ " secs ")
print("Days since epoch = " + str(int(days_since_epoch)))


