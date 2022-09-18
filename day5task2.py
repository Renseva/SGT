# 2. Almost Hangman

# Write a program to recognize a text symbol
# The user (first player) enters the text.
# Only asterisks instead of letters are output.
# Assume that there are no numbers, but there may be spaces.
# The user (i.e. the other player) enters the symbol.
# If the letter is found, then the letter is displayed in ALL the appropriate places, all other letters remain asterisks.

# Example:
# First input: Kartupeļu lauks -> ********* *****
# Second input: a -> *a****** *a***
# In principle, this is a good start to the game of hangman.

# https://en.wikipedia.org/wiki/Hangman_(game)

# I got stuck with attempted solution at the bottom, and ran out of time to figure all out by myself
# and have noone to ask. I started learning coding with c and i find Python loops confusing probably as a result,
# so the following solution is after having a look at how others solved it :( i.e. copied over with own names :(, hopefully
# next week will be better :(

words=input("Enter a phrase (letters and spaces only) :")

space = " "
asterisk = "*"
answer = ""

for c in words:
    if c == space:
        answer += space  
    else: 
        answer += asterisk 

print(answer)

while asterisk in answer:
    user_try = input("Guess a letter:")
    for i, c in enumerate(words): 
        if c == user_try:
           answer = answer[:i] + user_try + answer[i+1:]
    print(answer)
print("you win, and I lose :(")


# initial attempt below, stuck on how to replace multiple letters and stop once all the letters are guessed correctly
# words = input("Enter a phrase (letters and spaces only) :")
# answer = '*' * len(words)
# print(answer)
# letter_count = 27

# for y in range(1, letter_count):
#     user_try = input('Guess a letter:')
#     if len(user_try) > 1:
#         user_try = user_try[0]
#     mould = user_try * len(words)

#     answer_list = list(answer)
#     for i, j in zip(words, mould):
#         if i == j:
#             indx = words.index(i)
#             answer_list[indx] = i # cia reikia rasti kaip replacinti b8ten tą
#             answer = "".join(answer_list)
#     print(answer)
   
#     if answer.count('*') == 0:
#         break