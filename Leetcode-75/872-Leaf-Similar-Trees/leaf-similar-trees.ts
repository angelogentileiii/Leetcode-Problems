// PROBLEM #872 - LEAF SIMILAR TREES

// Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a leaf value sequence.
// Two binary trees are considered leaf-similar if their leaf value sequence is the same.
// Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.

// ---------------------------------------------------------------------------------------------------------------------------

// Need to employ a depth-first search to find the leaf nodes first, we don't care about tracking the rest of the tree
//     So that is Recursion and a helper function
// Need a way to track each trees nodes and compare the arrays --> Maybe simultaneously

// ---------------------------------------------------------------------------------------------------------------------------

import { BinaryTree, OptionalTreeNode } from "../../Utils/Trees/Tree";

function leafSimilar(
    root1: OptionalTreeNode<number>,
    root2: OptionalTreeNode<number>
): boolean {
    // Initialize two stacks to keep track of leaf nodes
    let stack1: number[] = [];
    let stack2: number[] = [];

    function dfs(
        node: OptionalTreeNode<number>,
        stack: (number | null)[]
    ): void {
        if (!node) return;

        // Only push values to the stack if they are a leaf node
        if (!node.left && !node.right) {
            stack.push(node.val);
            return;
        }

        // Call the recursion on each child node to move deeper into tree
        dfs(node.left, stack);
        dfs(node.right, stack);
    }

    // Call the recursive function on both roots with respective stacks
    dfs(root1, stack1);
    dfs(root2, stack2);

    return stack1.join() === stack2.join(); // Must convert arrays to strings to compare in JavaScript
}

//---------------------------------------------------------------------------------------------------------------------------

const tree1_vals = [10, 4, 6, 15, 34, 40];
const tree2_vals = [10, 23, 42, 15, 34, 40];

const tree1 = new BinaryTree<number>();
for (let val of tree1_vals) {
    tree1.add(val);
}

const tree2 = new BinaryTree<number>();
for (let val of tree2_vals) {
    tree2.add(val);
}

console.log(tree1.toString());
console.log(tree2.toString());

console.log(leafSimilar(tree1.root, tree2.root));
