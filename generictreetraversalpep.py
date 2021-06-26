
class Tree():
  def __init__(self, data):
    self.data = data
    self.child = []
   
m = int(input())
ip = list(map(int, input().split()))
l = []
root = None

for i in ip:
  if(i==-1):
    l.pop()
  else:
    node = Tree(i)
    if(len(l)==0):
      root = node
    else:
      l[-1].child.append(node)
    l.append(node)
   


  
def traverse(root):
  #WHILE going deep in recursion, preorder
  print("Node Pre", root.data)
  for i in root.child:
    #left side edge in recursion, left edge
    print("Edge Pre ", root.data, "--", i.data, sep = "")
    traverse(i)
    #right side edge in recursion, right edge
    print("Edge Post ", root.data, "--", i.data, sep ="")
  #WHILE  coming out in recursion, postorder
  print("Node Post", root.data)

traverse(root)




