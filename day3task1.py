# 1. Health check

# Ask user for their temperature.
x = float(input("What's your temperature in Celsius? "))

# If the user enters below 35, then output "not too cold"
if x < 35:
    print("not too cold \n")

# If 35 to 37 (inclusive), output "all right"
elif x > 37:
    print("possible fever \n")

# If the temperature  over 37, then output  "possible fever
else:
    print("all right \n")
# remember about type conversion if needed