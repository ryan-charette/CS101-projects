#Python Code Challenges involving Functions

#1. Tenth Power
#Write a function named tenth_power() that has one parameter named num.
#The function should return num raised to the 10th power.

def tenth_power(num):
    return num ** 10

#2. Square Root
#Write a function named square_root() that has one parameter named num.
#Use exponents (**) to return the square root of num.

def square_root(num):
    return num ** 0.5

#3. Win Percentage
#Create a function called win_percentage() that takes two parameters named wins and losses.
#This function should return out the total percentage of games won by a team based on these two numbers.

def win_percentage(wins, losses):
    return 100 * wins / (wins + losses)

#4. Average
#Write a function named average() that has two parameters named num1 and num2.
#The function should return the average of these two numbers.

def average(num1, num2):
    return (num1 + num2) / 2

#5. Remainder
#Write a function named remainder() that has two parameters named num1 and num2.
#The function should return the remainder of twice num1 divided by half of num2.

def remainder(num1, num2):
    return num1 * 2 % (num2 / 2)
