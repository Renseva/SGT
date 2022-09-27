# 3. Is there a pangram?
# Write a function is_pangram(text, alphabet='abcdefghijklmnopqrstuvwxyz')
# that returns True when the text parameter contains all the letters passed in an alphabet.
# We return False otherwise
# pangram - sentence, word string containing all letters of the alphabet - https://en.wikipedia.org/wiki/Pangram
# We ignore spaces and believe that uppercase is as valid as lowercase, i. here A and a -> a
# print(is_pangram("The five boxing wizards jump quickly")) -> True
# print(is_pangram("Not a pangram")) -> False

def is_pangram(text, alphabet='abcdefghijklmnopqrstuvwxyz'):
    text_set = set(text.lower())
    abc_set = set(alphabet)
    return abc_set.intersection(text_set) == abc_set

print(is_pangram("The five boxing wizards jump quickly", alphabet='abcdefghijklmnopqrstuvwxyz'))
print(is_pangram("Not a pangram", alphabet='abcdefghijklmnopqrstuvwxyz'))

# Will search for Lithuanian pangrams over weekend :)
# Bonus: test it also on Lithuanian alphabet:
# a_lt = 'aąbcčdeęėfghiįyjklmnoprsštuųūvzž' # see if this correct
# some languages have perfect pangrams, some do not
# perfect pangram - a pangram that uses every letter of the alphabet at just once