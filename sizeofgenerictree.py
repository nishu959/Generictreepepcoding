class Tree():
  def __init__(self, data):
    self.data = data
    self.child = []
    
    
root= None
l = []
m = int(input())
n = list(map(int, input().split()))


for i in n:
  if i==-1:
    l.pop()
  else:
    node = Tree(i)
    if(len(l)>0):
      l[-1].child.append(node)
    else:
      root = node
      
    l.append(node)
    

def sizeoftree(root):
  s =0
  for i in root.child:
    s += sizeoftree(i) 
  return s+1
  
  
print(sizeoftree(root))

    
    



