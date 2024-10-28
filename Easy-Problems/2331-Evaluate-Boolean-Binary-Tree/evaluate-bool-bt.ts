// Problem #2331 --> EVALUATE BOOLEAN BINARY TREE

// You are given the root of a full binary tree with the following properties:

// Leaf nodes have either the value 0 or 1, where 0 represents False and 1 represents True.
// Non-leaf nodes have either the value 2 or 3, where 2 represents the boolean OR and 3 represents the boolean AND.

// ---------------------------------------------------------------------------------------------------------------------------

import { BinaryTree, TreeNode } from "../../Utils/Trees/Tree";

function evaluateTree(root: TreeNode<any> | null): boolean {
    if (!root) return false; // Base case to return if there is no root to evaluate

    switch (
        root.val // Switch statement based on node value
    ) {
        case 0:
            return false; // Likely could remove as default would handle --> More readability
        case 1:
            return true;
        case 2:
            // The 2 value returns true is either child evaluates to True
            return evaluateTree(root.left) || evaluateTree(root.right);
        case 3:
            // The 3 value returns true is both children evaluate to True
            return evaluateTree(root.left) && evaluateTree(root.right);
        default:
            return false;
    }
}

//---------------------------------------------------------------------------------------------------------------------------

// On each recursive call, we evaluate the value based on the cases
// If children are present, we recursively enter those children to evaluate

// TIME COMPLEXITY
//     O(n) Time --> Where 'n' is the number of nodes in the tree
//     We visit each node one time during traversal

// SPACE COMPLEXITY
//     O(h) Space --> Where 'h' is the height of the tree
//         Worst case it could be equal to the number of nodes if the tree is lopsided

const tree1Vals = [2, 1, 3, null, null, 0, 1];

const tree1 = new BinaryTree();

for (let val of tree1Vals) {
    tree1.add(val);
}

console.log(tree1.toString());
console.log(evaluateTree(tree1.root));
