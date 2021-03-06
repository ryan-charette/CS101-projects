#Difficult Python Code Challenges involving Functions

#1. First Three Multiples
#Write a function named first_three_multiples() that has one parameter named num.
#This function should print the first three multiples of num. Then, it should return the third multiple.
#For example, first_three_multiples(7) should print 7, 14, and 21 on three different lines, and return 21.

def first_three_multiples(num):
    print(num)
    print(num * 2)
    print(num * 3)
    return num * 3

#2. Tip
#Create a function called tip() that has two parameters named total and percentage.
#This function should return the amount you should tip given a total and the percentage you want to tip.

def tip(total, percentage):
    return total * percentage / 100

#3. Bond, James Bond
#Write a function named introduction() that has two parameters named first_name and last_name.
#The function should return the last_name, followed by a comma, a space, first_name another space, and finally last_name.

def introduction(first_name, last_name):
    return(last_name + ", " + first_name + " " + last_name)

#4. Dog Years
#Some say that every one year of a human’s life is equivalent to seven years of a dog’s life. Write a function named dog_years() that has two parameters named name and age.
#The function should compute the age in dog years and return the following string:
#"{name}, you are {age} years old in dog years"

def dog_years(name, age):
    return(name + ", you are " + str(age * 7) + " years old in dog years")

#5. All Operations
#Create a function named lots_of_math(). This function should have four parameters named a, b, c, and d. The function should print 3 lines and return 1 value.
#First, print the sum of a and b.
#Second, print c minus d.
#Third, print the first number printed, multiplied by the second number printed.
#Finally, return the third number printed modulo a.

def lots_of_math(a, b, c, d):
    print(sum:= a + b)
    print(difference:= c - d)
    print(product:= sum * difference)
    return(product % a)
