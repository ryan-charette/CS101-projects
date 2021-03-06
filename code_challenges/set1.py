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

#Difficult Python Code Challenges involving Control Flow

#1. In Range
#Create a function named in_range() that has three parameters named num, lower, and upper.
#The function should return True if num is greater than or equal to lower and less than or equal to upper. Otherwise, return False.

def in_range(num, lower, upper):
    if lower <= num <= upper:
        return True
    else:
        return False

#2. Same Name
#Create a function named same_name() that has two parameters named your_name and my_name.
#If our names are identical, return True. Otherwise, return False.

def same_name(your_name, my_name):
    if your_name == my_name:
        return True
    else:
        return False

#3. Always False
#Create a function named always_false() that has one parameter named num.
#Using an if statement, your variable num, and the operators >, and <, make it so your function will return False no matter what number is stored in num.
#An if statement that is always false is called a contradiction. You will rarely want to do this while programming, but it is important to realize it is possible to do this.

def always_false(num):
    if num < num:
        return True
    else:
        return False

#4. Movie Review
#Create a function named movie_review() that has one parameter named rating.
#If rating is less than or equal to 5, return "Avoid at all costs!". If rating is between 5 and 9, return "This one was fun.". If rating is 9 or above, return "Outstanding!"

def movie_review(rating):
    if rating <= 5:
        return "Avoid at all costs!"
    elif rating < 9:
        return "This one was fun."
    else:
        return "Outstanding!"

#5. Max Number
#Create a function called max_num() that has three parameters named num1, num2, and num3.
#The function should return the largest of these three numbers. If any of two numbers tie as the largest, you should return "It's a tie!".

def max_num(num1, num2, num3):
    if sorted([num1, num2, num3])[1] !=  max(num1, num2, num3):
        return max(num1, num2, num3)
    else:
        return "It's a tie!"

#Python Code Challenges involving Lists

#1. Append Size
#Create a function called append_size that has one parameter named lst.
#The function should append the size of lst (inclusive) to the end of lst. The function should then return this new list.
#For example, if lst was [23, 42, 108], the function should return [23, 42, 108, 3] because the size of lst was originally 3.

def append_size(lst):
    lst.append(len(lst))
    return lst

#2. Append Sum
#Write a function named append_sum that has one parameter — a list named named lst.
#The function should add the last two elements of lst together and append the result to lst. It should do this process three times and then return lst.
#For example, if lst started as [1, 1, 2], the final result should be [1, 1, 2, 3, 5, 8].

def append_sum(lst):
    for i in range(3):
        lst.append(lst[-1] + lst[-2])
    return lst

#3. Larger List
#Write a function named larger_list that has two parameters named lst1 and lst2.
#The function should return the last element of the list that contains more elements. If both lists are the same size, then return the last element of lst1.

def larger_list(lst1, lst2):
    if len(lst1) >= len(lst2):
        return lst1[-1]
    else:
        return lst2[-1]

#4. More Than N
#Create a function named more_than_n that has three parameters named lst, item, and n.
#The function should return True if item appears in the list more than n times. The function should return False otherwise.

def more_than_n(lst, item, n):
    if lst.count(item) > n:
        return True
    else:
        return False
        
#5. Combine Sort
#Write a function named combine_sort that has two parameters named lst1 and lst2.
#The function should combine these two lists into one new list and sort the result. Return the new sorted list.

def combine_sort(lst1, lst2):
    return sorted(lst1 + lst2)

#Difficult Python Code Challenges involving Lists

#1. Every Three Numbers
#Create a function called every_three_nums that has one parameter named start.
#The function should return a list of every third number between start and 100 (inclusive). For example, every_three_nums(91) should return the list [91, 94, 97, 100]. If start is greater than 100, the function should return an empty list.

def every_three_nums(start):
  return list(range(start, 101, 3))

#2. Remove Middle
#Create a function named remove_middle which has three parameters named lst, start, and end.
#The function should return a list where all elements in lst with an index between start and end (inclusive) have been removed.
#For example, the following code should return [4, 23, 42] because elements at indices 1, 2, and 3 have been removed:
#remove_middle([4, 8 , 15, 16, 23, 42], 1, 3)

def remove_middle(lst, start, end):
    return lst[:start] + lst[end + 1:]

#3. More Frequent Item
#Create a function named more_frequent_item that has three parameters named lst, item1, and item2.
#Return either item1 or item2 depending on which item appears more often in lst.
#If the two items appear the same number of times, return item1.

def more_frequent_item(lst, item1, item2):
    if lst.count(item1) >= lst.count(item2):
        return item1
    else:
        return item2

#4. Double Index
#Create a function named double_index that has two parameters: a list named lst and a single number named index.
#The function should return a new list where all elements are the same as in lst except for the element at index. The element at index should be double the value of the element at index of the original lst.
#If index is not a valid index, the function should return the original list.
#For example, the following code should return [1,2,6,4] because the element at index 2 has been doubled:
#double_index([1, 2, 3, 4], 2)

def double_index(lst, index):
    try:
        lst[index] *= 2
    except:
        IndexError
    return lst

#5. Middle Item
#Create a function called middle_element that has one parameter named lst.
#If there are an odd number of elements in lst, the function should return the middle element. If there are an even number of elements, the function should return the average of the middle two elements.

def middle_element(lst):
    if len(lst) % 2 != 0:
        return lst[len(lst) // 2]
    else:
        return (lst[len(lst) // 2] + lst[len(lst) // 2 - 1]) / 2

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

#Difficult Python Code Challenges involving Loops

#1. Larger Sum
#Create a function named larger_sum() that takes two lists of numbers as parameters named lst1 and lst2.
#The function should return the list whose elements sum to the greater number. If the sum of the elements of each list are equal, return lst1.

def larger_sum(lst1, lst2):
    if sum(lst1) >= sum(lst2):
        return lst1
    else:
        return lst2

#2. Over 9000
#Create a function named over_nine_thousand() that takes a list of numbers named lst as a parameter.
#The function should sum the elements of the list until the sum is greater than 9000. When this happens, the function should return the sum. If the sum of all of the elements is never greater than 9000, the function should return total sum of all the elements. If the list is empty, the function should return 0.
#For example, if lst was [8000, 900, 120, 5000], then the function should return 9020.

def over_nine_thousand(lst):
    sum = 0
    for num in lst:
        sum += num
        if sum > 9000:
            break
    return sum

#3. Max Num
#Create a function named max_num() that takes a list of numbers named nums as a parameter.
#The function should return the largest number in nums

def max_num(nums):
    return max(nums)

#4. Same Values
#Write a function named same_values() that takes two lists of numbers of equal size as parameters.
#The function should return a list of the indices where the values were equal in lst1 and lst2.
#For example, the following code should return [0, 2, 3]
#same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5])

def same_values(lst1, lst2):
    equal_lst = [i for i in range(len(lst1)) if lst1[i] == lst2[i]]
    return equal_lst

#5. Reversed List
#Create a function named reversed_list() that takes two lists of the same size as parameters named lst1 and lst2.
#The function should return True if lst1 is the same as lst2 reversed. The function should return False otherwise.
#For example, reversed_list([1, 2, 3], [3, 2, 1]) should return True.

def reversed_list(lst1, lst2):
    if lst1 == list(reversed(lst2)):
        return True
    else:
        return False

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
