#Python Code Challenges involving Loops

#1. Divisible by Ten
#Create a function named divisible_by_ten() that takes a list of numbers named nums as a parameter.
#Return the count of how many numbers in the list are divisible by 10.

def divisible_by_ten(nums):
    counter = 0
    for num in nums:
        if num % 10 == 0:
            counter += 1
    return counter

#2. Greetings
#Create a function named add_greetings() which takes a list of strings named names as a parameter.
#In the function, create an empty list that will contain each greeting. Add the string 'Hello, ' in front of each name in names and append the greeting to the list.
#Return the new list containing the greetings.

def add_greetings(names):
    greetings = []
    for name in names:
        greetings.append("Hello, " + name)
    return greetings

#3. Delete Starting Even Numbers
#Write a function called delete_starting_evens() that has a parameter named lst.
#The function should remove elements from the front of lst until the front of the list is not even. The function should then return lst.
#For example if lst started as [4, 8, 10, 11, 12, 15], then delete_starting_evens(lst) should return [11, 12, 15].
#Make sure your function works even if every element in the list is even!

def delete_starting_evens(lst):
    while len(lst) > 0 and lst[0] % 2 == 0:
        lst.pop(0)
    return lst

#4. Odd Indicies
#Create a function named odd_indices() that has one parameter named lst.
#The function should create a new empty list and add every element from lst that has an odd index. The function should then return this new list.
#For example, odd_indices([4, 3, 7, 10, 11, -2]) should return the list [3, 10, -2].

def odd_indices(lst):
    lst_odds = [lst[i] for i in range(1, len(lst), 2)]
    return lst_odds

#5. Exponents
#Create a function named exponents() that takes two lists as parameters named bases and powers. Return a new list containing every number in bases raised to every number in powers.
#For example, consider the following code.
#exponents([2, 3, 4], [1, 2, 3])
#the result would be the list [2, 4, 8, 3, 9, 27, 4, 16, 64]. It would first add two to the first. Then two to the second. Then two to the third, and so on.

def exponents(bases, powers):
    exponent_lst = []
    for base in bases:
        for power in powers:
            exponent_lst.append(base ** power)
    return exponent_lst
