export class ListNode {
    val: number;
    next: ListNode | null;
    constructor(val?: number, next?: ListNode | null) {
        this.val = val === undefined ? 0 : val;
        this.next = next === undefined ? null : next;
    }
}

// TWO FUNCTIONS TO AID IN TERMINAL OUTPUT

export function listToLinkedList(list: any[]): ListNode | null {
    if (!list) return null;

    const head = new ListNode(list[0]);
    let current = head;

    for (let i = 1; i < list.length; i++) {
        current.next = new ListNode(list[i]);
        current = current.next;
    }

    return head;
}

export function linkedListToList(head: ListNode | null): any[] | undefined {
    if (!head) return;

    let current: ListNode | null = head;
    let res: any[] = [];

    while (current) {
        res.push(current.val);
        current = current.next;
    }

    return res;
}
