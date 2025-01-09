# Problem 206 - REVERSE A LINKED LIST

# Given the head of a singly linked list, reverse the list, and return the reversed list.

# ---------------------------------------------------------------------------------------------------------------------------

from Utils.Python.LinkedList import ListNode, linkedListToList, listToLinkedList


def reverseList(head: ListNode) -> ListNode:
    # Variable for the previous node --> Will become the tail
    prev = None

    # Variable for our current position in our list --> Begins at the head
    currNode = head

    # While loop for moving through our nodes of our list
    while currNode:
        # Variable for the next node in the list originally
        nextNode = currNode.next

        # Make the pointer to the next node point to the previous node
        currNode.next = prev

        # Make the previous node pointer point to the current node --> Updated for next loop iteration
        prev = currNode

        # Updated the current node pointer to the next node --> For the next iteration of the loop
        currNode = nextNode

    return prev  # Return the previous node --> At the end of the loop, this becomes the new head of the linked list (updates to currNode AKA the new HEAD)


# ---------------------------------------------------------------------------------------------------------------------------


# SLIGHT SYNTAX CHANGE --> SAME SOLUTION (ONE LESS VAR STORED)
def reverseListSmall(head: ListNode) -> ListNode:
    if not head or not head.next:
        return head

    prev = None

    while head.next:
        next = head.next
        head.next = prev
        prev = head
        head = next

    head.next = prev

    return head


# ---------------------------------------------------------------------------------------------------------------------------

linkedList1 = listToLinkedList([1, 2, 3, 4, 5])
linkedList2 = listToLinkedList([56, 34, 32, 4424, 544, 20, 4])


reversedLinkedList1 = reverseList(linkedList1)  # Expect [5, 4, 3, 2, 1]
reversedLinkedList2 = reverseList(linkedList2)  # Expect [4, 20, 544, 4424, 32, 34, 56]


print(linkedListToList(reversedLinkedList1))
print(linkedListToList(reversedLinkedList2))
