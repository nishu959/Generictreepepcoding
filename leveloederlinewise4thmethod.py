class Tree():
  def __init__(self, data ):
    self.data = data
    self.child = []
 
class pair():
  def __init__(self, node, level):
    self.node = node
    self.level = level
  
   
root = None
l = []
m = int(input())
n = list(map(int, input().split()))

for i in n:
  if(i==-1):
    l.pop()
  else:
    p = Tree(i)
    if(len(l)>0):
      l[-1].child.append(p)
    else:
      root = p
    l.append(p)

def fun(root):
  s = []
  level = 0
  p = pair(root, level)
  s.append(p)
  
  while(len(s)>0):
    a =s.pop(0)
    if(a.level>level):
      level = a.level
      print()
    print(a.node.data, end = " ")
     
    for i in a.node.child:
      s.append(pair(i,level+1))
  
    
fun(root)