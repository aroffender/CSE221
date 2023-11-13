f= open('/content/input2c.txt','r')
out=open('output2.txt','w')
lines = f.readlines()
line1= lines[0].split(" ")
u= int(line1[0])
v=int(line1[1].strip())
graph=[[]]*(u+1)

for i in range(1,v+1):
  line= lines[i].split(" ")
  x,y = line
  if len(graph[int(x)])==0:
    graph[int(x)]=[int(y)]
  else:
    graph[int(x)].append(int(y)) 


def Bfs(graph, st):
  que = [st]
  visited = []
  res = []
  while que:
    node = que.pop(0)
    if node not in visited:
      visited.append(node)
      res.append(node)
      for adj in graph[node]:
        if adj not in visited:
          que.append(adj)
  return res

print(*Bfs(graph, 1))
print(*Bfs(graph, 1),file=out)
out.close()



