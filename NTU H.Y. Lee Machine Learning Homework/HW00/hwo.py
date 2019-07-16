#!/usr/bin/env python
# coding: utf-8

# In[1]:


f = open('hw0_data.dat')


# In[2]:


f = open('hw0_data.dat')
f.redaline()


# In[3]:


f = open('hw0_data.dat')
f.readline()


# In[11]:


f = open('hw0_data.dat')
s1=f.readline()
s2=f.readline()
print(s1)
print(s2)


# In[21]:


import pandas as np
f = open('hw0_data.dat')
*s1=f.readline()
*s2=f.readline()
*print(s1)
*print(s2)
array = np.array(f).astype(float)
for i in range(0, 500, 1):
     s1 = array[i]
     


# In[30]:


f = open('hw0_data.dat')
s1=f.readline()
s2=f.readline()
print(s1)
print(s2)


# In[38]:


import pandas as pd
import numpy as np

f = open('hw0_data.dat')
s1=f.readline()
s2=f.readline()
print(s1)
print(s2)

array = np.array(f).astype(float)

x_list = []

for i in range(0, 500, 1):
        for j in range(24-9):
            mat = array[i:i+18, j:j+9]
            label = array[i] # 第10行是PM2.5
            x_list.append(mat)
            y_list.append(label)
            
x = np.array(x_list)            


# In[39]:


f = open('hw0_data.dat')
s1=f.readline()
s2=f.readline()
print(s1)
print(s2)
import numpy as np


# In[43]:


import numpy as np

f = open('hw0_data.dat')
s1=f.readline()
s2=f.readline()
print(s1)
print(s2)

array = np.arange(f)
array2[2,1]


# In[45]:


import numpy as np

f = open('hw0_data.dat')
s1=f.readline()
s2=f.readline()
print(s1)
print(s2)

array = np.array(f)
print(array)


# In[47]:


f=open("hw0_data.dat")

target=1
answers=[]

for line in f:
    n=line.split()
    index=target-1
    answers.append(n[index])
    
answers.sort()
print(answers)

output="ans1.txt"
f=open(output, 'w')
f.write(str(answers))
f.close()


# In[50]:


import PIL
pil_color_image = PIL.Image.open("The Grand Budapest Hotel.jpg")


# In[ ]:





# In[53]:


import PIL
pil_color_image = PIL.open("The Grand Budapest Hotel.jpg")


# In[52]:


import PIL


# In[56]:


from PIL import Image
im=Image.open('The Grand Budapest Hotel.jpg')
im.show()


# In[60]:


from PIL import Image
im=Image.open('Lena.png')
#im.show()

rotated=im.rotate(45)
rotated.show()


# In[66]:


from PIL import Image
im=Image.open('Lena.png')

im.transpose(Image.FLIP_LEFT_RIGHT).transpose(Image.FLIP_TOP_BOTTOM)
im.show()


# In[70]:


from PIL import Image
im=Image.open('Lena.png')

output = im.transpose(Image.FLIP_LEFT_RIGHT).transpose(Image.FLIP_TOP_BOTTOM)
output.show()
output.save('ans2.png')


# In[ ]:




