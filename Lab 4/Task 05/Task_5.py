f= open('/content/input5a.txt','r')
out=open('output5.txt','w')
lines = f.readlines()
line1= lines[0].split(" ")
u= int(line1[0])
v=int(line1[1])
destination= int(line1[2].strip())


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


def pathfinder(graph, st, dest):
  visited = []
  que = [[st]]
  if st == dest:
    print("Time: 0")
    print("Shortest path: 1")
    return	

  while que:
    npath = que.pop(0)
    node = npath[-1]
    if node not in visited:
      adjs = graph[node]
      for adj in adjs:
        shortpath = list(npath)
        shortpath.append(adj)
        que.append(shortpath)
        if adj == dest:
          print("Time:",len(shortpath)-1)
          print("Time:",len(shortpath)-1,file=out)
          print("Shortest path:", *shortpath)
          print("Shortest path:", *shortpath,file=out)
          return
  visited.append(node)

pathfinder(graph,1, destination)

out.close()