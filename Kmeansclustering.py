#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as pyplot
import random

df = pd.DataFrame({
    'x':[12, 20,28,18,29,33,24,45,45,52,51,52,55,53,55,61,64,69,72],
    'y':[39,36,30,52,54,46,55,59,63,70,66,63,58,23,14,8,19,7,24]
})
print(df)


# In[2]:


x =0
val = input("number of clusters needed: ")
centroids =[]
for i in  range(0,int(val)):
    centroids.append([])
    
for i in range(0,int(val)):
    x =random.randint(0,18)
    centroids[i].append(df['x'][x])
    centroids[i].append(df['y'][x])
    
print(centroids)


# In[3]:


clusters=[]
for i in range(0,int(val)):
    clusters.append([])
#clusters[0].append(centroids[0])
#clusters[1].append(centroids[1])
#clusters[2].append(centroids[2])

print(clusters)


# In[4]:


import math
values=[]

def where(x,y):
    values=[]
    for i in range(0,int(val)):
        dist = (centroids[i][0]-x)*(centroids[i][0]-x)+(centroids[i][1]-y)*(centroids[i][1]-y)
        dist =math.sqrt(dist)
        values.append(dist)
        print(dist)
        
    z =min(values)
    print(values.index(z))
    
        
    return values.index(z)
        

         
         
   
    
    


# In[5]:


l =df.size/2
l


# In[6]:


point =[[]]
sumx =0
sumy =0
count =0
for i in range(0,int(l)):
    point =[[]]
    sumx=0
    sumy=0
    count =0
    z= where(df['x'][i],df['y'][i])
    point[0].append(df['x'][i])
    point[0].append(df['y'][i])            
    clusters[z].append(point[0])
    for j in clusters[z]:
        count = count+1
        sumy = sumy+j[1]
        sumx = sumx+j[0]
    centroids[z][0] =sumx/count
    centroids[z][1] =sumy/count
        
    


# In[7]:


print(centroids)


# In[8]:


for i in range(0,int(val)):
    print("cluster"+str(i)+" :")
    for j in clusters[i]:
        print(j)
        


# In[9]:


def distance(x,y,i):
    dist = (centroids[i][0]-x)*(centroids[i][0]-x)+(centroids[i][1]-y)*(centroids[i][1]-y)
    
    return dist
    


# In[10]:


sume =0
for i in range(0,int(val)):
    for j in clusters[i]:
        sume =sume+distance(j[0],j[1],i)
        
print("sum of squared sum for this classificationis :")
print(sume)


# In[ ]:




