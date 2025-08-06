#!/usr/bin/env python
# coding: utf-8

# # Image Processing Course for Absolute Beginners - Experiment 1

# In[10]:


import cv2
import matplotlib.pyplot as plt
from matplotlib.pyplot import *
from numpy import *


# ## 1) Displaying an Image using CV2

# In[11]:


img = cv2.imread(r"C:\Users\mpstme.student\Downloads\Cameraman.png")
plt.imshow(img)


# In[12]:


img.shape


# ## 2) Display Image using mathplotlib

# In[13]:


plt.imshow(img, cmap = 'gray')
plt.title('Original Image')
plt.show()


# ## 3) Down Scaling Image

# In[14]:


f = 2
(m,n,_) = img.shape
imgNew = zeros((m//f,n//f), dtype = int)

for i in range (m):
    for j in range(n):
        imgNew[i//f,j//f] = img[i,j,0]


# In[15]:


plt.imshow(imgNew, cmap = 'gray')
plt.title('Downscaled Image')
plt.show()


# In[16]:


imgNew.shape


# In[52]:


#Different method using cv2 library
img_shrinked = cv2.resize(img, (226//2,226//2)) 
plt.imshow(img_shrinked)
img_shrinked.shape


# ## 4) Upscaling Image

# In[18]:


f=2
(m,n,_) = img.shape
imgNew2=zeros((m*f,n*f),dtype= int)
for i in range(0, m*f):
  for j in range(0, n*f):
    imgNew2[i,j] = img[i//f,j//f, 0]


# In[19]:


plt.imshow(imgNew2, cmap = 'gray')
plt.title('Upscaling Image')
plt.show()


# In[51]:


imgNew2.shape


# In[53]:


#Different method using cv2 library
img_upscaled = cv2.resize(img, (226*2,226*2)) 
plt.imshow(img_upscaled)
img_upscaled.shape


# ## 5)  Bit Depth on Image Quality Bit Depth on Image Quality

# In[26]:


img.shape


# In[25]:


img.max()


# In[21]:


bits = int(input("Enter number of bits for image: "))


# In[27]:


maxoriginal = 226
maxnew = 2**bits
factor = (maxnew-1)/(maxoriginal-1)
factor


# In[48]:


imgNew2=np.zeros((m,n))
for i in range(m):
    for j in range(n):
        imgNew2[i,j]=factor*img[i,j,0]


# In[49]:


imgNew2.max()


# ## 6) Grayscaling

# In[50]:


imshow(imgNew2,cmap='gray')

