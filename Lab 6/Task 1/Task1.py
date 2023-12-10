import heapq
f = open("input1b.txt", "r")
out = open("output1.txt", "w")

lines= f.readlines()
line1 = lines[0].strip().split(' ')
n,m = int(line1[0]),int(line1[1])

alist= {}
for i in range(0, n + 1):
  alist[i] = []

for j in range(1,m):
  line= lines[j].strip().split(' ')
  a=int(line[0])
  b=int(line[1])
  c=int(line[2])
  alist[a].append((b, c))

start=int(lines[-1].strip())

def Dijkstra(graph, start):
  dist = {node: float('inf') for node in graph}
  dist[start] = 0
  pque =[(0,start)]
  while pque:
    cdist,cnode = heapq.heappop(pque)
    if cdist > dist[cnode]:
      continue
    for nb, weight in graph[cnode]:
      newdist= cdist + weight
      if newdist < dist[nb]:
        dist[nb]=newdist
        heapq.heappush(pque,(newdist, nb))
  return dist

shortest= Dijkstra(alist,start)
nodes=[]
for k,v in shortest.items():
  if v==float('inf'):
    v=-1
  nodes.append(v)

print(*nodes[1:])
print(*nodes[1:],file=out)
out.close()
import heapq
f = open("input1b.txt", "r")
out = open("output1.txt", "w")

lines= f.readlines()
line1 = lines[0].strip().split(' ')
n,m = int(line1[0]),int(line1[1])

alist= {}
for i in range(0, n + 1):
  alist[i] = []

for j in range(1,m):
  line= lines[j].strip().split(' ')
  a=int(line[0])
  b=int(line[1])
  c=int(line[2])
  alist[a].append((b, c))

start=int(lines[-1].strip())

def Dijkstra(graph, start):
  dist = {node: float('inf') for node in graph}
  dist[start] = 0
  pque =[(0,start)]
  while pque:
    cdist,cnode = heapq.heappop(pque)
    if cdist > dist[cnode]:
      continue
    for nb, weight in graph[cnode]:
      newdist= cdist + weight
      if newdist < dist[nb]:
        dist[nb]=newdist
        heapq.heappush(pque,(newdist, nb))
  return dist

shortest= Dijkstra(alist,start)
nodes=[]
for k,v in shortest.items():
  if v==float('inf'):
    v=-1
  nodes.append(v)

print(*nodes[1:])
print(*nodes[1:],file=out)
out.close()
