#!/usr/bin/env python
# coding: utf-8

# In[3]:


def add_numbers(x,y,z):
    a = x + y
    b = x + z
    c = y + z
    print(a,b,c)


# In[6]:


add_numbers(10,20,30)


# In[8]:


def square(x):
    y=x**2
    return y


# In[9]:


result=square(4)
print(result)


# In[14]:


def loop_five(x):
    for x in range(0,25):
        print(x)
        if x==5:
            return
        print("this line will not execute.")


# In[17]:


loop_five(26)


# In[18]:


def hello():
    print("hello,world")


# In[19]:


hello()


# In[23]:


monika=60
if monika >= 65:
    print ("monika is pass")
else:
        print("monika is failed")


# In[24]:


monika=a
if monika >= 65:                           exception handling
    print ("monika is pass")
else:
        print("monika is failed")


# In[25]:


x=15
if x>10:
     raise Exception("x should not exceed 10. the value of x was: {}" .format(x))


# In[27]:


try:
    print(1/0)
except ZeroDivisionError:
    print("you cant divide by zero,you're silly")


# In[29]:


try:
    x=2+5
except:
        print("it dosent work!")
else:
    print('will run when no exception',x)


# In[32]:


lamb = lambda x:x**5


# In[34]:


print(lamb(5))


# In[35]:


double= lambda x: x*6


# In[36]:


print(double(5))


# In[37]:


def f(x,c,v):
    f(x+c+v)


# In[40]:


print(f(2,4,5))

