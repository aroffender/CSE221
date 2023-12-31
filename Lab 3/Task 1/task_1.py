# -*- coding: utf-8 -*-
"""task_1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1dSOtAjXkhV5R50ma-XwKcUgeBg4thR84#scrollTo=9hnbXr8UzGAp&uniqifier=3
"""
f = open('/content/input1a.txt','r')
out= open('output1.txt','w')
lines= f.readlines()
n= int(lines[0])
arr= lines[1].split(' ')
for i in range(len(arr)):
  x=int(arr[i])
  arr[i]=x


def merge(a,b):
  c=[0]*(len(a)+len(b))
  i,j=0,0
  for k in range(len(a)+len(b)):
    if i<len(a) and j<len(b):
      if a[i]<b[j]:
        c[k]= a[i]
        i+=1
      else:
        c[k]=b[j]
        j+=1
    else:
      if i<len(a):
        c[k]=a[i]
        i+=1
      elif j<len(b):
        c[k]=b[j]
        j+=1
  return c

def mergeSort(arr):
  if len(arr) <= 1:
    return arr
  else:
    mid = len(arr)//2
    a1 = mergeSort(arr[:mid])
    a2 = mergeSort(arr[mid:])
    a=merge(a1, a2)
    return(a)

res = mergeSort(arr)
for i in res:
  print(i,end=' ')
  print(i,end=' ',file=out)

out.close()