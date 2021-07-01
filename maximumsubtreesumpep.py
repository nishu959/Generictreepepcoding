import sys 

class Tree():
  def __init__(self, data ):
    self.data = data
    self.child = []
 


m = int(input())
n = list(map(int, input().split()))


def treeform(n, l, root):
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
  return root
   


root = treeform(n, [], None)
msn = None

ms = -1 * sys.maxsize


def maxsubtree(root):
  s = 0
  global ms, msn
  for i in root.child:
    cs = maxsubtree(i)
    s += cs
  s += root.data
  if(s>ms):
    ms = s
    msn = root.data
  return s
  
maxsubtree(root)

print(msn, ms, sep="@")
    
  
    
  
  
  