f= open('/content/input6c.txt','r')
out=open('output6.txt','w')
lines = f.readlines()
line1= lines[0].split(" ")
r= int(line1[0])
h=int(line1[1].strip())
max_dcount = 0

visited =[[False]*h for i in range(r)]
graph=[]
for i in range(1,r+1):
  x= list(lines[i].strip())
  graph.append(x)

def search(graph,visited,r,c):
  if  r<0 or r>=len(graph) or c<0 or c>=len(graph[0]):
    return 0
  if visited[r][c] or graph[r][c] == '#':
    return 0

  dcount=0
  if graph[r][c]=="D":
    dcount+=1

    
  visited[r][c] = True
  dcount+= search(graph, visited, r + 1, c)
  dcount+= search(graph, visited, r - 1, c)
  dcount+= search(graph, visited, r, c + 1)
  dcount+= search(graph, visited, r, c - 1)
  return dcount

def findmax(x,y):
  if x>y:
    return x
  else:
    return y
  
for i in range(r*h):
  i, j = divmod(i, h)
  if graph[i][j]=='.':    
    dcount = search(graph,visited,i,j)
    max_dcount= findmax(max_dcount,dcount)

print(max_dcount)
print(max_dcount,file=out)
out.close()



