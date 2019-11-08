import pandas as pd
import numpy as np
import math
col_names = ['outlook','temperature','humidity','windy','play']
df = pd.read_csv("climate.csv",header=None, names=col_names)
print(df)
df1 =df[['play']].to_numpy()
#print(df1)
y=0
n =0
for i in df1:
    if(i == "no"):
        n = n+1
    if(i == "yes"):
        y =y+1

t =n+y
print("probability of no is :")
print(n/t)
print("probability of yes is :")
print(y/t)
values =[]

val1 =input("outlook is :")
val2 =input("temperature is :")
val3 =input("humidity is :")
val4 =input("windy is :")
values.append(val1)
values.append(val2)
values.append(val3)
values.append(val4)

#calculating p(x/yes)
k =0
sumv=0
prod =1
for i in df:
    if(i=="play"):
        break
    else:
        for j in range(0,t):
            if((df[i][j] == values[k])&(df['play'][j]=="yes")):
                sumv = sumv+1
            
    prod =prod*(sumv/y)
    sumv =0
    k =k+1

prod =prod*(y/t)
print("probability of x/yes")
print(prod)
x=[]
x.append(prod)

#calculating p(x/no)
k =0
sumv=0
prod =1
for i in df:
    if(i=="play"):
        break
    else:
        for j in range(0,t):
            if((df[i][j] == values[k])&(df['play'][j]=="no")):
                sumv = sumv+1
            
    prod =prod*(sumv/y)
    sumv =0
    k =k+1

prod =prod*(n/t)
print("probability of x/no")
print(prod)
x.append(prod)

if(x[0]>x[1]):
    print("you can play")
else:
    print("you can't play outside")



