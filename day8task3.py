
# # 3. Dictionary cleaner
# 3a. Write clean_dict_value(d, bad_val), which returns a cleaned dictionary without any keys with the value bad_val
# The parameters of the function are the dictionary d to be processed and the value bad_val to be disposed of together with its key.
# Example:
# clean_dict_value ({'a': 5, 'b': 6, 'c': 5}, 5) -> {'b': 6}, because 5 was a value for both a and c keys to get rid of.

# PS. Remember we can use del d['a'] only if the key 'a' exists.
# !! When resizing a dictionary, we are not allowed to iterate at the same time!
# There are two options: either walk through the copy my_dict.copy.items(), or build a new dictionary. 
# Dictionary comprehension would be one option.

# def clean_dict_value(d, bad_val):
#     new_dict = {}
#     for key, value in d.items():
#         if value != bad_val:
#             new_dict[key] = value
#     return new_dict

# print(clean_dict_value({'a': 5, 'b': 6, 'c': 5}, 5)) 

# 3b Write clean_dict_values ​​(d, v_list), which returns a cleaned dictionary
# The parameters of the function are the dictionary d to be processed and the list of values ​​v_list to get rid of.
# clean_dict_values ​​({'a': 5, 'b': 6, 'c': 5, 'd':3}, [3,4,5]) -> {'b': 6} because 3 and 5 were in the list of values to delete.
# Naudoti .copy, turbut for loop blogu verciu sarasui bet suziureti kurioj vietoj tkkrinti ar key dar neistrintas

def clean_dict_values(d, v_list):
    for key, value in d.copy().items():
        for i in range(len(v_list)):
            # print(v_list[i])
            if v_list[i] == value:
                if key in d.items() == True:
                    del(d[key])
                    break
    return d

print(clean_dict_values({'a': 5, 'b': 6, 'c': 5, 'd':3}, [3,4,5]))

