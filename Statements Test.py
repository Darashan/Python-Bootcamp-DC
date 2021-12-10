#!/usr/bin/env python
# coding: utf-8

# Use for, .split(), and if to create a Statement that will print out words that start with 's':

# In[ ]:


st = 'Print only the words that start with s in this sentence'


# In[7]:


for x in st.split():
    if x[0] == 's':
        print(x)


# Use range() to print all the even numbers from 0 to 10.

# In[9]:


for x in range(0,10):
    if x%2 == 0:
        print(x)


# Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.

# In[10]:


mylist = [x for x in range(0,50) if x%3 == 0]


# In[11]:


mylist


# Go through the string below and if the length of a word is even print "even!"

# In[12]:


st = 'Print every word in this sentence that has an even number of letters'


# In[27]:


for x in st.split():
    if len(x)%2 ==0:
        print(x + " has even number of letters!")


# Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz" instead of the number, and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".

# In[25]:


for num in range(1,101):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)


# Use List Comprehension to create a list of the first letters of every word in the string below:

# In[18]:


st = 'Create a list of the first letters of every word in this string'


# In[20]:


firsts = [x[0] for x in st.split()] 


# In[21]:


firsts

