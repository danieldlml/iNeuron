#!/usr/bin/env python
# coding: utf-8

# Q1. Write a Python program to get the string from the given string where
# all the occurrence of its first char has been changed to '$,' except first
# char itself?
# 
#     Sample String: 'prospect'
#     Expected Result : 'pros$ect'
# 

# In[22]:


Strings are immutable in Python, which means you cannot change an existing string. 
However the expected result can be achieved by dividing the string into char and then replace the required char to '$'


# Q2. Write a Python program to get the single string from the two given
# strings, and separated by the space and swap the first two characters of
# each string?
# 
#     Sample String : 'abc', 'xyz'.
#     Expected Result: 'xyc abz'

# In[ ]:


str = "abc, xyz"
str1 = str[-3:-1]+str[2:3] # swap the first two characters of each string
str2 = str[:2]+str[-1:] # swap the first two characters of each string
swapStr = list([str1,str2])
swapStr


# Q3. Write the Python program to add 'ing' at the end of the given string
# (length of the string should be at least 3). If given string already ends
# with 'ing,' then add 'ly' instead. If string length of the given string is less
# than 3, leave it unchanged?
# 
# 
#     Sample string: ' abc '
#     Expected result: ' abcing '
#     Sample string: ' string '
#     Expected result: ' stringly '
# 

# In[ ]:


def inglyFun(str):
    if str[-3:] =='ing':
        return str
    else:
        str = str+'ly' 
        return str
    
#inglyFun('surprise') # call the function to execute
#inglyFun('surprising')


# Q4. Write the Python program to find the first appearance of the
# substring 'not' and 'poor' from the given string, if 'not' follows the 'poor',
# replace the whole 'not'...' poor' substring with 'good'.Return the resulting
# string.
# 
#     Sample string: 'The lyrics are not that poor!'
#     'The lyrics are poor!'
#     Expected Result: 'The lyrics are good!'
#     'The lyrics are poor!'

# In[ ]:


def replaceNegFun(sampleString):
    index = sampleString.find('not poor')
    if index !=-1:
        stmt = sampleString.replace("not poor", "Rich")
        return stmt
    else:
        return sampleString
    
#replaceNegFun('The lyrics are not poor !')  # call the function to execute


# Q5. Write the Python program to remove the characters which have odd
# index values of a given string.

# In[ ]:


str = "1234567890"
str[1::2]


# Q6. Write the python program to print the following floating numbers up
# to 2 decimal places?

# In[ ]:


flt2dec=345435.459
print("%.2f" % flt2dec)


# Q7. Write the Python program to format a number with a percentage?

# In[ ]:


num2Per=0.98765
print(format(num2Per,".2%") )


# Q8. Write the Python program to count occurrences of a substring in a
# String?

# In[ ]:


sampleString = "The lyrics are not not poor!"
print(sampleString.count('not'))


# Q9. Write the Python program to count repeated characters in a string.
# 
#     Sample string: ' thequickbrownjumpsoverthelazydog '
#     
#     Expected output:
#     o 3
#     e 3
#     u 2
#     h 2
#     r 2
#     t 2

# In[ ]:


sampleString = "thequickbrownjumpsoverthelazydog"
print('o',sampleString.count('o'))
print('e',sampleString.count('e'))
print('u',sampleString.count('u'))
print('h',sampleString.count('h'))
print('r',sampleString.count('r'))
print('t',sampleString.count('t'))


# Q10. Write the Python program to print the square and cube symbol in
# the area of a rectangle and volume of a cylinder?
# 
#     Sample outputThe area of the rectangle is 1256.66cm2
#     The volume of the cylinder is 1254.725cm3
# 

# In[ ]:


#Initialiaze the variables of radius, π
# for Rectangle
length = 11.0
breadth = 11.0
height = 11.0
areaRect = length * breadth * height
print('\nThe area of the rectangle is ',areaRect,'cm2')

# for Cylinder
rad = 12.0
piVal = 3.1415926535897931
# Formula for the Volume of Sphere
volSphere = 4.0/3.0*piVal* rad**3
#Print the Volume of the Sphere
print('\nThe volume of the cylinder is ',volSphere,'cm3')


