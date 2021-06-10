#!/usr/bin/env python
# coding: utf-8

# # IMPORT LIBRARIES

# In[1]:

'''ALL THESE WORKS ARE DONE BY 

ANKITA SIKDER

STUDENT OF BTECH, IN UEMK

CONTACT NO.: 8583939774

EMAIL ID: ankita.sikder14@gmail.com'''
import numpy as np
np.array([1,2,3,4,5])


# In[3]:


a=[1,2,3,4,5]
a


# # TIMING CHECKING

# In[9]:


l1=[1,2,3]
l2=[3,4,5]
#we will create a list like [1*3,2*4,3*5]
get_ipython().run_line_magic('timeit', 'list(map(lambda x,y : x*y,l1,l2))')


# In[8]:


npA1=np.array([1,2,3])
npA2=np.array([3,4,5])
#we will create a list like [1*3,2*4,3*5]
get_ipython().run_line_magic('timeit', 'npA1*npA2')


# # NUMPY FUNDEMENTALS

# In[27]:


puku=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])


# In[28]:


puku


# In[29]:


puku.shape


# In[30]:


puku.dtype


# In[31]:


puku.ndim#According to list of list concept


# In[32]:


puli=np.arange(1,10)


# In[33]:


puli


# In[34]:


puli.dtype


# In[35]:


pylist=range(0,10)


# In[36]:


pylist


# In[37]:


puli


# In[39]:


chopechul=np.array([[1,0,0],[0,1,0],[0,0,1]])
chopechul


# In[42]:


chopechul=np.eye(5)


# In[43]:


chopechul


# In[45]:


chopechul.dtype


# In[46]:


chopechul.itemsize


# In[49]:


gurde=np.full((10,10),9)


# In[50]:


gurde


# In[51]:


gurde.shape


# In[52]:


#[v,v
# v,v
# v,v]
#(3,2)
v=[1,3,4]
np.tile(v,(3,2))


# In[53]:


puku


# In[54]:


puku.T


# In[59]:


np.linspace(1,50,10)


# # SLICING PART IN NUMPY

# In[60]:


puku


# In[61]:


puku[1,2]


# In[62]:


puku.shape


# In[65]:


puku2=puku.reshape(6,2)


# In[66]:


puku2.shape


# In[67]:


puku2


# In[68]:


puku[1]


# In[69]:


puku


# In[75]:


puli.shape


# In[77]:


puli[:,np.newaxis].shape


# In[78]:


puku[2]


# In[82]:


puku[puku>6]


# In[83]:


puku


# In[86]:


chaat=np.array([[1,0,4,0],[0,1,0,9],[0,0,1,6]])


# In[87]:


chaat


# In[88]:


np.vstack((puku,chaat))


# In[89]:


np.hstack((puku,chaat))


# # MATHEMATICAL PART AND 
# # LINEAR ALGEBRA

# In[90]:


puku


# In[91]:


np.sin(puku)


# In[92]:


np.cos(puku)


# In[93]:


np.median(puku)


# In[94]:


np.exp(puku)


# In[95]:


puku


# In[99]:


sm=np.array([[1,2,9],[4,5,6],[7,8,9]])
sm


# In[100]:


np.linalg.det(sm)


# In[101]:


np.linalg.inv(sm)


# In[102]:


np.linalg.eig(sm)


# In[103]:


sm


# In[104]:


sm2=np.array([[1,2,9],[4,5,6],[7,8,9]])


# In[2]:


laora=np.dot(sm,sm2)


# In[109]:


laora.argmax()#REturn Index OF Maximum Value of A matrix


# In[118]:


puli2=np.array([1,5,9,7,820,58,96,5,2,4])
puli2


# In[122]:


np.sort(puli2)#Sorting Numpy Array


# In[110]:


laora


# In[111]:


laora.sum(axis=0)


# In[115]:


laora.sum(axis=1)


# In[114]:


#MATRIX MULTIPLICATION
import numpy as np
r1=int(input("Enter the no of rows of 1st matrix :: "))
c1=int(input("Enter the no of columns of 1st matrix :: "))
r2=int(input("Enter the no of rows of 2nd matrix :: "))
c2=int(input("Enter the no of columns of 2nd matrix :: "))
print("Enter the {} entries in a Matrix 1 (separated by space): ".format(r1*c1)) 
entries1 = list(map(int, input().split())) 
matrix1=np.array(entries1).reshape(r1,c1)
print("Enter the {} entries in a Matrix 2 (separated by space): ".format(r2*c2)) 
entries2 = list(map(int, input().split())) 
matrix2=np.array(entries2).reshape(r2,c2)
print("MATRIX-1: \n",matrix1)
print("MATRIX-2: \n",matrix2)
mulmat=np.dot(matrix1,matrix2)
print(mulmat)


# # HAPPY CODING -- NUMPY FINISHED

# In[ ]:




