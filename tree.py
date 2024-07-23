class node:
  def __init__(self,data):
    self.data=data
    self.left=left
    self.right=right
  def preorder(self,root):
    if(root==none):
      return
    print(root.data,end=" ")
    root.preorder(root.left)
    root.preorder(root.right)
root=node(1)
root.left=node(2)
root.right=node(3)

    
