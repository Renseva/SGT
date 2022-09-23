# 2. Palindrome
# Write the function is_palindrome(text)
# which returns a bool True or False depending on whether the word or sentence is read equally from both sides.
# PS You can start with a one-word solution from the beginning, but the full solution will ignore whitespace and uppercase and lowercase letters.
# is_palindrome ("Alus ari i ra    sula") -> True
# is_palindrome("ABa") -> True
# is_palindrome("nava") -> False

def is_palindrome(text):
    phrase = text.lower().replace(" ", "*")
    return phrase == phrase[::-1]

some_text = input("Please enter some text: ")
print(is_palindrome(some_text))

# initially I used .split method to make a list from sentence however not checked for one word which in case of one word makes a list
# with that word as the single list element

# below worked for word, was told it's more lower level solution, makes sense given the above.....
#  def is_palindrome(text):
#     # text_list = text.split("")
#     n = 0
#     m = 0
#     for i in range(0, len(text)):
#         if text[0 + n] == text [-1 + m]:
#             result = True
#             n += 1
#             m -= 1
#         else:
#             result = False
#             break
#     return result