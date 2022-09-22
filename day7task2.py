# 2. Palindrome
# Write the function is_palindrome(text)
# which returns a bool True or False depending on whether the word or sentence is read equally from both sides.
# PS You can start with a one-word solution from the beginning, but the full solution will ignore whitespace and uppercase and lowercase letters.
# is_palindrome ("Alus ari i ra    sula") -> True
# is_palindrome("ABa") -> True
# is_palindrome("nava") -> False

def is_palindrome(text):
    # text_list = text.split("")
    n = 0
    m = 0
    for i in range(0, len(text)):
        if text[0 + n] == text [-1 + m]:
            result = True
            n += 1
            m -= 1
        else:
            result = False
            break
    return result
word = input("Please enter a word: ")
print(is_palindrome(word))
