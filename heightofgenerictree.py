class Tree():
  def __init__(self, data):
    self.data = data
    self.child = []
   
m = int(input())
ip = list(map(int, input().split()))
l = []


for i in ip:
  if(i==-1):
    l.pop()
  else:
    node = Tree(i)
    if(len(l)==0):
      root = node
    else:
      l[-1].child.append(node)
    l.append(node)
   
  
def heightoftree(root):
  ht = -1
  for i in root.child:
    p = heightoftree(i)
    ht = max(p, ht)
  ht += 1
  return ht
 

print(heightoftree(root))