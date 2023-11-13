f= open('/content/input1b2.txt','r')
out1b= open("output1b.txt",'w')

lines = f.readlines()
line1= lines[0].split(" ")
u= int(line1[0])
v=int(line1[1].strip())


graph=[[]]*(u+1)

for i in range(1,v+1):
  line= lines[i].split(" ")
  x,y,z = line
  if len(graph[int(x)])==0:
    graph[int(x)]=[(int(y),int(z))]
  else:
    graph[int(x)].append((int(y),int(z))) 

for i in range(u+1):
  print(i,':',*graph[i])
  print(i,':',*graph[i],file= out1b)

out1b.close()