# Problem #2331 --> EVALUATE BOOLEAN BINARY TREE

# You are given the root of a full binary tree with the following properties:

# Leaf nodes have either the value 0 or 1, where 0 represents False and 1 represents True.
# Non-leaf nodes have either the value 2 or 3, where 2 represents the boolean OR and 3 represents the boolean AND.

# ---------------------------------------------------------------------------------------------------------------------------


def evaluateTree(root: object) -> bool:
    def traverse(node: object) -> bool:
        # Base case - Handles empty tree or missing child
        if node is None:
            return True

        # Check if the node is a leaf node --> No children present
        if node.left is None and node.right is None:
            # Return corresponding boolean base on numerical value
            return False if node.val == 0 else True

        # If the node's value is 2 --> either evaluate if one node is True or both
        # Recursive function call to move through children
        if node.val == 2:
            # Returns the case where the value is 2 --> Either child must evaluate to True
            return traverse(node.left) or traverse(node.right)
        else:
            # Returns the case where the value is 3 --> Both children must evaluate to True
            return traverse(node.left) and traverse(node.right)

    # Return the internal function to begin the recursion
    return traverse(root)


# ---------------------------------------------------------------------------------------------------------------------------

# TIME COMPLEXITY
# O(n) Time --> Where 'n' is the number of nodes in the tree
# We visit each node one time during traversal

# SPACE COMPLEXITY
# O(h) Space --> Where 'h' is the height of the tree
# Worst case it could be equal to the number of nodes if the tree is lopsided

# ---------------------------------------------------------------------------------------------------------------------------

# Same logic as the above solution --> We traverse each node and set the appropriate value
# This function uses a match/case statement for cleaner handling of node values.

# Logic:
# - If the node value is 0, the subtree evaluates to False.
# - If the node value is 1, the subtree evaluates to True.
# - If the node value is 2, the subtree evaluates to the logical OR of its left and right subtrees.
# - If the node value is 3, the subtree evaluates to the logical AND of its left and right subtrees.
# - For any other value, the subtree evaluates to False.


def evaluateTree2(root):
    if not root:
        return False

    match root.val:
        # Node value 0 maps to False.
        case 0:
            return False
        # Node value 1 maps to True.
        case 1:
            return True
        # Node value 2 maps to logical OR of left and right subtrees.
        case 2:
            return evaluateTree2(root.left) or evaluateTree2(root.right)
        # Node value 3 maps to logical AND of left and right subtrees.
        case 3:
            return evaluateTree2(root.left) and evaluateTree2(root.right)
        # Default case: Return False for unsupported node values.
        case _:
            return False


from Utils.Python.Tree import BinaryTree

tree1Vals = [2, 1, 3, None, None, 0, 1]

tree1 = BinaryTree()

for val in tree1Vals:
    tree1.add(val)

tree1.print_level_order()
print(evaluateTree2(tree1.root))
