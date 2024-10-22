class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self) -> str:
        return f'{self.val}'

class Tree:
    def __init__(self):
        self.root = None

    # Return the in-order traversal of the tree as a string
    def __str__(self):
        values = []
        self._level_order(self.root, values)
        return " -> ".join(map(str, values))

    # In-order traversale for print statement
    def _level_order(self, node, values):
        if not node:
            return
        
        queue = [node]

        while queue:
            curr = queue.pop(0)
            values.append(curr.val)

            if curr.left:
                queue.append(curr.left)

            if curr.right:
                queue.append(curr.right)


    def add(self, value):
        if not self.root:
            self.root = TreeNode(value)
            return

        queue = [self.root]

        while queue:
            current = queue.pop(0)

            if not current.left:
                current.left = TreeNode(value)
                return
            
            if not current.right:
                current.right = TreeNode(value)
                return
            
            queue.append(current.left)
            queue.append(current.right)
        

