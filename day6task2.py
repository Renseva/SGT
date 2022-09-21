# # 2. Cubes
# The user enters the beginning (integer) and end number.
# The output is the entered numbers and their cubes
# For example: inputs 2 and 5 (two inputs)
# Output
# 2 cubed: 8
# 3 cubed: 27
# 4 cubed: 64
# 5 cubed: 125
# All cubes: [8,27,64,125]
# PS could theoretically do without a list, but with a list it will be more convenient
num1 = int(input("Please enter the first whole number: "))
num2 = int(input("Please enter the second whole number: "))
num_list = list(range(num1, num2 + 1))
cubed = []
for num in num_list:
    cubed_el = num**3
    cubed.append(cubed_el)
    print(f"{num} cubed is {cubed_el}.")
print(f"All cubes: {cubed}")

# solved checking against example..






# for i in num_list:
#     print(i, end = " ")
