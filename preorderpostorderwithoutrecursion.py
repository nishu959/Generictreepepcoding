
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

class pair():
  def __init__(self, node, state):
    self.node = node
    self.state = state
    
       

def traverse(root):
  pre = ""
  post = ""
  s = []
  p = pair(root,-1)
  s.append(p)
  
  while(len(s)>0):
    top = s[-1]
    if(top.state == -1):
      pre += str(top.node.data) + " "
      top.state += 1
    elif(top.state ==  len(top.node.child)):
      post += str(top.node.data) + " "
      s.pop()
    else:
      p = pair(top.node.child[top.state],-1)
      s.append(p)
      top.state += 1
      
      
  print(pre)
  print(post)
 
 
traverse(root)
      