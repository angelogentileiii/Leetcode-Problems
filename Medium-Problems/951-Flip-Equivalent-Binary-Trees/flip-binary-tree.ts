import { Tree, TreeNode } from "../../Utils/Trees/Tree";

function flipEquiv(root1: TreeNode | null, root2: TreeNode | null): boolean {
    function checkNodes(node1: TreeNode | null, node2: TreeNode | null): boolean {
        if (!node1 && !node2) {
            return true
        }

        if (!node1 || !node2 || node1.val !== node2.val) {
            return false
        }

        return (
            (checkNodes(node1.left, node2.left) || checkNodes(node1.left, node2.right))
        ) && (
            (checkNodes(node1.right, node2.right) || checkNodes(node1.right, node2.left))
        )
    }

    return checkNodes(root1, root2)
}