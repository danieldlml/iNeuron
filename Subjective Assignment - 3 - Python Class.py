#!/usr/bin/env python
# coding: utf-8

# # Assignment

# Q1. Write the Python class to convert an integer to a roman numeral?

# In[29]:


# Python class to convert an integer to a roman numeral
class py_sol:
    def int_to_Roman(self, num):
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
            ]
        syb = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
            ]
        roman_num = ''
        i = 0
        while  num > 0:
            for _ in range(num // val[i]):
                roman_num += syb[i]
                num -= val[i]
            i += 1
        return roman_num


#print(py_sol().int_to_Roman(8))
print(py_sol().int_to_Roman(800))


# Q2 Write the Python class to convert a Roman numeral to an integer?
# 

# In[30]:


#Python Class to convert a Roman numeral to an integer

class py_sol:
    def roman_to_int(self, s):
        rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        int_val = 0
        for i in range(len(s)):
            if i > 0 and rom_val[s[i]] > rom_val[s[i - 1]]:
                int_val += rom_val[s[i]] - 2 * rom_val[s[i - 1]]
            else:
                int_val += rom_val[s[i]]
        return int_val

print(py_sol().roman_to_int('MMMCMLXXXVI'))


# Q3. Write the Python class to find the validity of the string of the
# parentheses, '(', ')', '{', '}', '[' and '] and the brackets must be closed
# in the correct order, example - "()" and "()[]{}" are valid but "[)",
# "({[)]" and "{{{" are invalid.
# 

# In[31]:


#Python class to find the validity of the string of the parentheses

class py_sol:
   def is_valid_parenthesis_fun(self, str1):
        stack, pchar = [], {"(": ")", "{": "}", "[": "]"}
        for parenthese in str1:
            if parenthese in pchar:
                stack.append(parenthese)
            elif len(stack) == 0 or pchar[stack.pop()] != parenthese:
                return False
        return len(stack) == 0

print(py_sol().is_valid_parenthesis_fun("[{()}]"))
print(py_sol().is_valid_parenthesis_fun("(){}[]"))
print(py_sol().is_valid_parenthesis_fun("([{)}"))
print(py_sol().is_valid_parenthesis_fun("{[("))


# Q4. Write the Python class to get all possible unique subsets from a set
# of distinct integers?
# 
#     Input - [4, 5, 6]
#     Output - [[], [6], [5], [5, 6], [4], [4, 6], [4, 5], [4, 5, 6]]

# In[32]:


#Python class to get all possible unique subsets from a set of distinct integers
class py_sol:
    def sub_sets_fun(self, sset):
        return self.subsetsRecur_fun([], sorted(sset))
    
    def subsetsRecur_fun(self, current, sset):
        if sset:
            return self.subsetsRecur_fun(current, sset[1:]) + self.subsetsRecur_fun(current + [sset[0]], sset[1:])
        return [current]

print(py_sol().sub_sets_fun([4,5,6]))


# Q5. Write the Python class to find a pair of elements (indices of the two
# numbers) from a given array whose sum equals the specific target
# number?
# 
#     Input: numbers- [10,20,10,40,50,60,70], target=50
#     Output- 3, 4

# In[33]:


# Python class to find a pair of elements (indices of the two numbers) from a given array whose sum equals the specific target number

class py_sol:
   def twoSum_fun(self, nums, target):
        lookup = {}

        for i, num in enumerate(nums):
            if target - num in lookup:
                return (lookup[target - num], i )
            lookup[num] = i
            
print("index1=%d, index2=%d" % py_sol().twoSum_fun((10,20,10,40,50,60,70),50))  #50 : target to sum


# Q6. Write the Python class to find the three elements that sum to zero
# from the set of n real numbers?
# 
#     Input array- [-25, -10, -7, -3, 2, 4, 8, 10]
#     Output - [[-10, 2, 8], [-7, -3, 10]]
# 

# In[34]:


class py_solution:
 def threeSum(self, nums):
        nums, result, i = sorted(nums), [], 0
        while i < len(nums) - 2:
            j, k = i + 1, len(nums) - 1
            while j < k:
                if nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                elif nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                else:
                    result.append([nums[i], nums[j], nums[k]])
                    j, k = j + 1, k - 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
            i += 1
            while i < len(nums) - 2 and nums[i] == nums[i - 1]:
                i += 1
        return result

print(py_solution().threeSum([-25, -10, -7, -3, 2, 4, 8, 10]))


# Q7. Write the Python class to implement pow(x, n)?

# In[35]:


#Python class to implement pow(x, n)

class py_sol:
   def pow(self, x, n):
        if x==0 or x==1 or n==1:
            return x 

        if x==-1:
            if n%2 ==0:
                return 1
            else:
                return -1
        if n==0:
            return 1
        if n<0:
            return 1/self.pow(x,-n)
        val = self.pow(x,n//2)
        if n%2 ==0:
            return val*val
        return val*val*x

print(py_sol().pow(2, -3));
print(py_sol().pow(3, 5));
print(py_sol().pow(100, 0));


# Q8. Write the Python class which has two methods get_String and
# print_String. get_String accept the string from the user and 
# print_String print the string in upper case.

# In[36]:


#Python class which has two methods get_String and print_String. get_String accept the string from the user and print_String print the string in upper case.

class IOString():
    def __init__(self):
        self.str1 = ""

    def get_String(self):
        self.str1 = input()

    def print_String(self):
        print(self.str1.upper())

str1 = IOString()
str1.get_String()
str1.print_String()


# Q9. Write the Python class named Rectangle constructed by a length
# and width and the method which will compute the area of the
# rectangle?

# In[37]:


#Python class named Rectangle constructed by a length and width and the method which will compute the area of the rectangle

class Rectangle():
    
    def __init__(self, ln, wd):
        self.length = ln
        self.width = wd
    
    def area_rectangle(self):
        return self.length * self.width
    
newRect = Rectangle(6,4)

print("Area of Rectangle is :",newRect.area_rectangle(),"Sq.units")


# Q10. Write the Python class named Circle constructed by the radius
# and two methods which will compute the area and perimeter of
# the circle?

# In[38]:


#Python class named Circle constructed by the radius and two methods which will compute the area and perimeter of the circle

class Circle():
    
    def __init__(self, rad):
        self.radius = rad
        
    def areaCircle(self):
        return 3.14*self.radius**2  #Area = π * r^2
    
    def circumferenceCircle(self):
        return 2*3.14*self.radius  #circumference = 2 * π * r
    
newCirc = Circle(10) # Radius of the Circle
print("Area of Circle is :",newCirc.areaCircle(),"Sq.Units")
print("Circumference of Circle is :",newCirc.circumferenceCircle(),"Sq.Units")


# Q11. Write the Python program to get the class name of an instance in
# Python?

# In[39]:


import itertools
x = itertools.count(20)
print(type(x).__name__)


# In[40]:


#Python program to count the number of students of individual class
from collections import Counter
data_classes = (
    ('V', 1),
    ('VI', 1),
    ('V', 2),
    ('VI', 2),
    ('VI', 3),
    ('VII', 1),
)
students = Counter(class_name for class_name, num_students in data_classes)
print(students)

