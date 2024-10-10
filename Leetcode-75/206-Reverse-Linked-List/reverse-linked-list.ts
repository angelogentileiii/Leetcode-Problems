// Problem #206 - REVERSE A LINKED LIST

class ListNode {
    val: number;
    next: ListNode | null;
    constructor(val?: number, next?: ListNode | null) {
        this.val = val === undefined ? 0 : val;
        this.next = next === undefined ? null : next;
    }
}

function reverseList(head: ListNode | null): ListNode | null {
    if (!head) return null; // Base case --> If not given a valid head, return null

    let prevNode: ListNode | null = null; // Marker for the previos node --> Will become the tail
    let currNode: ListNode | null = head; // Marker for the current node --> Tracks position within list

    while (currNode) {
        let nextNode = currNode.next; // Marker for the next node in the list --> In the original order
        currNode.next = prevNode; // Change the next pointer to point to the previous node --> The REVERSAL is here
        prevNode = currNode; // Update marker to current node for next iteration
        currNode = nextNode; // Update marker to the next node for next iteration
    }

    return prevNode; // Return the previous node --> After the last iteration, the previous node represents the final current node AKA the new HEAD
}

//---------------------------------------------------------------------------------------------------------------------------

// TWO FUNCTIONS TO AID IN TERMINAL OUTPUT

function listToLinkedList(list: any[]): ListNode | null {
    if (!list) return null;

    const head = new ListNode(list[0]);
    let current = head;

    for (let i = 1; i < list.length; i++) {
        current.next = new ListNode(list[i]);
        current = current.next;
    }

    return head;
}

function linkedListToList(head: ListNode | null): any[] | undefined {
    if (!head) return;

    let current: ListNode | null = head;
    let res: any[] = [];

    while (current) {
        res.push(current.val);
        current = current.next;
    }

    return res;
}

//---------------------------------------------------------------------------------------------------------------------------

const linkedList1 = listToLinkedList([5, 4, 3, 2, 1]);
const linkedList2 = listToLinkedList([56, 34, 32, 4424, 544, 20, 4]);

const reversedList1 = reverseList(linkedList1);
const reversedList2 = reverseList(linkedList2);

console.log(linkedListToList(reversedList1));
console.log(linkedListToList(reversedList2));
