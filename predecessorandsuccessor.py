


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

pre = None
suc = None
state = 0

def findpresuc(root, ele):
  global pre, suc, state
  if(state==0):
    if(root.data==ele):
      state = 1
    else:
      pre = root
  elif(state==1):
    suc = root
    state = 2
    
    return
  
  for i in root.child:
    findpresuc(i, ele)
    
      
    
    
    
findpresuc(root, ele)   
if pre is not None:
  print("Predecessor =", pre.data)
else:
  print("Predecessor = Not found")
if suc is not None:
  print("Successor =", suc.data)
else:
  print("Successor = Not found" )

    

