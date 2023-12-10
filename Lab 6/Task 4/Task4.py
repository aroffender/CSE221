f=open("/content/input4a.txt", "r")
out=open("output4.txt", "w")
lines = f.readlines()
line1 = lines[0].strip().split(' ')
ct,road = int(line1[0]),int(line1[1])
roads=[]

for line in lines[1:]:
  roads.append([int(x) for x in line.split()])

class disjset:
  def __init__(self, n):
    self.parent= list(range(n))
    self.state=[0] * n

  def pfinder(self, c):
    if self.parent[c] != c:
      self.parent[c] = self.pfinder(self.parent[c])
    return self.parent[c]

  def union(self, x, y):
    a= self.pfinder(x)
    b= self.pfinder(y)
    if a!=b:
      if self.state[a] < self.state[b]:
        self.parent[a] = b
      elif self.state[a] > self.state[b]:
        self.parent[b] = a
      else:
        self.parent[a] = b
        self.state[b] += 1

def mincost(n,m,roads):
  roads.sort(key=lambda x:x[2])
  dsunion= disjset(n)
  fcost = 0
  included_edges = 0

  for r in roads:
    u, v, w = r
    if dsunion.pfinder(u-1) != dsunion.pfinder(v-1):
      dsunion.union(u-1, v-1)
      included_edges += 1
      fcost += w
    if included_edges == n - 1:
      break
  return fcost
  
rescost= mincost(ct,road, roads)
print(rescost)
print(rescost,file=out)
out.close()