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

def levellinewise2nd(root):
  q = []  
  q.append(root)
  q.append(None)
  while(len(q)!=1 ):
    a = q.pop(0)
    if a is not None:
      print(a.data, end = " ") 
      for i in a.child:
        q.append(i)
    else:
      q.append(None)
      print()
      
 
 

 
levellinewise2nd(root)