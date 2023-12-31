# -*- coding: utf-8 -*-
"""task_6.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1dSOtAjXkhV5R50ma-XwKcUgeBg4thR84#scrollTo=9hnbXr8UzGAp&uniqifier=3
"""
f = open('/content/input6a.txt','r')
out= open('output6.txt','w')
lines= f.readlines()
n= int(lines[0].split(' ')[0])
q = int(lines[2].split(' ')[0])

arr= lines[1].split(' ')
for i in range(len(arr)):
  x=int(arr[i])
  arr[i]=x


def Partition(arr, start, end):
  pivot = arr[end]
  i = start - 1
  for j in range(start, end):
    if arr[j] < pivot:
      i = i + 1
      (arr[i], arr[j]) = (arr[j], arr[i])
  (arr[i + 1], arr[end]) = (arr[end], arr[i + 1])
  return i + 1

def smallestk(arr, start, end, K):
  if (K > 0 and K <= end + 1):
    parti = Partition(arr, start, end)
    if parti == K - 1:
      return arr[parti]
    elif parti > K - 1:
      return smallestk(arr, start, parti-1, K)
    else:
      return smallestk(arr, parti + 1, end, K)
  else:
    return min(arr) -1

for i in range(q):
  x= lines[3+i]
  k=int(x)
  elem=smallestk(arr,0,len(arr)-1,k)
  print(elem,file=out)
  print(elem)