# Q11. Write the Python program to check if a string contains all letters of
# the alphabet?

# In[ ]:


import string
def containsAlphaFun(inputString):
    alphabet = set(string.ascii_lowercase)
    checkChars = set(inputString.lower()) >= alphabet
    if  checkChars == True:
        return "The string contains all letters of the alphabet"
    else:
        return "The string doesn't contains all letters of the alphabet"
    
#containsAlphaFun("The quick brown fox jumps over the lazy dog")
#containsAlphaFun("The quick brown fox jumps over the lazy cat")


# Q12. Write the Python program to find the second most repeated word
# in a given string?

# In[ ]:


from collections import Counter
def secMaxCharFun(sampleStr):
    countChars = Counter(sampleStr)
    sortedList = sorted(countChars.values(), reverse=True)
    secLargest = sortedList[2]
    for(key,val) in countChars.items():
        if val == secLargest:
            print('Second Largest string is ',key)
            return
        
#secMaxCharFun("b b b c c c e b c b") # Run the function


# Q13. Write the Python program to find the minimum window in the given
# string, which will contains all the characters of another given
# strings?
# 
#     Example 1
#     Input : string1 = " PRWSOERIUSFK "
#     string2 = " OSU "
#     Output: Minimum window is "OERIUS"

# In[ ]:



no_of_chars = 256

# Function to find smallest window 
# containing all characters of 'pat' 
def findSubString(string, pat): 

	len1 = len(string) 
	len2 = len(pat) 

	# check if string's length is less than pattern's 
	# length. If yes then no such window can exist 
	if len1 < len2: 
	
		print("No such window exists") 
		return "" 

	hash_pat = [0] * no_of_chars 
	hash_str = [0] * no_of_chars 

	# store occurrence ofs characters of pattern 
	for i in range(0, len2): 
		hash_pat[ord(pat[i])] += 1

	start, start_index, min_len = 0, -1, float('inf') 

	# start traversing the string 
	count = 0 # count of characters 
	for j in range(0, len1): 
	
		# count occurrence of characters of string 
		hash_str[ord(string[j])] += 1

		# If string's char matches with 
		# pattern's char then increment count 
		if (hash_pat[ord(string[j])] != 0 and
			hash_str[ord(string[j])] <=
			hash_pat[ord(string[j])]): 
			count += 1

		# if all the characters are matched 
		if count == len2: 
		
			# Try to minimize the window i.e., check if 
			# any character is occurring more no. of times 
			# than its occurrence in pattern, if yes 
			# then remove it from starting and also remove 
			# the useless characters. 
			while (hash_str[ord(string[start])] > 
				hash_pat[ord(string[start])] or
				hash_pat[ord(string[start])] == 0): 
			
				if (hash_str[ord(string[start])] > 
					hash_pat[ord(string[start])]): 
					hash_str[ord(string[start])] -= 1
				start += 1
			
			# update window size 
			len_window = j - start + 1
			if min_len > len_window: 
			
				min_len = len_window 
				start_index = start 

	# If no window found 
	if start_index == -1: 
		print("No such window exists") 
		return "" 
	
	# Return substring starting from 
	# start_index and length min_len 
	return string[start_index : start_index + min_len] 

#findSubString("PRWSOERIUSFK", "OSU")


# Q14. Write the Python program to count number of substrings from a
# given string of lowercase alphabets with exactly k distinct (given)
# characters?
# 
#     Input a string (lowercase alphabets): wolf
#     Input k: 4
#     Number of substrings with exactly 4 distinct characters: 1

# In[ ]:


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
print(count_k_dist(str1, k))


# Q15. Write the Python program to count number of substrings with same
# first and last characters of the given string?
# 
#     Input a string: abcd
#     4
# 

# In[21]:


def substring_with_equalEnds_Fun(sampleStr): 
	result = 0; 
	n = len(str1); 
	for i in range(n): 
		for j in range(i, n): 
			if (str1[i] == str1[j]): 
				result = result + 1
	return result 
sampleStr = input("Input a string: ")
print(substring_with_equalEnds_Fun(sampleStr))


# ## Great Job!
