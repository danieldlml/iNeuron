#!/usr/bin/env python
# coding: utf-8

# 1. Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included). The numbers obtained should be printed in a comma-separated sequence on a single line. 

# In[12]:


# Initialize the empty list
lstNum=[]
#iterate the numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included, so max value is 3201 in range)
for num in range (2000,3201):
    if(num%7 == 0) and (num%5 != 0):
        lstNum.append(str(num))
# Print the output of the logic.
print(','.join(lstNum))


# 2. Write a Python program to accept the user's first and last name and then getting them printed in the the reverse order with a space between first name and last name

# In[13]:


#Input the First Name
firstName  = input('Input your First Name: ')
#Input the Last Name
lastName  = input('Input your Last Name: ')
#Print the reverse order with a space between First Name and Last Name
print(lastName +" "+firstName)


# 3.Write a Python program to find the volume of a sphere with diameter 12 cm.  
#  
# Formula: V=4/3 * π * r 3 

# In[15]:


#Initialiaze the variables of radius, π
rad = 12.0
piVal = 3.1415926535897931
# Formula for the Volume of Sphere
volSphere = 4.0/3.0*piVal* rad**3
#Print the Volume of the Sphere
print('The Volume of the Sphere is : ',volSphere,'cm cube (Units)')


# 4.Write a program which accepts a sequence of comma-separated numbers from console and generate a list. 

# In[16]:


#Console for Comma-Separated numbers 
vals = input("Input some Comma-Separated numbers : ")
#Splitting thru comma (,)
listCsn = vals.split(",")
#Print Sequence of Comma-Separated numbers
print('List : ',listCsn)

5. Create the below pattern using nested for loop in Python. 
 
 
*  
* *  
* * * 
* * * *  
* * * * *  
* * * *  
* * *  
* *  
* 
 
 
# In[17]:


#Input for the number of STARS(*) to be displayed on single line like Symmetric
rowsNum = input("Enter max number of STARS(*) to be displayed on single line : ")
#Typecast the value to int
rowsNum = int (rowsNum)
#To print upper partition
for a in range (0, rowsNum):
    for b in range(0, a + 1):
        print("*", end=' ')
    print("\r")
#To print lower  partition
for a in range (rowsNum, 0, -1):
    for b in range(0, a -1):
        print("*", end=' ')
    print("\r")


# 6. Write a Python program to reverse a word after accepting the input from the user. 
#  
# Sample Output: 
#  
# Input word: iNeuron 
#  
# Output: norueNi

# In[18]:


#Input the word to reverse
wordRev = input("Input a word to reverse : ")
#Logic to reverse the word
for char in range(len(wordRev) - 1, -1, -1):
  print(wordRev[char], end="")
print("\n")


# 7. Write a Python Program to print the given string in the format specified in the ​sample output. 
#  WE, THE PEOPLE OF INDIA, having solemnly resolved to constitute India into a SOVEREIGN, SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC and to secure to all its citizens 
#  
# Sample Output: 
#  
# WE, THE PEOPLE OF INDIA,   having solemnly resolved to constitute India into a SOVEREIGN, !  SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC    and to secure to all its citizens 

# In[19]:


#Initialiaze the strings of the Sentence
str1 = 'We, the people of india'
str2 = 'having solemnly resolved to constitute India into a'
str3 = 'sovereign, {} socialist, secular, democratic republic'
str4 = 'and to secure to all its citizens'
#Print the required format of the sentence.
print(str1.upper()+', '+str2+' '+str3.upper().format('! ')+' '+str4)


# Note : - NOTE:​ ​The​ ​solution​ ​shared​ ​through​ ​Github​ ​should​ ​contain​ ​the​ ​source code​ ​used​ ​ and​  ​the​ ​output

# In[ ]:




