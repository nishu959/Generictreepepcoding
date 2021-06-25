class Node:
  def __init__(self, data):
    self.data = data
    self.child = []
  

ip = [10,20,50,-1,60, -1,-1,30, 70,-1,80,110, -1,120,-1,-1,90,-1,-1,40,100,-1,-1,-1]


# making of Tree

l = []
root = None

for i in ip:
  if(i==-1):
    l.pop()
  else:
    n = Node(i)
    if(len(l)>0):
      l[-1].child.append(n)
    else:
      root = n
    l.append(n)
    
#displaying the tree

def display(root):
  s = str(root.data) + " -> "
  for i in root.child:
    s += str(i.data) + ", "
  s += "."
  print(s)
  for i in root.child:
    display(i)
    

display(root)
    

    
    
    


      
      
      










