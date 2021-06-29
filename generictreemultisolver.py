
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


size = 0
height = 0
maximum = -1*sys.maxsize
minimum = sys.maxsize

def multisolver(root,level):
  global size, maximum, minimum, height
  size += 1
  height =  max(level, height) 
  maximum = max(root.data,maximum)
  minimum = min(root.data,minimum)
  for i in root.child:
    multisolver(i,level+1)
    
   
 
multisolver(root, 0)
print("Size =", size)
print("Maximum =",maximum)
print("Minimum =",minimum)
print("Height =",height)