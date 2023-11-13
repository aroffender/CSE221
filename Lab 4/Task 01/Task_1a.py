f= open('/content/input1a2.txt','r')
out1a=open('output1a.txt','w')

lines= f.readlines()
line1 = lines[0].strip().split(' ')
v,e = int(line1[0]),int(line1[1])

graph=[]
for i in range(v+1):
  lis= [0]*(v+1)
  graph.append(lis)

for i in range(1,v):
  line=lines[i].strip().split(' ')
  a,b,c = int(line[0]),int(line[1]),int(line[2])
  graph[a][b]=c

for i in graph:
  print(*i)
  print(*i,file=out1a)

out1a.close()




