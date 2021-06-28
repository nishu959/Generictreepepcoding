class Tree():
  def __init__(self, data ):
    self.data = data
    self.child = []
 

root = None
l = []
m = int(input())
n = list(map(int, input().split()))
num = int(input())



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
    

def rootpath(root, num):
  if(root.data == num): #base case
    p = []
    p.append(num)
    return p
  for i in root.child:
    p = rootpath(i, num) #hypothesis
    if(len(p)>0):
      p.append(root.data) #induction
      return p
  return []
    
  
    
  
print(rootpath(root,num)) 
