#!/usr/bin/env python
# coding: utf-8

# # Assignments

# Q1. Write the Python function to get a string made of 4 copies of the last
# two characters of the specified string (length must be at least 2).
# 
#     Sample function and result :
#     insert-end ('Python') -> abababab
#     insert-end('Exercises') -> jkjkjkjk

# In[8]:


#Python function to get a string made of 4 copies of the last two characters 
   #of the specified string (length must be at least 2).
def four_str_Fun(str):
   if len(str)>2:
       str = str[-2:]*4 
       return str
   else:
       return str

str='testing'
str2='in'
four_str_Fun(str)
#four_str_Fun(str2)


# Q2. Write the python function to get a string made of its first three
# characters of a specified string. If the length of the string is less than 3
# then return the original string.
#     
#     Sample function and result :
#     first-three('ipy') -> ipy
#     first-three('python') -> pyt

# In[9]:


#Python function to get a string made of its first three characters 
   #of a specified string. If the length of the string is less than 3 then return the original string.
def three_char_Fun(str):
   if len(str)>3:
       str = str[:3]
       return str
   else:
       return str

str='testing'
str2='in'
three_char_Fun(str)
#three_char_Fun(str2)


# Q3. Write the Python program to find smallest window that contains all
# characters of the given string?
# 
#     Original Strings:
#     asdaewsqgtwwsa
#     Smallest window that contains all characters of the said string:
#     Daewsqgt

# In[10]:


from collections import defaultdict   

def find_sub_string(str): 
    str_len = len(str) 
      
    # Count all distinct characters. 
    dist_count_char = len(set([x for x in str])) 
  
    ctr, start_pos, start_pos_index, min_len = 0, 0, -1, 9999999999
    curr_count = defaultdict(lambda: 0) 
    for i in range(str_len): 
        curr_count[str[i]] += 1
 
        if curr_count[str[i]] == 1: 
            ctr += 1
  
        if ctr == dist_count_char: 
            while curr_count[str[start_pos]] > 1: 
                if curr_count[str[start_pos]] > 1: 
                    curr_count[str[start_pos]] -= 1
                start_pos += 1
  
            len_window = i - start_pos + 1
            if min_len > len_window: 
                min_len = len_window 
                start_pos_index = start_pos 
    return str[start_pos_index: start_pos_index + min_len] 
      
str1 = "asdaewsqgtwwsa"
print("Original Strings:\n",str1)
print("\nSmallest window that contains all characters of the said string:")
print(find_sub_string(str1)) 


# Q4. Write the Python program to count number of substrings from a
# given string of lowercase alphabets with exactly k distinct (given)
# characters?
# 
#     Input a string (lowercase alphabets): wolf
#     Input k: 4
#     Number of substrings with exactly 4 distinct characters: 1

# In[11]:


def count_k_dist_Fun(str1, k):
    str_len = len(str1)
    result = 0
    cntr = [0] * 27
    for i in range(0, str_len):
        dist_cntr = 0
        
        cntr = [0] * 27
        for j in range(i, str_len):
            if(cntr[ord(str1[j]) - 97] == 0):
                dist_cntr += 1

            cntr[ord(str1[j]) - 97] += 1

            if(dist_cntr == k):
                result += 1
            if(dist_cntr > k):
                break

    return result 

str1 = input("Input a string (lowercase alphabets):")
k = int(input("Input k: "))
print("Number of substrings with exactly", k, "distinct characters : ", end = "") 
print(count_k_dist_Fun(str1, k))


# Q5. Write the Python program to count number of non-empty
# substrings of the given string?
# 
#     Input a string: w3resource
#     Number of substrings:
#     55

# In[12]:


def number_of_substrings(str): 
    str_len = len(str)
    return int(str_len * (str_len + 1) / 2) 

str1 = input("Input a string: ")
print("Number of substrings:") 
print(number_of_substrings(str1))


# Q6. Write the Python program to count the number of strings where the
# string length is 2 or more, and first and last character are same
# from a given list of strings.
# 
#     Sample List : ['abc', 'xyz', 'wxw', '1331']
#     Expected Result: 2

# In[13]:


def match_words_fun(words):
  counter = 0

  for word in words:
    if len(word) > 1 and word[0] == word[-1]:
      counter += 1
  return counter

print(match_words_fun(['abc', 'xyz', 'wxw', '1331']))


# Q7. Write the Python program to get a list, sorted in increasing order by
# the last element in each tuple from the given list of non-empty
# tuples?
# 
#     Sample List - [ (2, 5), (1, 2), (4, 4), (2, 3), (2, 1) ]
#     Expected Result - [ (2, 1), (1, 2), (2, 3), (4, 4), (2, 5) ]

# In[14]:


def last(n): return n[-1]

def sort_list_last_fun(tuples):

  return sorted(tuples, key=last)

print(sort_list_last_fun([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))


# Q8. Write the Python program to remove duplicates from a list?

# In[15]:


dup_lst = [90,10,30,40,10,50,30,10,30,60,70,20]
dup_items = set(dup_lst)
ori_lst = list(dup_items)
ori_lst


# Q9. Write the Python program to find the list of words that are longer
# than n from a given list of words?

# In[16]:


def long_words_fun(n, str):
    word_len = []
    txt = str.split(" ")
    for x in txt:
        if len(x) > n:
            word_len.append(x)
    return word_len	
print(long_words_fun(4, "The quick brown fox jumps over the lazy cat"))


# Q10. Write the Python program to print a specified list after removing the
# 0th, 4th, and 5th elements?
#     
#     Sample List - ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
#     Expected Output - ['Green', 'White', 'Black']

# In[17]:


sampleList = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
sampleList = [x for (i,x) in enumerate(sampleList) if i not in (0,4,5)] #removing the 0th, 4th, and 5th elements
print(sampleList)


# Q11. Write the Python program to generate all permutations of a list in
# Python?

# In[18]:


import itertools
print(list(itertools.permutations(['a','b','c'])))


# Q12. Write the Python program to convert a pair of values into a sorted
# unique array?
#  
#     Original List- [ (1, 2), (3, 4), (1, 2), (5, 6), (7, 8), (1, 2), (3, 4), (3, 4), (7, 8), (9, 10) ]
#     Sorted Unique Data- [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ] 
# 

# In[19]:


OriList = [ (1, 2), (3, 4), (1, 2), (5, 6), (7, 8), (1, 2), (3, 4), (3, 4), (7, 8), (9, 10) ]
print("Sorted Unique Array:",sorted(set().union(*OriList)))

