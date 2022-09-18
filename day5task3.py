# 3. Text conversion

# Write a program for text conversion
# Save user input
# Print the entered text without changes
# Exception: if the words in the input are not .... bad, 
# then the output is not ...  bad section must be changed to is good

# Examples:
# The weather is not bad -> The weather is good
# The car is not new -> The car is not new
# This cottage cheese is not so bad -> This cottage cheese is good 
# Hints:
# Find (or index, or even rfind) will probably come in handy, as may an operator. Also slice syntax will be useful.

# Extra: How would you do this task in Latvian language (nav slikts/a -> ir labs/a)?

# MY CODE DOESN'T HANDLE CASES LIKE 'A IS NOT BAD AND B IS NOT SO BAD' - I DON'T HAVE TIME NOW TO REVIEW IT

textt = input("Please enter some text: ")
start_word = 'not'
end_word = 'bad'
new_line = 'good'
check1 = False
Check2 = False
if (start_word in textt) and (end_word in textt):
    start_ind = textt.index(start_word)
    end_ind = textt.index(end_word)
    line_end = end_ind + len(end_word)
    if start_ind < end_ind:
        old_line = textt[start_ind:end_ind + len(end_word)]
        print(textt.replace(old_line, new_line))
else:
    print(textt)

# Previous solution but also doesn't handle all cases
# textt = input("Please enter some text: ")
# start_word = 'not'
# end_word = 'bad'
# new_line = 'good'
# check1 = False
# Check2 = False
# if (start_word in textt) and (end_word in textt):
#     start_ind = textt.index(start_word)
#     check1 = True
#     end_ind = textt.index(end_word)
#     check2 = True
#     line_end = end_ind + len(end_word)
# else:
#     print(textt)

# if (check1 == True and check2 == True and start_ind < end_ind):
#     old_line = textt[start_ind:end_ind + len(end_word)]
#     print(textt.replace(old_line, new_line))
