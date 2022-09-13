#  2. Christmas tree 

# Ask user to enter the height of the tree 
# Then Print the tree: Ex. height == 3 
# The printout would be: 
#   * 
#  *** 
# ***** 
# Note: remember that several symbols can be printed at once, for example: print ("" * 10 + "*" * 6)

height = int(input("Please enter the height of the tree (whole number): "))
row_length= (height * 2) - 1
for i in range(1, height + 1):
    stars = i + i - 1
    gap = int((row_length - stars) / 2)
    print(" " * gap + "*" * stars + " " * gap)