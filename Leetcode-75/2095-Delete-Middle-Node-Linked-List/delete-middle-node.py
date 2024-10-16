# PROBLEM #2095 - DELETE THE MIDDLE NODE OF A LINKED LIST

# You are given the head of a linked list. Delete the middle node, and return the head of the modified linked list.

# The middle node of a linked list of size n is the ⌊n / 2⌋th node from the start
# using 0-based indexing, where ⌊x⌋ denotes the largest integer less than or equal to x.

# For n = 1, 2, 3, 4, and 5, the middle nodes are 0, 1, 1, 2, and 2, respectively.

#---------------------------------------------------------------------------------------------------------------------------

from Utils.LinkedLists.LinkedList import ListNode, linkedListToList, listToLinkedList

def deleteMiddle(head: ListNode | None) -> ListNode | None:
    if not head or not head.next: return None

    n = 0
    current = head

    while (current):
        current = current.next
        n += 1

    midIdx = n // 2
    current = head
    prevNode = None

    for i in range(midIdx):
        prevNode = current
        current = current.next

    if prevNode and current:
        prevNode.next = current.next

    return head

#---------------------------------------------------------------------------------------------------------------------------

linkList1 = listToLinkedList([1, 3, 4, 7, 1, 2, 6])
print(linkedListToList(linkList1))
deleteMiddle(linkList1) # For a multi-node list, there is no need to update the reference to the linked list
print(linkedListToList(linkList1))

linkList2 = listToLinkedList([1])
print(linkedListToList(linkList2))
linkList2 = deleteMiddle(linkList2) # For a single-node list, we must update the variable to remove any reference to the original linked list
print(linkedListToList(linkList2))