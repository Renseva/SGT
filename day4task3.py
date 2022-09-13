# 3. Primes Check if entered positive number is a prime number.
#  A prime number is a number that divides without remainder only by itself and 1.
# Hint: what numbers do we have to check?

numberr = int(input("Please enter a positive whole number: "))
if numberr == 1:
    print("1 is a prime number.")
else:
    for i in range(2, numberr):
        if numberr % i == 0:
            print(f"{numberr} is not a prime number.")
            break
        else:
            print(f"I think {numberr} is a prime number!")
            break