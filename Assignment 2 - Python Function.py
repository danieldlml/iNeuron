#!/usr/bin/env python
# coding: utf-8

# ## Problem Statement

# Q.1 Write a Python Program to implement your own myreduce() function which works exactly like
# Python's built-in function reduce()
# 

# In[37]:


#To display the minimum element in the list with reduce custom function
def myreduce(arg):
    listResults = arg[0]
    for i in arg:
        listResults = min(listResults,i) # min function
    return listResults

#Initialize the list for parameter argument. 
lst = [4,6,8,3,4,6,9]

# Invoke the myreduce function
myreduce(lst)


# Q.2 Write a Python program to implement your own myfilter() function which works exactly like
# Python's built-in function filter()

# In[38]:


#To print the odd numbers with myfilter custom function
def myfilter(lstRng, func):
    resLst = []
    for element in lstRng:
        if func(element):
            resLst.append(element)
    return resLst
# Parameters initialization
func = lambda num: num%2 != 0
lstRng = range(30)  # Upto 30 numbers
#Invoke the myfilter function
print(myfilter(lstRng, func))


# Q.3 Implement List comprehensions to produce the following lists.
#    Write List comprehensions to produce the following Lists
#    
#     ['A', 'C', 'A', 'D', 'G', 'I', ’L’, ‘ D’]
#    
#     ['x', 'xx', 'xxx', 'xxxx', 'y', 'yy', 'yyy', 'yyyy', 'z', 'zz', 'zzz', 'zzzz']
# 
#     ['x', 'y', 'z', 'xx', 'yy', 'zz', 'xx', 'yy', 'zz', 'xxxx', 'yyyy', 'zzzz']
#     
#     [[2], [3], [4], [3], [4], [5], [4], [5], [6]]
# 
#     [[2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7], [5, 6, 7, 8]]
# 
#     [(1, 1), (2, 1), (3, 1), (1, 2), (2, 2), (3, 2), (1, 3), (2, 3), (3, 3)]

# In[39]:


listCompStr = 'ACADGILD'
print(list(listCompStr))
print([x*y for x in 'xyz' for y in range(1,4)])
print([x*(2**y) for y in range(3) for x in 'xyz' ])
print([[x+y] for x in range(2,5) for y in range(3)])
print([list(range(x, x+4)) for x in range(2,6)])
print([(y,x) for x in range(1,4) for y in range(1,4)])


# Q.4 Implement a function longestWord() that takes a list of words and returns the longest one.

# In[40]:


#Function to print the longestWord() that takes a list of words and returns the longest one.
import string
def longestWordFun(usrInput):
    wordLen = {}
    for word in usrInput.split():
        word = word.rstrip(string.punctuation).lower()
        if wordLen.get(len(word), 0) == 0:
            wordLen[len(word)] = [word]
        else:
            wordLen[len(word)].append(word)
    return wordLen[max(wordLen.keys())]
#User input
usrInput = "abc defg hijkl mnopq rstuv"
#Invoke the longest word function
print("The longest words of User's Sentence is/are:",*longestWordFun(usrInput), sep = " ")


# Q.5 Write a Python Program(with class concepts) to find the area of the triangle using the below
# formula.
# 
# area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
# 
# Function to take the length of the sides of triangle from user should be defined in the parent
# class and function to calculate the area should be defined in subclass.

# In[43]:


#Function to take the length of the sides of triangle from user should be defined in the parent class and function to calculate the area should be defined in subclass.

class TriangleArea(object):  #Function to take the length of the sides of triangle 
    def __init__(mine, a, b, c):
        mine.a = a
        mine.b = b
        mine.c = c
        mine.s = (a+b+c)/2 
    def calcArea(mine): #function to calculate the area should be defined in subclass
        return (mine.s*(mine.s-mine.a)*(mine.s-mine.b)*(mine.s-mine.c)) ** 0.5
    
#Initilize the side of the triangle
aa=2
bb=3
cc=4

#Invoke the Class with parameters 
areaTr = TriangleArea(aa,bb,cc)

#Print the area of the triangle by calling the sub class
print("Area of the Triangle  is ",areaTr.calcArea(),"Units")


# Q.6 Write a function filter_long_words() that takes a list of words and an integer n and returns the list
# of words that are longer than n.

# In[44]:



#Function to  filter_long_words() that takes a list of words and an integer n and returns the list of words that are longer than n.

import string

def filter_long_words_Fun(usrString, num):
    for word in usrString.split():
        word = word.rstrip(string.punctuation).lower()
        if len(word) > num:
            print(word)
#User's Inputs
usrString = 'abc defgh ijk lmno pqrstu'
num_len = 4

#print the output of the required logic
print("The following are the words which islonger than the user's input : ")
filter_long_words_Fun(usrString, num_len)


# Q.7 Write a Python program using function concept that maps list of words into a list of integers
# representing the lengths of the corresponding words.
#     
#     Hint: If a list [ ab,cde,erty] is passed on to the python function output should come as [2,3,4]
#     Here 2,3 and 4 are the lengths of the words in the list.

# In[45]:


#Python program using function concept that maps list of words into a list of integers representing the lengths of the corresponding words.

import string

def lenWords_Fun(usrList):
    return [len(word.rstrip(string.punctuation).lower()) for word in usrList]
#User's inputs
usrList = ['1234567','12345','123456789','1234','abcdefghijklmnopqrstuvwxyz']
#Invoke the function to print the length/size of strings
lenWords_Fun(usrList)


# Q.8 Write a Python function which takes a character (i.e. a string of length 1) and returns True if it is
# a vowel, False otherwise.

# In[46]:


#Function to print whether the given char is vowel or not
def isVowel_Func(char):
    vowels = 'aeiou' # initialize the vowels - aeiou
    return True if char.lower() in vowels else False 

print(isVowel_Func('B')) #Invoke to test the Capital B
print(isVowel_Func('A')) #Invoke to test the Capital A
print(isVowel_Func('e')) #Invoke to test the small e
print(isVowel_Func('1')) #Invoke to test the number 1

