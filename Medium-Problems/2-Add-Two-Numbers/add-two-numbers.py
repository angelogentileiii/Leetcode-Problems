# PROBLEM #2 - ADD TWO NUMBERS

# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order, and each of their nodes contains a single digit.
# Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# ---------------------------------------------------------------------------------------------------------------------------

import math
from Utils.LinkedLists.LinkedList import ListNode, linkedListToList, listToLinkedList


def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    # Initialize our base vars for use in function

    # The amount carried over to the next digit if the sum is greater than a single digit
    carry = 0

    # A dummy node for traversal and to easily return ListNode
    dummy = ListNode()

    # A pointer to our current node in the iteration --> Used for traversal
    current = dummy

    # Our loop runs while we have listnodes or a value that is carried over
    while l1 or l2 or carry:

        # The sum of the list node values plus any carried over value from prior node sum --> Begins at 0 from above
        sum = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
        print(f"Sum: {sum}")

        # The amount needed to be carried over for the next iteration --> Either 0 or 1 if we extend past a single digit
        carry = math.floor(sum / 10)
        print(f"Carry Over Amount: {carry}")

        # Set the next node to a list node with the proper summed value as a single digit --> Use % to have the remainder as the single digit (so 7 not 17)
        current.next = ListNode(sum % 10)

        # Move the pointer to the next node --> Our current calculations are completed
        current = current.next

        # Update the pointers for each linked list for next iteration
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

    # We return dummy.next because we've updated the listNodes as we traverse with current
    # If we just return dummy, we'll have the additional headnode with a value of 0 at the beginning --> Incorrect answer
    print(f"Result: {linkedListToList(dummy.next)}")

    print(f"Result w/ Dummy Head: {linkedListToList(dummy)}")
    return dummy.next


l1 = listToLinkedList([2, 4, 3])
l2 = listToLinkedList([5, 6, 4])

addTwoNumbers(l1, l2)
