class Tree():
  def __init__(self, data ):
    self.data = data
    self.child = []
 

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
   
 

def linear2(root):
  if(len(root.child)==0):
    return root
  lkt = linear2(root.child[-1])
  while(len(root.child)>1):
    ln = root.child.pop()
    sln = root.child[-1]
    a = linear2(sln)
    a.child.append(ln)
  return lkt
   
  
linear2(root)


def display(root):
  s = str(root.data) + " -> "
  for i in root.child:
    s += str(i.data) + ", "
  s += "."
  print(s)
  for i in root.child:
    display(i)
    

display(root)


