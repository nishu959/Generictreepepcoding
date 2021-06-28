class Tree():
  def __init__(self, data ):
    self.data = data
    self.child = []
 


m = int(input())
n = list(map(int, input().split()))
p = int(input())
q = list(map(int, input().split()))



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
   

mroot = treeform(n, [], None)

proot = treeform(q, [], None)



def checkshape(mroot, proot):
  if(len(mroot.child)!=len(proot.child)):
    return False
  for i in range(len(mroot.child)):
    c1 = mroot.child[i]
    c2 = proot.child[i]
    if(checkshape(c1, c2)==False):
      return False
  return True
  
  
  
if(checkshape(mroot, proot)):
  print("true")
else:
  print("false")
    

   
 