# -*- coding: utf-8 -*-
"""task_1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1o5e3kEhOSQ2aEC5xUYyr0I9fe1SnYrn5

#1(a)
"""

file= open('/content/input1a.txt','r')
out = open('output1a.txt','w')
var= file.readlines()
n= int(var[0])

for i in range(1,n):
  if int(var[i])%2==0:
    print(f'{int(var[i])} is even',file = out)
  else:
    print(f'{int(var[i])} is odd',file = out)

out.close()

#1(b)

file2= open('/content/input1b.txt','r')
out = open("output1b.txt",'w')

f = file2.readlines()
n= int(f[0])
for i in range(1,n):
  x= f[i].split(' ')

  if x[2]== "+":
    a=int(x[1])
    b=int(x[3])
    ans= a + b
    print(f'The result of {a}{x[2]}{b} is  {ans}',file =out)

  elif x[2]== "-":
    a=int(x[1])
    b=int(x[3])
    ans= a - b
    print(f'The result of {a}{x[2]}{b} is  {ans}',file =out)
  elif x[2]== "*":
    a=int(x[1])
    b=int(x[3])
    ans= a * b
    print(f'The result of {a}{x[2]}{b} is  {ans}',file =out)
  elif x[2]== "/":
    a=int(x[1])
    b=int(x[3])
    ans= a / b
    print(f'The result of {a}{x[2]}{b} is {ans}',file =out)

out.close()
