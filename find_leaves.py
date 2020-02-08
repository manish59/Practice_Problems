"""
366. Find Leaves of Binary Tree
Medium

Given a binary tree, collect a tree's nodes as if you were doing this: Collect and remove all leaves, repeat until the tree is empty.

 

Example:

Input: [1,2,3,4,5]
  
          1
         / \
        2   3
       / \     
      4   5    

Output: [[4,5,3],[2],[1]]

 

Explanation:

1. Removing the leaves [4,5,3] would result in this tree:

          1
         / 
        2          

 

2. Now removing the leaf [2] would result in this tree:

          1          

 

3. Now removing the leaf [1] would result in the empty tree:

          []         

"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
def print_tree(node):
    if node.left==None and node.right==None:
        print(node.val)
        return None
    else:
        node.left=print_tree(node.left)
        node.right=print_tree(node.right)
    return node
def Is_It_Child(node):
    if node.left==None and node.right==None:
        return True
if __name__=="__main__":
    Root=TreeNode(1)
    first_node=TreeNode(2)
    second_node=TreeNode(3)
    third_node=TreeNode(4)
    fourth_node=TreeNode(5)
    Root.left=first_node
    Root.right=second_node
    Root.left.left=third_node
    Root.left.right=fourth_node
    #print(Is_It_Child(Root.left.right))
    print_tree(Root)