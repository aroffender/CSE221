# -*- coding: utf-8 -*-
"""task_4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1dSOtAjXkhV5R50ma-XwKcUgeBg4thR84#scrollTo=9hnbXr8UzGAp&uniqifier=3
"""
f = open('/content/input4b.txt','r')
out= open('output4.txt','w')
lines= f.readlines()
n= int(lines[0])
arr= lines[1].split(' ')
for i in range(len(arr)-1):
  x=int(arr[i])
  arr[i]=x

max=-9999
i=1
j=2
while i<j and j<=n:
  val= arr[i-1]+arr[j-1]**2
  if j==n:
    i+=1
    j=i+1
  else:
    j+=1
  if max<val:
    max = val

print(max)