f= open('/content/input4d.txt','r')
out=open('output4.txt','w')
lines = f.readlines()
line1= lines[0].split(" ")
u= int(line1[0])
v=int(line1[1].strip())
arr=[[]]*(u+1)

for i in range(1,v+1):
  line= lines[i].split(" ")
  x,y = line
  if len(arr[int(x)])==0:
    arr[int(x)]=[int(y)]
  else:
    arr[int(x)].append(int(y)) 

graph={}
for i in range(u+1):
  graph[i]=arr[i]


def Cycleingraph(graph):
  visited = []
  que = []
  for node in graph:
    if node not in visited:
      if Cyclefinder(graph, node, visited, que):
        return True
  return False

def Cyclefinder(graph, node, visited, que):
    visited.append(node)
    que.append(node)
    for neighbor in graph[node]:
      if neighbor not in visited:
        if Cyclefinder(graph, neighbor, visited, que):
          return True
      elif neighbor in que:
        return True
    que.remove(node)
    return False


if Cycleingraph(graph):
  print("YES")
  print("YES",file=out)
else:
  print("NO")
  print("NO",file=out)

out.close()