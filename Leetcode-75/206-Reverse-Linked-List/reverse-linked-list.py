# Problem 206 - REVERSE A LINKED LIST

# Given the head of a singly linked list, reverse the list, and return the reversed list.

#---------------------------------------------------------------------------------------------------------------------------

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head: ListNode) -> ListNode:
    prev = None # Marker for the previos node --> Will become the tail
    currNode = head # Marker for our current position in our list --> Begins at the head

    while currNode: # While we have a currentNode to work with
        nextNode = currNode.next # Marker for the next node in the list originally
        currNode.next = prev # Make the pointer to the next node point to the previous node
        prev = currNode # Make the previous node pointer point to the current node --> Updated for next loop iteration
        currNode = nextNode # Updated the current node pointer to the next node --> For the next iteration of the loop

    return prev # Return the previous node --> At the end of the loop, this becomes the new head of the linked list (updates to currNode AKA the new HEAD)

#---------------------------------------------------------------------------------------------------------------------------

# SLIGHT SYNTAX CHANGE --> SAME SOLUTION (ONE LESS VAR STORED)
def reverseListSmall(head: ListNode) -> ListNode:
    if not head or not head.next: return head

    prev = None

    while head.next:
        next = head.next
        head.next = prev
        prev = head
        head = next

    head.next = prev

    return head

#---------------------------------------------------------------------------------------------------------------------------

# TWO FUNCTION TO AID IN TERMINAL OUTPUT
def listToLinkedList(lst: list) -> ListNode:
    if not lst: return None

    head = ListNode(lst[0])
    current = head

    for val in lst[1:]:
        current.next = ListNode(val)
        current = current.next
    
    return head

def linkedListToList(head: ListNode) -> list:
    if not head: return

    res = []
    while head:
        res.append(head.val)
        head = head.next
    return res

#---------------------------------------------------------------------------------------------------------------------------

linkedList1 = listToLinkedList([1,2,3,4,5])
linkedList2 = listToLinkedList([56, 34, 32, 4424, 544, 20, 4])


reversedLinkedList1 = reverseList(linkedList1) # Expect [5, 4, 3, 2, 1]
reversedLinkedList2 = reverseList(linkedList2) # Expect [4, 20, 544, 4424, 32, 34, 56]


print(linkedListToList(reversedLinkedList1))
print(linkedListToList(reversedLinkedList2))
