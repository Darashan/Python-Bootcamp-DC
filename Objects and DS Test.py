#!/usr/bin/env python
# coding: utf-8

# In[1]:


i = 11**2 - 1.75 + 9*1 - 56/2


# In[2]:


i


# In[3]:


4 * (6 + 5)


# In[4]:


4 * 6 + 5


# In[5]:


4 + 6 * 5


# In[6]:


type(3 + 1.5 + 4)


# In[8]:


9**0.5


# In[9]:


9**2


# In[10]:


s = 'hello'


# In[11]:


s[1]


# In[12]:


s[::-1]


# In[13]:


s[-1]


# In[14]:


s[4]


# In[15]:


list = [0,0,0]


# In[16]:


list


# In[18]:


list2 = [0]


# In[19]:


list2.append(0)


# In[20]:


list2.append(0)


# In[21]:


list2


# In[22]:


list3 = [1,2,[3,4,'hello']]


# In[23]:


list3[2][2] = 'goodbye'


# In[24]:


list3


# In[25]:


list4 = [5,3,4,6,1]


# In[27]:


list4.sort()


# In[28]:


list4


# In[29]:


d = {'simple_key':'hello'}


# In[30]:


d['simple_key']


# In[31]:


d = {'k1':{'k2':'hello'}}


# In[32]:


d['k1']['k2']


# In[33]:


d = {'k1':[{'nest_key':['this is deep',['hello']]}]}


# In[42]:


d['k1'][0]['nest_key'][1][0]


# In[43]:


d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}


# In[48]:


d['k1'][2]['k2'][1]['tough'][2][0]


# No we can't sort a dictionary because they are orderless.

# List is mutable, whereas a tuple is immutable.

# To create a tuple in Python, place all the elements in a () parenthesis, separated by commas.

# Unique thing about sets - There can only be one representative of the same object.

# In[49]:


list5 = [1,2,2,33,4,4,11,22,3,3,2]


# In[50]:


myset = set(list5)


# In[51]:


myset


# In[52]:


2 > 3


# In[53]:


3 <= 2


# In[54]:


3 == 2.0


# In[55]:


3.0 == 3


# In[56]:


4**0.5 != 2


# In[57]:


l_one = [1,2,[3,4]]
l_two = [1,2,{'k1':4}]


# In[58]:


l_one[2][0] >= l_two[2]['k1']


# In[ ]:




