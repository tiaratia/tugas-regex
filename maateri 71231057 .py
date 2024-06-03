#!/usr/bin/env python
# coding: utf-8

# In[4]:


s = 'foo123bar'
'123' in s
True


# In[3]:


s = 'foo123bar'
s.find('123')
3
s.index('123')
3


# In[11]:


pattern = r"Cookie"
sequence = "Cookie"
if re.match(pattern, sequence):
    print("Match!")
else: print("Not a match!")


# In[ ]:





# In[ ]:




