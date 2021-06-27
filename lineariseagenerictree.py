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


def gettail(s):
  while(len(s.child)==1):
    s = s.child[0]
  return s
  
def linear(root):
  for i in root.child:
    linear(i)
  while(len(root.child)>1):
    fl = root.child.pop()
    sl = root.child[-1]
    a = gettail(sl)
    a.child.append(fl)
   


linear(root)


def display(root):
  s = str(root.data) + " -> "
  for i in root.child:
    s += str(i.data) + ", "
  s += "."
  print(s)
  for i in root.child:
    display(i)
    

display(root)


