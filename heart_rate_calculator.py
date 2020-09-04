# Calculation program allows users to be intentional in
# their workouts by their tracking heart rate.

#Get user input telling age
user_age = input('How old are you? ')

maximum_heart_rate = 220 - int(user_age)

#Calculate maximum and minimum heart rate for each zone.

red_zone_minimum = .91 * maximum_heart_rate
red_zone_maximum = 1.0 * maximum_heart_rate

orange_zone_minimum = .81 * maximum_heart_rate
orange_zone_maximum = .90 * maximum_heart_rate

green_zone_minimum = .71 * maximum_heart_rate
green_zone_maximum = .80 * maximum_heart_rate

blue_zone_minimum = .61 * maximum_heart_rate
blue_zone_maximum = .70 * maximum_heart_rate

grey_zone_minimum = .51 * maximum_heart_rate
grey_zone_maximum = .60 * maximum_heart_rate

#print(f'To be in the orange zone keep your heart rate between {orange_zone_minimum} and {orange_zone_maximum}.')

# Use if, elif and else statement to get desired heart rate range.

#both hard-coded user color and as a variable 
user_color  = str (input("What color zone do you want to work out at today? The ranges go from red being very difficult to grey being very light. Please choose red, orange, green, blue or grey? "))

if user_color=="red":
  print(f" For the red workout maintain your heart rate between {red_zone_minimum} and {red_zone_maximum}. You got this! Enjoy your workout!") 
elif user_color=="orange":
  print(f" For the orange workout maintain your heart rate between {orange_zone_minimum} and {orange_zone_maximum}. You got this! Enjoy your workout!") 
elif user_color=="green":
  print(f" For the {user_color} workout maintain your heart rate between {green_zone_minimum} and {green_zone_maximum}. You got this! Enjoy your workout!") 
elif user_color=="blue":
  print(f" For the {user_color} workout maintain your heart rate between {blue_zone_minimum} and {blue_zone_maximum}. You got this! Enjoy your workout!") 
else:
    print(f" For the {user_color} workout maintain your heart rate between {grey_zone_minimum} and {grey_zone_maximum}. You got this! Enjoy your workout!") 
