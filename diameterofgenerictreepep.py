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

dia = 0

def returnheight(root):
  dn = -1
  sdn = -1
  global dia
  for i in root.child:
    d = returnheight(i)
    if(d > dn):
      sdn = dn
      dn = d
    elif(d>sdn):
      sdn = d
  can = dn + sdn + 2
  if(can>dia):
    dia = can
  dn+=1
  return dn
  
  
returnheight(root) 
print(dia)
  
    
  