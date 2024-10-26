from Utils.Trees.Tree import Tree, TreeNode


def flipEquiv(root1: TreeNode | None, root2: TreeNode | None) -> bool:
    def checkNodes(node1: TreeNode | None, node2: TreeNode | None) -> bool:
        if not node1 and not node2:
            return True

        if not node1 or not node2 or node1.val != node2.val:
            return False

        return (
            checkNodes(node1.left, node2.left) and checkNodes(node1.left, node2.right)
        ) and (
            checkNodes(node1.right, node2.right) or checkNodes(node1.right, node2.left)
        )

    return checkNodes(root1, root2)


tree1Vals = [1, 2, 3, 4, 5, 6, None, None, None, 7, 8]
tree2Vals = [1, 3, 2, None, 6, 4, 5, None, None, None, None, 8, 7]

tree1 = Tree()
for val in tree1Vals:
    tree1.add(val)


tree2 = Tree()
for val in tree2Vals:
    tree2.add(val)

print(tree1)
print(tree2)

print(flipEquiv(tree1.root, tree2.root))
