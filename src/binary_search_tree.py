class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

    def search(self, target):
        if self.value == target:
            return self
        elif target < self.value:
            if self.left is None:
                return False
            else:
                return self.left.search(target)
        else:
            if self.right is None:
                return False
            else:
                return self.right.search(target)



# ---------------- Deleting ---------------------- Lecture BTS (Binary Search Trees)
# Delete: 
def delete(self, target):
# Find the target node, keeping track of its parent
        parent_node = None
        target_node = None
        current = self
        # Repeat until target == current value
        while True:
            # Compare target to current value
            # If target is less than, go left → set current = left child
            if target < current.value:
                # update parent to current and set current to the left child
                parent_node = current
                current = current.left
            # If target is greater than, go right → set current = right child
            elif target > current.value:
                # update parent to current and set current to the right child
                parent_node = current
                current = current.right
            else:
                # target == current.value, break
                target_node = current
                break

        # If we don’t find it: return None / False
        if target_node is False:
            return False
            
        # If we do find it, there are 3 cases

        # Case 1: If target node is a leaf, just delete it (set the parent's pointer to None)
        if target_node.left is None and target_node.right is None:
            if target_node.value < parent_node.value:
                # target node value < parent node value, it's the left child
                parent_node.left = None
            else:
                # target node value > parent node value, it's the right child
                parent_node.right = None
            return target_node
            
        # Case 2: target node only has one child, select that child as the replacement node
        # If target node only has left child
        if target_node.right is None:
            # replacement is the child
            replacement = target_node.left
            # Set target’s parent.left/right = replacement
            if target_node.value < parent_node.value:
                parent_node.left = replacement
            else:
                parent_node.right = replacement
            # Set targets.children to none
            target_node.left = None
            return target_node
        # If target node only has right child
        elif target_node.right is None:
            replacement = target_node.right
            # Set target’s parent.left/right = replacement
            if target_node.value < parent_node.value:
                parent_node.left = replacement
            else:
                parent_node.right = replacement
            # Set targets.children to none
            target_node.right = None
            return target_node
            
        # Case 3: Target node has two children.
        # Choose the next largest node as the replacement
        # go to the left most child on the right subtree, keeping track of the replacement's parent
        replacement = None
        replacement_parent_node = None
        current = target_node.right
        while True:
            # While replacement has left child: replacement = replacement.left
            if current.left is None:
                # We found the smallest node in the subtree, set replacement to current
                replacement = current
                break
            else:
                # Still smaller values in the tree. update parent to current and set current to the left child
                replacement_parent_node = current
                current = current.left

        # Replace the target w/ the replacement
        # Replacement’s parent.left = none
        replacement_parent_node.left = None

        # Target’s parent.(left or right)? = replacement
        if target_node.value < parent_node.value:
            parent_node.left = replacement
        else:
            # target node value > parent node value, it's the right child
            parent_node.right = replacement

        # Replacement.left = target.left
        replacement.left = target_node.left
        # Replacement.right = target.right
        replacement.right = target_node.right
        return target_node
        
def find_minimum_value(self):
    # While current has left child: replacement = replacement.left
    # recursive:
    # base case:
    if self.left is None:
        return self
    left_child = self.left
    min = left_child.find_minimum_value()
    return min


class BST:
    def __init__(self, value):
        self.root = BSTNode(value)

    def insert(self, value):
        self.root.insert(value)

    def search(self, value):
        return self.root.search(value)

    def delete(self, value):
        return self.root.delete(value)

    def find_minimum_value(self):
        return self.root.find_minimum_value().value


bst = BST(30)
bst.insert(15)
bst.insert(39)
bst.insert(7)
bst.insert(10)
bst.insert(56)

# print(bst.find_minimum_value())
print(bst.root.value, bst.root.left.value, bst.root.right.value)
deleted = bst.delete(15)
print(deleted.value)

print(bst.root.value, bst.root.left.value, bst.root.right.value)


# At each node, get left and right subtree's height.
# Drill down recursion:
    # As we come up, we about 2 things
    # 1. A node's height in the tree and
    # 2. If a node's left and right subtrees are balanced.
