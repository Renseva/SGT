# 1a. Average value

# Write a program that prompts the user to enter numbers (float).
# The program shows the average value of all entered numbers after each entry.
# PS. 1a can do without a list
# 1b. The program shows both the average value of the numbers and ALL the numbers entered
# PS Exit the program  by entering "q"

# 1c The program does not show all the numbers entered but only TOP3 and BOTTOM3 and of course still average.
# will try 1b

num_list = []
user_input = 0
while a != "q":
    user_input = input("Please enter a number, including decimals, or 'q' to quit: ")
    if user_input != "q":
        num_list.append(float(user_input))
        sumsum = sum(num_list)
        div = len(num_list)
        aver = round(sumsum / div, 2)
        print(f"Average of {num_list} is {aver}")
