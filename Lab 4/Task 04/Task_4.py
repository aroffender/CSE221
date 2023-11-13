f= open('/content/input4e.txt','r')
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
  stack = []
  for node in graph:
    if node not in visited:
      if Cyclefinder(graph, node, visited, stack):
        return True
  return False

def Cyclefinder(graph, node, visited, stack):
    visited.append(node)
    stack.append(node)
    for neighbor in graph[node]:
      if neighbor not in visited:
        if Cyclefinder(graph, neighbor, visited, stack):
          return True
      elif neighbor in stack:
        return True
    stack.remove(node)
    return False


if Cycleingraph(graph):
  print("YES")
  print("YES",file=out)
else:
  print("NO")
  print("NO",file=out)

out.close()

