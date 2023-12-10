f = open('input1b.txt', 'r')
out = open('output1b.txt', 'w')
lines= f.readlines()
line1 = lines[0].strip().split(' ')
n,m = int(line1[0]),int(line1[1])

edges = []
for i in range(1,m+1):
  u, v = lines[i].strip().split(' ')
  edges.append((int(u), int(v)))

graph=[[] for _ in range(n + 1)]
for e in edges:
  u,v= e
  graph[u].append(v)

visd=[False]*(n+1)
visd[0]= True
incoming= [0] * (n+1)
queue= []

for i in range(len(graph)):
  for nb in graph[i]:
    incoming[nb] += 1

for node in range(1, n+1):
  if incoming[node]==0:
    queue.append(node)

res= []
while queue:
  node= queue.pop(0)
  res.append(node)
  visd[node] = True
  for nb in graph[node]:
    incoming[nb] -= 1
    if incoming[nb] == 0:
      queue.append(nb)


if False in visd:
  print("IMPOSSIBLE")
  print("IMPOSSIBLE",file=out)
else:
  print(*res)
  print(*res,file=out)

out.close()
