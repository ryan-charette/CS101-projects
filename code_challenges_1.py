#Python Code Challenges involving Control Flow

#1. Large Power
#Create a function named large_power() that takes two parameters named base and exponent.
#If base raised to the exponent is greater than 5000, return True, otherwise return False

def large_power(base, exponent):
    if base ** exponent > 5000:
        return True
    else:
        return False

#2. Over Budget
#Create a function called over_budget that has five parameters named budget, food_bill, electricity_bill, internet_bill, and rent.
#The function should return True if budget is less than the sum of the other four parameters — you’ve gone over budget! Return False otherwise.

def over_budget(budget, food_bill, electricity_bill, internet_bill, rent):