import sys

class Tree():
  def __init__(self, data ):
    self.data = data
    self.child = []
 


m = int(input())
n = list(map(int, input().split()))
ele = int(input())


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

floor = -1*sys.maxsize 
ceil =sys.maxsize 

def ceilfloor(root, ele):
  global floor, ceil
  if(root.data > ele and ceil > root.data):
    ceil = root.data
  if(root.data < ele and floor < root.data):
    floor = root.data
    
  for i in root.child:
    ceilfloor(i, ele)
    
ceilfloor(root, ele)
    

print("CEIL =", ceil)
  
    
print("FLOOR =", floor)
 

