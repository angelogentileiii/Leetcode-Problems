# PROBLEM #951 - FLIP EQUIVALENT BINARY TREES

# For a binary tree T, we can define a flip operation as follows: choose any node, and swap the left and right child subtrees.
# A binary tree X is flip equivalent to a binary tree Y if and only if we can make X equal to Y after some number of flip operations.
# Given the roots of two binary trees root1 and root2, return true if the two trees are flip equivalent or false otherwise.

# ---------------------------------------------------------------------------------------------------------------------------

from Utils.Python.Tree import Tree, TreeNode


def flipEquiv(root1: TreeNode | None, root2: TreeNode | None) -> bool:
    # Helper function to compare nodes of trees to see if an equivalency can be met
    def checkNodes(node1: TreeNode | None, node2: TreeNode | None) -> bool:
        # If both nodes are None --> They match and there are no children to check so we can return our True boolean
        if not node1 and not node2:
            return True

        # If either node is missing (We know we can't match) or if the values do not match
        # Return false because we know we can't flip values that don't match
        if not node1 or not node2 or node1.val != node2.val:
            return False

        # Recursively check the first roots left child versus the second roots left and right children --> Either can be True
        # Recursively check the first roots right child verss the second roots right and left children --> Again either can be True
        # If we receive True from both recursive functions, we know that it is possible to flip the trees as needed
        return (
            checkNodes(node1.left, node2.left) and checkNodes(node1.right, node2.right)
        ) or (
            checkNodes(node1.left, node2.right) and checkNodes(node1.right, node2.left)
        )

    # Begin the recursive call with each root given
    return checkNodes(root1, root2)


# ---------------------------------------------------------------------------------------------------------------------------

# DUE TO AN ISSUE WITH TREE CONSTRUCTION --> THIS RETURNS FALSE ALTHOUGH IT IS CORRECT AND PASSES ON LEETCODE

tree1Vals = [1, 2, 3, 4, 5, 6, None, None, None, 7, 8]
tree2Vals = [1, 3, 2, None, 6, 4, 5, None, None, None, None, 8, 7]

tree1 = Tree()
for val in tree1Vals:
    tree1.add(val)


tree2 = Tree()
for val in tree2Vals:
    tree2.add(val)

print("Tree1 Root: ")
tree1.print_root()
print("Tree2 Root: ")
tree2.print_root()

print(flipEquiv(tree1.root, tree2.root))
