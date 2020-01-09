class Node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data
def preorder_traversal(root):
    current=root
    if current.data!=None:
        print(current.data)
    if current.left!=None:
        preorder_traversal(current.left)
    if current.right!=None:
        preorder_traversal(current.right)
def postorder_traversal(root):
    current=root
    if current.left!=None:
        postorder_traversal(current.left)
    if current.right!=None:
        postorder_traversal(current.right)
    if current.data!=None:
        print(current.data)
def tree_traversal(root):
    current=root
    if current.data!=None:
        print(current.data)
    #if current.left!=None:
    #    tree_traversal(current.left)
    if current.right!=None:
        tree_traversal(current.right)
def get_height(root):
    if root is None:
        return -1
    else:
        left=get_height(root.left)
        right=get_height(root.right)
    return 1+max(left,right)
    
if __name__=="__main__":
    root=Node(1)
    root.left=Node(2)
    root.right=Node(3)
    root.left.left=Node(4)
    root.left.right=Node(5)
    root.right.left=Node(6)
    root.right.right=Node(7)
    #postorder_traversal(root)
    print(get_height(root))
'''
       1
    /     \
    2      3
   / \   /   \
  4   5 6     7
'''