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
    


def search(root,num):
  if(root.data == num):
    return True 
  for i in root.child:
    ans = search(i, num)
    if(ans):
      return True
  
  return False
 
 
if(search(root,num)):
  print("true")
else:
  print("false")
   


