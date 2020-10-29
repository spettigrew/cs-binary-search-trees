"""
You are given a binary tree.

Write a function that can find the **maximum depth** of the binary tree. The
maximum depth can be defined as the number of nodes found along the longest
path from the root down to the furthest leaf node. Remember, a leaf node is a
node that has no children.

Example:

Given the following binary tree

    5
   / \
  12  32
     /  \
    8    4

your function should return the depth = 3.
"""
class BinaryTreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def maxDepth(root):
    # Your code here
    # UPER
    # If root is a leaf, max depth is 1

    # PLAN
    # base case: if root is None, return 0
    if root is None:
        return 0
    # base case = if there's no left or right, return 1
    if root.left is None and root.right is None:
        return 1

    # if we have a left or right child:
    # get max depth of left child
    left_depth = maxDepth(root.left)
    # get the max depth of the right child
    right_depth = maxDepth(root.right)
    # add 1 to whichever is greater
    max_depth = 1 + max(left_depth, right_depth)  # max returns the max of whatever is passed in
    # return the result
    return max_depth

#
# root = BinaryTreeNode(value=5,
#                       left=BinaryTreeNode(value=12, left=None, right=None),
#                       right=BinaryTreeNode(value=32,
#                                            left=BinaryTreeNode(value=8, left=None, right=None),
#                                            right=BinaryTreeNode(value=4, left=None, right=None)))​
root = BinaryTreeNode(value=5,
                      left=BinaryTreeNode(value=12, left=None, right=None),
                      right=BinaryTreeNode(value=32,
                                           left=BinaryTreeNode(value=8, left=None, right=None),
                                           right=None))
print(maxDepth(root))


