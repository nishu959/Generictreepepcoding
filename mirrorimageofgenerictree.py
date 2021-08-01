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
    
def display(root):
  s = str(root.data) + " -> "
  for i in root.child:
    s += str(i.data) + ", "
  s += "."
  print(s)
  for i in root.child:
    display(i)
    

display(root)
    

    
    
def mirrorimage(root):
  for i in root.child:
    mirrorimage(i)
  root.child.reverse()
  
  
mirrorimage(root)

#After the mirror image tree become

def display2(root):
  s = str(root.data) + " -> "
  for i in root.child:
    s += str(i.data) + ", "
  s += "."
  print(s)
  for i in root.child:
    display2(i)
   

display2(root) 

