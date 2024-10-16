// PROBLEM #2095 - DELETE THE MIDDLE NODE OF A LINKED LIST

// You are given the head of a linked list. Delete the middle node, and return the head of the modified linked list.

// The middle node of a linked list of size n is the ⌊n / 2⌋th node from the start
// using 0-based indexing, where ⌊x⌋ denotes the largest integer less than or equal to x.

// For n = 1, 2, 3, 4, and 5, the middle nodes are 0, 1, 1, 2, and 2, respectively.

//---------------------------------------------------------------------------------------------------------------------------

import {
    ListNode,
    listToLinkedList,
    linkedListToList,
} from "../../Utils/LinkedLists/LinkedList";

function deleteMiddle(head: ListNode | null): ListNode | null {
    if (!head || !head.next) return null; // Returns null if the head is empty or a singular node --> Deletes the singular node so returns null

    // Pointers for our loop to find the middle node
    let n = 0;
    let current: ListNode | null = head;

    // Loop to count the total number of nodes in the list --> Will be used to find the middle node
    while (current !== null) {
        current = current.next;
        n++;
    }

    const midIdx = Math.floor(n / 2); // Find the index of the middle node --> Will be used below
    current = head; // Reset the current variable to the head of the list
    let prevNode: ListNode | null = null; // Initialize a variable to keep track of the node prior to the middle node

    // Loop for moving to the middle node
    for (let i = 0; i < midIdx; i++) {
        prevNode = current; // prevNode moves to the node just prior to the middle node
        current = current!.next; // current moves to the middle node of the list
    }

    // We delete the middle node by SKIPPING IT --> Update prevNode's next pointer from current to current.next
    if (prevNode && current) {
        prevNode.next = current.next;
    }

    return head; // Returns the now modified head node
}

//---------------------------------------------------------------------------------------------------------------------------

let linkList1 = listToLinkedList([1, 3, 4, 7, 1, 2, 6]);
console.log(linkedListToList(linkList1));
deleteMiddle(linkList1); // For a multi-node list, there is no need to update the reference to the linked list
console.log(linkedListToList(linkList1));

let linkList2 = listToLinkedList([1]);
console.log(linkedListToList(linkList2));
linkList2 = deleteMiddle(linkList2); // For a single-node list, we must update the variable to remove any reference to the original linked list
console.log(linkedListToList(linkList2));
