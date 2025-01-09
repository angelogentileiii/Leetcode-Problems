from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self) -> str:
        left_val = self.left.val if self.left else "None"
        right_val = self.right.val if self.right else "None"
        return f"{'Value: ', self.val, 'Right Child: ', self.left.val, 'Left Child', self.right.val}"


class BinaryTree:
    def __init__(self):
        self.root = None

    def add(self, value):
        new_node = TreeNode(value)

        if not self.root:
            self.root = new_node
            return

        queue = deque([self.root])
        while queue:
            current = queue.popleft()

            if not current.left:
                current.left = new_node
                break
            else:
                queue.append(current.left)

            if not current.right:
                current.right = new_node
                break
            else:
                queue.append(current.right)

    def print_level_order(self):
        if not self.root:
            print("Tree is empty")
            return

        values = []
        queue = deque([self.root])

        while queue:
            node = queue.popleft()

            # Only store the value for non-leaf nodes, or if it's a leaf node, store it until we encounter more leaf nodes
            if node:
                values.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                values.append(None)

        # Remove the trailing none values
        while values and values[-1] is None:
            values.pop()

        # Print the result as an array-like format
        print(values)
