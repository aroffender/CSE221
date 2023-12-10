f = open('input1c.txt', 'r')
out = open('output1a.txt', 'w')
lines= f.readlines()
line1 = lines[0].strip().split(' ')
n,m = int(line1[0]),int(line1[1])

edges = []
for i in range(1,m+1):
  u, v = lines[i].strip().split(' ')
  edges.append((int(u), int(v)))

graph=[[] for _ in range(n + 1)]
for e in edges:
  u,v = e
  graph[u].append(v)

print(graph)
visd=[False] * (n + 1)
in_stack=[False]*(n + 1)
res=[]

def dfs(node):
  visd[node] = True
  in_stack[node] = True
  for nb in graph[node]:
    if in_stack[nb]:
      return False
    if not visd[nb]:
      if not dfs(nb):
        return False
  in_stack[node] = False
  res.append(node)
  return True

cycle = False
for node in range(1, n + 1):
  if not visd[node]:
    if not dfs(node):
      cycle = True

if cycle:
  print("IMPOSSIBLE")
  print("IMPOSSIBLE",file=out)
else:
  print(*res[::-1])
  print(*res[::-1],file=out)

out.close()

