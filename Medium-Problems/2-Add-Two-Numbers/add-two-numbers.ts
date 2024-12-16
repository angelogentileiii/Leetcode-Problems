// PROBLEM #2 - ADD TWO NUMBERS

// You are given two non-empty linked lists representing two non-negative integers.
// The digits are stored in reverse order, and each of their nodes contains a single digit.
// Add the two numbers and return the sum as a linked list.

// You may assume the two numbers do not contain any leading zero, except the number 0 itself.

// ---------------------------------------------------------------------------------------------------------------------------

import {
    ListNode,
    linkedListToList,
    listToLinkedList,
} from "../../Utils/LinkedLists/LinkedList";

function addTwoNumbers(
    l1: ListNode | null,
    l2: ListNode | null
): ListNode | null {
    // Initialize our variables --> And a dummy head for base case
    let carry: number = 0; // This represents the carried over value if summing of two nodes is larger than a single digit
    let dummy: ListNode = new ListNode(0); // This serves as our dummy head for the linked list
    let current: ListNode = dummy; // The pointer to track the current listNode we are on

    while (l1 || l2 || carry) {
        // Set two variables to represent the value to be added for the current nodes --> Cleaner code
        const val1 = l1 ? l1.val : 0;
        const val2 = l2 ? l2.val : 0;

        // Another variable tracks the total value of adding the two node values and any carried over value
        const sum = val1 + val2 + carry;
        console.log(`Summed Value: ${sum}`);

        // Calculate the most updated carry value after summing all of the value and prior carry value
        // Will either be 1 or 0 since each node value is a single digit
        carry = Math.floor(sum / 10);
        console.log(`Carried Over Value: ${carry}`);

        // Update the next value of the current pointer to the value of the list node calculated
        // Using % 10 ensures that we only return the remainder --> the additional 10 (1 value) has been assigned to the carry variable above
        current.next = new ListNode(sum % 10);
        console.log(`Computed Node Value: ${sum % 10}`);

        // Update our pointer to move to our next node --> Updates the loop so we can continue to process with new value
        current = current.next;

        // Update each list item node --> Either null or the next node
        l1 = l1 ? l1.next : null;
        l2 = l2 ? l2.next : null;
    }

    // We return dummy.next because it represents the beginning of our computed list
    // Since we make current = dummy --> As we update current we are also updating everything from dummy.next onward
    console.log(`Solution: ${linkedListToList(dummy.next)}`);
    return dummy.next;
}

const l1 = listToLinkedList([2, 4, 3]);
const l2 = listToLinkedList([5, 6, 4]);

addTwoNumbers(l1, l2);
