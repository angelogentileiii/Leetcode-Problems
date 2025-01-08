export class TreeNode<T> {
    val: T | null;
    left: OptionalTreeNode<T>;
    right: OptionalTreeNode<T>;

    constructor(value: T | null) {
        this.left = null;
        this.right = null;
        this.val = value;
    }
}

export class BinaryTree<T> {
    root: OptionalTreeNode<T>;

    constructor() {
        this.root = null;
    }

    add(value: T | null): BinaryTree<T> {
        const node = new TreeNode(value);

        if (value === null) {
            return this; // Skip null values
        }

        if (!this.root) {
            this.root = node;
            return this;
        }

        const queue: (TreeNode<T> | null)[] = [this.root];

        while (queue.length) {
            const currNode = queue.shift(); // Get the front node from the queue

            // Check if we can insert in the left child
            if (!currNode!.left) {
                currNode!.left = node; // Insert here
                return this;
            } else {
                queue.push(currNode!.left); // Add left child to the queue
            }

            // Check if we can insert in the right child
            if (!currNode!.right) {
                currNode!.right = node; // Insert here
                return this;
            } else {
                queue.push(currNode!.right); // Add right child to the queue
            }
        }

        return this; // Return this for method chaining
    }

    lookup(value: T): TreeNode<T> | boolean {
        let currNode = this.root;

        while (currNode) {
            if (!currNode.val) continue;

            if (value === currNode.val) {
                return currNode;
            } else if (value > currNode.val) {
                currNode = currNode.right;
            } else {
                currNode = currNode.left;
            }
        }

        return false;
    }

    remove(value: T): BinaryTree<T> | boolean {
        let currNode = this.root;
        let parentNode: TreeNode<T> | null = null;

        while (currNode) {
            if (!currNode.val) continue;

            if (value === currNode.val) {
                // No children --> Leaf Node
                if (!currNode.left && !currNode.right) {
                    if (!parentNode) {
                        this.root = null;
                    } else if (parentNode.left === currNode) {
                        parentNode.left = null;
                    } else {
                        parentNode.right = null;
                    }
                    // Missing one child
                } else if (!currNode.left || !currNode.right) {
                    const childNode = currNode.left
                        ? currNode.left
                        : currNode.right;

                    if (!parentNode) {
                        this.root = childNode;
                    } else if (parentNode.left === currNode) {
                        parentNode.left = childNode;
                    } else {
                        parentNode.right = childNode;
                    }
                    // Has both children
                } else {
                    let leftMost = currNode.right; // start with right child to then move leftmost
                    let leftMostParent = currNode;

                    while (leftMost.left) {
                        leftMostParent = leftMost;
                        leftMost = leftMost.left;
                    }

                    currNode.val = leftMost.val;

                    if (leftMostParent.left === leftMost) {
                        leftMostParent.left = leftMost.right;
                    } else {
                        leftMostParent.right = leftMost.right;
                    }
                }
                return this;
            } else if (value > currNode.val) {
                parentNode = currNode;
                currNode = currNode.right;
            } else {
                parentNode = currNode;
                currNode = currNode.left;
            }
        }

        return false;
    }

    // Return the in-order traversal of the tree as a string
    toString(): string {
        let values: T[] = [];
        this._levelOrder(this.root);
        return values.join(" -> ");
    }

    // Level-order traversale for print statement
    _levelOrder(
        node: OptionalTreeNode<T> | null
    ): { level: number; values: (T | null)[] }[] {
        if (!node) {
            return [];
        }

        const result: { level: number; values: (T | null)[] }[] = [];
        const queue: OptionalTreeNode<T>[] = [node];
        let levelNum = 0; // Initialize level number

        while (queue.length > 0) {
            const level: (T | null)[] = [];
            const levelLength = queue.length;

            // Increment level number at the start of each level
            levelNum++;

            for (let i = 0; i < levelLength; i++) {
                const currentNode = queue.shift()!; // Remove the first element from the queue

                // Nulls are being pushed in the wrong place
                if (currentNode) {
                    level.push(currentNode.val);
                    queue.push(currentNode.left);
                    queue.push(currentNode.right);
                } else {
                    level.push(null);
                }
            }

            // Push an object containing the level number and the level values to the result
            result.push({ level: levelNum, values: level });
        }

        console.log(result);
        return result;
    }
}

export type OptionalTreeNode<T> = TreeNode<T> | null;
