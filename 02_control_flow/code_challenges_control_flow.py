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
    if budget < food_bill + electricity_bill + internet_bill + rent:
        return True
    else:
        return False

#3. Twice As Large
#Create a function named twice_as_large() that has two parameters named num1 and num2.
#Return True if num1 is more than double num2. Return False otherwise.

def twice_as_large(num1, num2):
    if num1 > num2 * 2:
        return True
    else:
        return False

#4. Divisible By Ten
#Create a function called divisible_by_ten() that has one parameter named num.
#The function should return True if num is divisible by 10, and False otherwise. Consider using modulo operator % to check for divisibility.

def divisible_by_ten(num):
    if num % 10 == 0:
        return True
    else:
        return False

#5. Not Sum To Ten
#Create a function named not_sum_to_ten() that has two parameters named num1 and num2.
#Return True if num1 and num2 do not sum to 10. Return False otherwise.

def not_sum_to_ten(num1, num2):
    if num1 + num2 != 10:
        return True
    else:
        return False
