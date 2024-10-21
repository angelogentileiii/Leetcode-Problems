// Problem #206 - REVERSE A LINKED LIST

import {
    ListNode,
    linkedListToList,
    listToLinkedList,
} from "../../Utils/LinkedLists/LinkedList";

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

const linkedList1 = listToLinkedList([5, 4, 3, 2, 1]);
const linkedList2 = listToLinkedList([56, 34, 32, 4424, 544, 20, 4]);

const reversedList1 = reverseList(linkedList1);
const reversedList2 = reverseList(linkedList2);

console.log(linkedListToList(reversedList1));
console.log(linkedListToList(reversedList2));