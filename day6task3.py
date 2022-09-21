# 3. Reversed words
# The user enters a sentence.
# We output all the words of the sentence in a reverse form. 
# - not the whole text reversed!!
# Example
# Alus kauss mans -> Sula ssuak snam
# notice how each word was reversed separately
# PS Split and join operations could be useful here.

user_input = input("Please enter a sentence: ")
word_list = user_input.lower().split()

reverse_list = []
for word in word_list:
    reverse_list.append(word[::-1])
reverse_list[0] = reverse_list[0].capitalize()
reverse_sentence = ' '.join(reverse_list)
print(reverse_sentence)

# solved checking against example..
# review list comprehension option below - would be instead of lines 14,15
# basically above 'one by one do what' and below 'do what one by one"
# reverse_list = [word[::-1] for word in word_list]
