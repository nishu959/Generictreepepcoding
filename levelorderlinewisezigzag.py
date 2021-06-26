
  
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

def levellinewise(root):
  q = []  
  q.append(root)
  cq = []
  r = 0
  while(len(q)>0):
    a= q.pop()
    print(a.data, end=" ")
    if(r%2==0):
      for i in a.child:
        cq.append(i)   
      
    else:
      
      for i in a.child[::-1]:
        cq.append(i)   
      
      
      
     
    if(len(q)==0):
      q = cq
      cq = []
      print()
      r += 1
    
  



levellinewise(root)
