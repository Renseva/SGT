#1. The Big Result
# Write an add_mult function that requires three parameters / arguments
# Returns the result that is the sum of the 2 smallest arguments multiplied by the largest argument value.
# PS Assume that numeric parameters will always be passed to the function, no need to check types
# Various solutions are possible (you are allowed to use other data structures inside function such as list).
# Example add_mult (2,5,4) -> will return (2 + 4) * 5 = 30
# PSS function should return the result, not print it.

# tried but failed to avoid global variables and doesn't work when 2 same numbers

# user_entry = input("Please enter 3 integers: ")
# num_list = user_entry.split()

a = int(input("Please enter first integer: "))
b = int(input("Please enter second integer: "))
c = int(input("Please enter third integer: "))
def add_mult(a, b, c):
    arg_list = [a, b, c]
    largest = max(arg_list)
    smallest = min(arg_list)
    smaller = 0
    for i in arg_list:
        if i != largest and i != smallest:
            smaller = i
    return (smallest + smaller) * largest

result = add_mult(a, b, c)
# print(add_mult(a, b, c))



