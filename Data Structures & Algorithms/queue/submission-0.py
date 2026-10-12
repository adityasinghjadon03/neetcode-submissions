class ListNode:
    def __init__(self, val, prev=None,next=None):
        self.val = val
        self.prev = prev
        self.next = next

class Deque:
    
    def __init__(self):
        self.head = ListNode(-1)
        self.tail = ListNode(-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def isEmpty(self) -> bool:
        if self.head.next == self.tail:
            return True
        return False

    def append(self, value: int) -> None:
        new_node = ListNode(value)
        new_node.prev = self.tail.prev
        new_node.next = self.tail
        self.tail.prev.next = new_node
        self.tail.prev = new_node

    def appendleft(self, value: int) -> None:
        new_node = ListNode(value)
        new_node.next = self.head.next
        new_node.prev = self.head
        self.head.next.prev = new_node
        self.head.next = new_node

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        target = self.tail.prev
        target.prev.next = self.tail
        self.tail.prev = target.prev
        return target.val
        
    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        target = self.head.next
        self.head.next = target.next
        target.next.prev = self.head
        return target.val