# Sandeep Sadarangani 3/12/18
# Testing the modulus operator- %
# Modulus gives us the remainder of the division of two operands

minutes_in_hour = 60

movie_time = 105


hours_component = movie_time//minutes_in_hour
minutes_component = movie_time % minutes_in_hour

print("The movie is " + str(hours_component) + " hours and " + str(minutes_component) + " minutes." )

