import sys
class Tree():
  def __init__(self, data):
    self.data = data
    self.child = []
   
m = int(input())
ip = list(map(int, input().split()))
l = []
root = None


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
    

def maxintree(root):
  m = -1*sys.maxsize 
  for i in root.child:
    p = maxintree(i)
    m = max(p, m)
    
  if(root.data>m):
    m = root.data
  return m
  
  
  
print(maxintree(root))
 
 
    
  


