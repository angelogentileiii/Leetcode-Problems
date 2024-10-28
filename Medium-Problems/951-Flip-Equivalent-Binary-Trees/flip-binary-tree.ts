// PROBLEM #951 - FLIP EQUIVALENT BINARY TREES

// For a binary tree T, we can define a flip operation as follows: choose any node, and swap the left and right child subtrees.
// A binary tree X is flip equivalent to a binary tree Y if and only if we can make X equal to Y after some number of flip operations.
// Given the roots of two binary trees root1 and root2, return true if the two trees are flip equivalent or false otherwise.

// ---------------------------------------------------------------------------------------------------------------------------

import { BinaryTree, TreeNode } from "../../Utils/Trees/Tree";

function flipEquiv(
    root1: TreeNode<number> | null,
    root2: TreeNode<number> | null
): boolean {
    function checkNodes(
        node1: TreeNode<number> | null,
        node2: TreeNode<number> | null
    ): boolean {
        if (!node1 && !node2) {
            return true;
        }

        if (!node1 || !node2 || node1.val !== node2.val) {
            return false;
        }

        return (
            (checkNodes(node1.left, node2.left) &&
                checkNodes(node1.right, node2.right)) ||
            (checkNodes(node1.left, node2.right) &&
                checkNodes(node1.right, node2.left))
        );
    }

    return checkNodes(root1, root2);
}

const tree1Vals = [1, 2, 3, 4, 5, 6, null, null, null, 7, 8];
const tree2Vals = [1, 3, 2, null, 6, 4, 5, null, null, null, null, 8, 7];

const tree1 = new BinaryTree<number>();
for (let val of tree1Vals) {
    tree1.add(val);
}

const tree2 = new BinaryTree<number>();
for (let val of tree2Vals) {
    tree2.add(val);
}

console.log("Tree1: ", tree1.toString());
console.log("Tree2: ", tree2.toString());

console.log(flipEquiv(tree1.root, tree2.root));
