"""
You are given a binary tree, you need to write a function that can determine if
it is symmetric around its center.

For example, this binary tree [4,5,5,6,7,7,6] is symmetric:

```plaintext
    4
   / \
  5   5
 / \ / \
6  7 7  6
```

But the following [4,5,5,None,6,None,6] is not:

```plaintext
    4
   / \
  5   5
   \   \
   6    6
```

*Note: you should attempt to solve this challenge with both an iterative and a
recursive solution.*
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def is_symmetric(root):
    # Your code here

