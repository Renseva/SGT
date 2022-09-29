# write a function of 3 arguments all strings
# function should return lexigraphically ordered string of unique characters
# these unique characters must be present in BOTH  of the first two strings 
# BUT not in the third "badstring"

# example:
# "abcf", "fab", "boo"  returns -> "af" 
# because "a" is in both "abc" and "fab" but not in "boo"
# same goes for "f" it is present in both "good strings" but not in "badstring"
# notice "b" is not in the result because it is in the badstring.

# slightly harder way would be to use loops and if statements to check each character
# the easy way is to use sets and set operations 😊

# either approach is acceptable

def lexi(*arg):
    if len(arg) != 3:
        return 0 # same as someone, don't know how to output a message only
    set1 = set(arg[0])
    set2 = set(arg[1])
    set3 = set(arg[2])
    set_common = set(set1 & set2)
    return "".join(sorted(set(set_common - set(set_common & set3)))) # common btwn 1 and 2 minus common with 3
 
print(lexi("labadiena", "labas", "lenda"))
print(lexi("labadiena", "lenda", "labas"))
print(lexi("abcf", "fab", "boo"))
# print(lexi("lalala"))

