f= open('input3c.txt','r')
out= open('output3.txt','w')
lines= f.readlines()
line1= lines[0].strip().split(' ')
n,m= int(line1[0]),int(line1[1])
edges=[]
incoming= [0]*(n + 1)

for i in range(1,m+1):
  u,v = lines[i].strip().split(' ')
  edges.append((int(u), int(v)))

inv= [[] for _ in range(n + 1)]
graph=[[] for _ in range(n + 1)]
for e in edges:
  u,v= e
  graph[u].append(v)
  inv[v].append(u)


vistd= [False]*(n + 1)
stack= []
def dfs(node, graph, vistd, stack):
  vistd[node] = True
  for nb in graph[node]:
    if not vistd[nb]:
      dfs(nb, graph, vistd, stack)
  stack.append(node)

def sccfinder(node, inv, vistd, comps):
  vistd[node]= True
  comps.append(node)
  for nb in inv[node]:
    if vistd[nb]==False:
      sccfinder(nb, inv, vistd, comps)


for node in range(1, n + 1):
  if not vistd[node]:
    dfs(node, graph, vistd, stack)

vistd=[False]*(n + 1)
scc=[]
while stack:
  node= stack.pop()
  if not vistd[node]:
    comps= []
    sccfinder(node,inv,vistd,comps)
    scc.append(comps)


for i in scc:
  print(*i)
  print(*i,file=out)

out.close()