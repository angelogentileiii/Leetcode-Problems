# PROBLEM #872 - LEAF SIMILAR TREES

# Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a leaf value sequence.
# Two binary trees are considered leaf-similar if their leaf value sequence is the same.
# Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.

# ---------------------------------------------------------------------------------------------------------------------------

# Need to employ a depth-first search to find the leaf nodes first, we don't care about tracking the rest of the tree
#     So that is Recursion and a helper function
# Need a way to track each trees nodes and compare the arrays --> Maybe simultaneously

#---------------------------------------------------------------------------------------------------------------------------

from Utils.Trees.Tree import TreeNode, Tree

def leafSimilar(root1: TreeNode | None, root2: TreeNode | None) -> bool:
    # Initialize two empty stacks --> Which we will push our leaf nodes into
    stack1 = []
    stack2 = []

    # Recursive function for DFS search
    def dfs(node: TreeNode | None, stack: list):
        # If we hit a null node (the end) --> We return
        if not node:
            return
        
        # If the node is a leaf node (no left or right children) --> We append to our relative stack
        if not node.left and not node.right:
            print('Leaf Node: ', node)
            stack.append(node.val)
            return
        
        # Call the recursive function on each child of the node --> Moves us deeper into the tree
        dfs(node.left, stack)
        dfs(node.right, stack)
    
    # Begin the recursive call on each root and the respective stack
    dfs(root1, stack1)
    dfs(root2, stack2)

    # Compare the two stacks and return the boolean if they are identical
    return stack1 == stack2

#---------------------------------------------------------------------------------------------------------------------------

tree1_vals = [10, 4, 6, 15, 34, 40]
tree2_vals = [10, 23, 42, 15, 34, 42]

tree1 = Tree()
for val in tree1_vals:
    tree1.add(val)

tree2 = Tree()
for val in tree2_vals:
    tree2.add(val)


print(tree1)
print(tree2)

print(leafSimilar(tree1.root, tree2.root))