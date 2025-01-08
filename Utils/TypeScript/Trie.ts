// Our TrieNode class will be used for each node of our Trie and keeping track of both the character's frequency and children (next letters)
export class TrieNode {
    childNodes: Map<string, TrieNode>;
    frequency: number;

    constructor() {
        this.childNodes = new Map();
        this.frequency = 0;
    }

    // Helper function for logging in the console properly --> Indentation based on character index
    prettyPrint(level: number = 0): string {
        const indent = "  ".repeat(level);
        let result = `${indent}TrieNode(frequency=${
            this.frequency
        }, children=[${Array.from(this.childNodes.keys()).join(", ")}])\n`;

        for (const [key, child] of this.childNodes.entries()) {
            result += `${indent}  '${key}':\n${child.prettyPrint(level + 2)}`;
        }

        return result;
    }
}

class TrieBase {
    root: TrieNode;

    constructor() {
        this.root = new TrieNode();
    }

    protected _insert(path: string[]): void {
        let currNode = this.root;

        for (const key of path) {
            if (!currNode.childNodes.has(key)) {
                currNode.childNodes.set(key, new TrieNode());
            }
            currNode = currNode.childNodes.get(key)!;
            currNode.frequency += 1;
        }
    }

    protected _search(path: string[]): number {
        let currNode = this.root;

        for (const key of path) {
            if (!currNode.childNodes.has(key)) {
                return 0;
            }
            currNode = currNode.childNodes.get(key)!;
        }
        return currNode.frequency;
    }
}

export class PrefixTrie extends TrieBase {
    insertWord(word: string): void {
        this._insert(Array.from(word));
    }

    searchWord(word: string): boolean {
        return this._search(Array.from(word)) > 1;
    }
}

export class PrefixSuffixTrie extends TrieBase {
    insertWord(word: string): void {
        let currNode = this.root;

        for (let i = 0; i < word.length; i++) {
            let prefix = word[i];
            let suffix = word[word.length - 1 - i];

            // Create the tuple key
            const key = `${prefix}, ${suffix}`;

            // If the (prefix, suffix) pair doesn't exist, initialize it
            if (!currNode.childNodes.has(key)) {
                currNode.childNodes.set(key, new TrieNode());
            }

            // Move to the next node and increment frequency
            currNode = currNode.childNodes.get(key)!;
            currNode.frequency += 1;
        }
    }

    searchWord(word: string): number {
        let currNode = this.root;

        for (let i = 0; i < word.length; i++) {
            let prefix = word[i];
            let suffix = word[word.length - 1 - i];

            // Create the tuple key
            const key = `${prefix}, ${suffix}`;

            // If the (prefix, suffix) pair doesn't exist, initialize it
            if (!currNode.childNodes.has(key)) {
                return 0;
            }

            // Move to the next node and increment frequency
            currNode = currNode.childNodes.get(key)!;
        }

        console.log(`Curr Node Frequency: ${currNode.frequency}`);
        return currNode.frequency;
    }
}
