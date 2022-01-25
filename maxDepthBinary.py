# Given the root of a binary tree, return its maximum depth.

# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Input: root = [3,9,20,null,null,15,7]
# Output: 3 [3->20->15 or 7]

# Input: root = [1,null,2]
# Output: 2 [1->2]

from collections import deque

def maxDepth(self, root):
    # Recursive : time O(n) space O(n)
    # if root is None:
    #     return 0
    
    # return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

    # Breadth First Search : time O(n) space O(n)
    if root is None:
        return 0

    queue = deque([root])
    level = 0

    while queue:
        for i in range(len(queue)):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        level += 1
    
    return level
