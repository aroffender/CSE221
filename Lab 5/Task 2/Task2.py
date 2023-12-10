import heapq
f= open('input2c.txt','r')
out = open('ouput2.txt','w')
lines= f.readlines()
line1 = lines[0].strip().split(' ')
n,m = int(line1[0]),int(line1[1])

edges=[]
incoming = [0] * (n + 1)

for i in range(1,m+1):
  u,v = lines[i].strip().split(' ')
  edges.append((int(u), int(v)))

graph=[[] for _ in range(n + 1)]
for e in edges:
  u,v = e
  graph[u].append(v)
  incoming[v] += 1

prque=[]
for i in range(1, n + 1):
  if incoming[i] == 0:
    heapq.heappush(prque, i)

res= []
while prque:
  course = heapq.heappop(prque)
  res.append(course)
  for nb in graph[course]:
    incoming[nb]-= 1
    if incoming[nb]== 0:
      heapq.heappush(prque, nb)

if len(res)<n:
  print("IMPOSSIBLE")
  print("IMPOSSIBLE",file=out)
else:
  print(*res)
  print(*res,file=out)

out.close()
