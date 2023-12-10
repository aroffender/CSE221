from queue import PriorityQueue

inp = open('input2c.txt', 'r')
out = open("output2.txt", "w")
lines = inp.readlines()
line1 = lines[0].strip().split(' ')
nodes,edge = int(line1[0]),int(line1[1])
start = lines[-1].split()
d = {}

for line in lines[1:-1]:
  current_line = line.split()
  if int(current_line[0]) not in d:
    d[int(current_line[0])] = [(int(current_line[2]), int(current_line[1]))]
  else:
    d[int(current_line[0])] += [(int(current_line[2]), int(current_line[1]))]



def dijkstra(graph, start):
  pq = PriorityQueue()
  dists = [float('inf')] * (nodes + 1)
  dists[start] = 0
  vis = [False] * (nodes + 1)
  pq.put((0, start))
  vis[start] = True

  while not pq.empty():
    node = pq.get()
    if node[1] not in graph:
      continue
    else:
      for j in graph[node[1]]:
        temp = dists[node[1]] + j[0]
        if dists[j[1]] > temp:
          dists[j[1]] = temp
        if vis[j[1]] is not True:
          pq.put(j)
        vis[j[1]] = True

  for idx in range(len(dists)):
    if dists[idx]== float('inf'):
      dists[idx]= -1
  return dists

s1 = dijkstra(d, int(start[0]))
s2 = dijkstra(d, int(start[1]))

final= -1
shortest= float('inf')
dist = None

for n in range(1, nodes + 1):
  if s1[n] != -1 and s2[n] != -1:
    dist = max(s1[n], s2[n])
    if dist < shortest:
      shortest = dist
      final = n

if dist is None:
  print("Impossible")
  print("Impossible",file=out)

else:
  print("Time", shortest)
  print("Time", shortest,file=out)
  print("Node", final)
  print("Node", final,file=out)
  
out.close()
from queue import PriorityQueue

inp = open('input2c.txt', 'r')
out = open("output2.txt", "w")
lines = inp.readlines()
line1 = lines[0].strip().split(' ')
nodes,edge = int(line1[0]),int(line1[1])
start = lines[-1].split()
d = {}

for line in lines[1:-1]:
  current_line = line.split()
  if int(current_line[0]) not in d:
    d[int(current_line[0])] = [(int(current_line[2]), int(current_line[1]))]
  else:
    d[int(current_line[0])] += [(int(current_line[2]), int(current_line[1]))]



def dijkstra(graph, start):
  pq = PriorityQueue()
  dists = [float('inf')] * (nodes + 1)
  dists[start] = 0
  vis = [False] * (nodes + 1)
  pq.put((0, start))
  vis[start] = True

  while not pq.empty():
    node = pq.get()
    if node[1] not in graph:
      continue
    else:
      for j in graph[node[1]]:
        temp = dists[node[1]] + j[0]
        if dists[j[1]] > temp:
          dists[j[1]] = temp
        if vis[j[1]] is not True:
          pq.put(j)
        vis[j[1]] = True

  for idx in range(len(dists)):
    if dists[idx]== float('inf'):
      dists[idx]= -1
  return dists

s1 = dijkstra(d, int(start[0]))
s2 = dijkstra(d, int(start[1]))

final= -1
shortest= float('inf')
dist = None

for n in range(1, nodes + 1):
  if s1[n] != -1 and s2[n] != -1:
    dist = max(s1[n], s2[n])
    if dist < shortest:
      shortest = dist
      final = n

if dist is None:
  print("Impossible")
  print("Impossible",file=out)

else:
  print("Time", shortest)
  print("Time", shortest,file=out)
  print("Node", final)
  print("Node", final,file=out)
  
out.close()
