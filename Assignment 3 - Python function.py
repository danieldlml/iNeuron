#!/usr/bin/env python
# coding: utf-8

# ## Problem Statement

# Q.1 Write a function to compute 5/0 and use try/except to catch the exceptions.

# In[1]:


def divZeroFun(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return 0
    
#divZeroFun(8,4)
divZeroFun(8,0)


# Q.2 Implement a Python program to generate all sentences where subject is in ["Americans",
# "Indians"] and verb is in ["Play", "watch"] and the object is in ["Baseball","cricket"].
# 
#     Hint: Subject,Verb and Object should be declared in the program as shown below.
#     subjects=["Americans ","Indians"]
#     verbs=["play","watch"]
#     objects=["Baseball","Cricket"]
# 
#     Output should come as below:
#     Americans play Baseball.
#     Americans play Cricket.
#     Americans watch Baseball.
#     Americans watch Cricket.
#     Indians play Baseball.
#     Indians play Cricket.
#     Indians watch Baseball.
#     Indians watch Cricket.

# In[2]:


subject=["Americans", "Indians"]
verb=["Play", "watch"]
obj=["Baseball","cricket"]

# Use list comprehension instead of looping over each of the predicates
sen_list = [(sb+" "+ vb + " " + ob) for sb in subject for vb in verb for ob in obj]
for sen in sen_list:
 print (sen)


# Q.3 Write a function so that the columns of the output matrix are powers of the input vector.
# The order of the powers is determined by the increasing boolean argument. Specifically, when
# increasing is False, the i-th output column is the input vector raised element-wise to the power
# of N - i - 1.
# 
#     HINT: Such a matrix with a geometric progression in each row is named for Alexandre Theophile Vandermonde.

# In[7]:



#Python method to display the matrix with a geometric progression in each row (Alexandre Theophile Vandermonde)
import numpy as np

def gen_vandermonde_matrix_fun(ip_vector, n, increasing=False):
    
    if not increasing:
        op_matx = np.array([x**(n-1-i) for x in ip_vector for i in range(n)]).reshape(ip_vector.size,n)
        
    elif increasing:
        op_matx = np.array([x**i for x in ip_vector for i in range(n)]).reshape(ip_vector.size,n)
    
    return op_matx

ip_vector = np.array([0,2,4,6,8])
columns_num_op = 4
matrix_dec_ordr_op = gen_vandermonde_matrix_fun(ip_vector,columns_num_op,False)
matrix_asc_ordr_op = gen_vandermonde_matrix_fun(ip_vector,columns_num_op,True)

print("The Input Array is:",ip_vector,"\n")
print("Number of Columns in Output Matrix is:",columns_num_op,"\n")
print("Alexandre Theophile Vandermonde Matrix in Decreasing Order Of Powers :\n\n",matrix_dec_ordr_op,"\n")
print("Alexandre Theophile Vandermonde matrix in Increasing Order Of Powers :\n\n",matrix_asc_ordr_op,"\n")


# In[ ]:




