# Write a program that asks for and saves a username
# Ask a question about the user's age, using the username in the question.
# Shows in how many years the user will be 100 years old smile
# BONUS: Let the program also show the year when the user will be 100 years old.
# It could use a variable with the current year.
# It would be even better to get the current year automatically
# then you will need two additional lines:
# import datetime # let's talk about imports separately
# currentYear = datetime.datetime.now (). year

import datetime
current_year = datetime.datetime.now().year
username = input("Enter username:")
user_age = input(f"Hi {username}, please confirm your age:")
user_age = int(user_age)
user_hundred = current_year+100-user_age
print(user_hundred)
print(f"You will reach 100 years in year {user_hundred} \U0001F600")
