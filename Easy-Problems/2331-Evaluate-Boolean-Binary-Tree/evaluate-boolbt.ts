class TreeNode {
    val: number;
    left: TreeNode | null;
    right: TreeNode | null;
    constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
        this.val = val === undefined ? 0 : val;
        this.left = left === undefined ? null : left;
        this.right = right === undefined ? null : right;
    }
}

function evaluateTree(root: TreeNode | null): boolean {
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

// On each recursive call, we evaluate the value based on the cases
// If children are present, we recursively enter those children to evaluate

// TIME COMPLEXITY
//     O(n) Time --> Where 'n' is the number of nodes in the tree
//     We visit each node one time during traversal

// SPACE COMPLEXITY
//     O(h) Space --> Where 'h' is the height of the tree
//         Worst case it could be equal to the number of nodes if the tree is lopsided
