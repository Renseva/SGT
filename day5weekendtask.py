# write a program that asks for two text inputs s1 and s2 
# you can use better names than s1 and s2

# then checks if all the characters in first string are in second string
# if they are, print All character counts in the second string
# if not, print Not all characters are in the second string
# example
# s1 = "abc"
# s2 = "abracadabra"
# output: a 5, b 2, c 1, d 1, r 2  # so do not print the empty ones

# example two
# s1 = "abc"
# s2 = "def"
# output: Not all characters are in the second string

# on assumption characters don't repeat in s1
import enum

s1 = input("enter one of two strings of characters:")
s2 = input("enter the second (not shorter) string of characters:")
n1 = len(s1)
n2 = len(s2)
x = 0
outp_string = ""

for i in s1:
    if i in s2:
        x += 1
if x == n1:
    for i in s1:
        for j, c in enumerate(s2):
            if i == c and (i in outp_string) == False:
                m = str(s2.count(i))
                if j < len(s2) - 1:
                    outp_string += i + " " + m +", "
                else:
                    outp_string += i + " " + m
            elif (c in outp_string) == False:
                n = str(s2.count(c))
                if j < len(s2) - 1:
                    outp_string += c + " " + n + ", "
                else:
                    outp_string += c + " " + n
    print(outp_string)
else:
    print("Not all characters are in the second string.")

# need to sort out end ,
# need to exclude multiple instances 
# print("all characters are in  the second string")

# print (i, m, end = ",")
        # s2 = s2.replace(i, " ")

 # if i != j and j.isspace() == False:     
            #     n = s2.count(j)
            #     print(j, n, end =",")
            #     s2 = s2.replace(j, " ")