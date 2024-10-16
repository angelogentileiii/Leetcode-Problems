class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

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
