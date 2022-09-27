# 2. Common Elements
# Write a function that returns a tuple with common elements in three sequences. Inputs can be list, tuple, string.
# get_common_elements(seq1, seq2, seq3)
# Example:
# get_common_elements("abc", ['a', 'b'], ('b', 'c')) -> ('b',) # we return a tuple with a single element 
# # remember that we can convert strings to set with set(mystring), and set to tuple with tuple(myset)

# 2. b For those with some experience 
# BONUS:  make a function that can handle an arbitrary number of input sequences
# so function which takes any number of sequences and returns a tuple with common elements
# get_common_elements(seq1, seq2, seq3, seq4, seq5, seq6, seq7) etc :), so just like print takes any number of values

def get_common_elements(seq1, seq2, seq3):
    set1 = set(seq1)
    set2 = set(seq2)
    set3 = set(seq3)
    common12 = set(set1.intersection(set2))
    common123 = common12.intersection(set3)
    if len(common123) > 0:
        return tuple(common123)
    else:
        print("No common elements..")

print(get_common_elements("abc", ['a', 'b'], ('b', 'c')))

# print(get_common_elements("abc", ['m', 'n'], ('h', 'c')))
# not sure how to not have 'None' at the end