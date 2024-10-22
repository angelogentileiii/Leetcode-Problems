export class TreeNode {
    val: number;
    left: TreeNode | null;
    right: TreeNode | null;

    constructor(val: number) {
        this.val = val;
        this.left = null;
        this.right = null;
    }

    toString(): string {
        return `${this.val}`;
    }
}

export class Tree {
    root: TreeNode | null;
    constructor() {
        this.root = null;
    }

    // Return the in-order traversal of the tree as a string
    toString() {
        let values: number[] = [];
        this._level_order(this.root, values);
        return values.join(" -> ");
    }
    // In-order traversale for print statement
    _level_order(node: TreeNode | null, values: number[]) {
        if (!node) return;

        let queue = [node];

        while (queue.length > 0) {
            let curr = queue.shift()!;
            values.push(curr.val);

            if (curr.left) {
                queue.push(curr.left);
            }

            if (curr.right) {
                queue.push(curr.right);
            }
        }
    }

    add(value: number): void {
        if (!this.root) {
            this.root = new TreeNode(value);
            return;
        }

        let queue = [this.root];

        while (queue.length > 0) {
            let current = queue.shift()!;

            if (!current.left) {
                current.left = new TreeNode(value);
                return;
            }

            if (!current.right) {
                current.right = new TreeNode(value);
                return;
            }

            queue.push(current.left);
            queue.push(current.right);
        }
    }
}
