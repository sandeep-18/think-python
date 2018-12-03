# Sandeep Sadarangani 3/12/18
# Ask the user to enter their speed and the zone speed and then calculate the speeding fine

def fine_calculation(curr_speed, speed_zone):
    speed_diff = curr_speed - speed_zone  # Calculate the difference of speeds
    
    fine = 0
    
    if speed_diff <= 0:  # Current speed less than speed zone
        fine = 0
    elif speed_diff <= 10: # Current speed less than 10 km/hr over
        fine = 119
    elif speed_diff <= 20: # Current speed less than 20 km/hr over
        fine = 275
    elif speed_diff <= 30: # Current speed less than 30 km/hr over
        fine = 472
    elif speed_diff <= 45: # Current speed less than 45 km/hr over
        fine = 903
    else:                  # Current speed greater than 45 km/hr over
        fine = 2435
        
    return fine
        


current_speed = input("What is your current speed: ")
current_speed = int(current_speed)

speed_zone = input("What is the speed zone: ")
speed_zone = int(speed_zone)

speeding_fine = fine_calculation(current_speed, speed_zone)

print("Your speeding fine is $" + str(speeding_fine))