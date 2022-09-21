# Find and output the first 20 
# (even better option to choose how many first primes we want) 
# prime numbers in the form of a list i.e. [2,3,5,7,11, ...
# so remember we already know how to find a single prime number 
# from previous exercise
# https://github.com/ValRCS/Python_SheGoesTech_22/blob/main/Day_4_Loops/day4_exercise_3.py

num_list = [2]
primnum_list = []
how_many = int(input("How many prime numbers do you want listed? "))
while len(primnum_list) < how_many:
    for i in range(2, int(num_list[-1]**0.5) + 1):
        if num_list[-1] % i == 0:
            break
    else:
        primnum_list.append(num_list[-1])
    num_list.append(num_list[-1] + 1)
print(primnum_list)

# review the logic behind square root method
