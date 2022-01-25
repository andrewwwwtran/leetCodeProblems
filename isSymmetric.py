# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

# Input: root = [1,2,2,3,4,4,3]
# Output: true

# Input: root = [1,2,2,null,3,null,3]
# Output: false

def isSymmetric(self, root):
    if root is None:
        return True
    else:
        # call recursively
        return self.isMirror(root.left, root.right)

def isMirror(self, leftChild, rightChild):
    # need to check if the top of the left and right child values are equal
    # recursively call 
    if leftChild and rightChild: # there are left and right child
        return leftChild.val == rightChild.val and self.isMirror(leftChild.left, rightChild.right) and self.isMirror(leftChild.right, rightChild.left)
    # this checks if both of the childs are null
    return leftChild == rightChild