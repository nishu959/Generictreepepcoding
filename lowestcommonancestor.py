class Tree():
  def __init__(self, data ):
    self.data = data
    self.child = []
 

root = None
l = []
m = int(input())
n = list(map(int, input().split()))
n1= int(input())
n2 = int(input())



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
    
  
    
def lca(root, n1, n2):
  p1 = rootpath(root, n1)
  p2 = rootpath(root, n2)
  i = len(p1)-1
  j = len(p2)-1
  while(i>=0 and j>=0 and (p1[i]==p2[j])):
    i -= 1
    j -= 1
       
  i+=1
  j+=1
  return p1[i]
  
print(lca(root, n1, n2)) 
  
  
  