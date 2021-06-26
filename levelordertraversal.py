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


      
def leveltraversal(root):
  s = []  
  s.append(root)
  while(len(s)>0):
    a = s.pop(0)
    print(a.data, end=" ")
    for i in a.child:
      s.append(i)
    
  
  print(".")
  
  
leveltraversal(root)
 
 