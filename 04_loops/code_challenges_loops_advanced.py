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
