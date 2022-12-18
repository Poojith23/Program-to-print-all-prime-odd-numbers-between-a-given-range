#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Program to print all prime odd numbers between a given range

start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

for num in range(start, end + 1):
   # prime numbers are greater than 1
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           if num % 2 != 0:
               print(num)

#Prime


# In[ ]:




