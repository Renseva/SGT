# 2. Xmas Bonus

# The company has promised a Christmas bonus in the amount of 15% of the monthly salary for EVERY year of 
# service over 2 years.

# Task. Ask the user for the amount of the monthly salary and the number of years worked.
m_salary = int(input("Please let me know your monthly salary in Euro ;) :"))
work_years = float(input("How many years have you worked here? "))

# Calculate the bonus.
if work_years > 2:
    year_bonus = int(m_salary * 0.15)
    # also assuming no bonus for part of a year over 2 years....
    total_bonus = (int(work_years) - 2) * year_bonus
    print(f"With your {work_years} of experience and {m_salary} Euros monthly salary, your Christmas bonus will be {total_bonus} \n")
else:
    print(f"With your {work_years} of experience and {m_salary} Euros monthly salary, sorry, no Christmas bonus... \n")

# Example1: 5 years of experience, 1000 Euro salary, the bonus will be 450 Euro.

# Example2: 1.5 years of experience, 1500 Euro salary, no bonus(0)

