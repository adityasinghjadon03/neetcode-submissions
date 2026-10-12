class ListNode:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class MyStack:

    def __init__(self):
        self.head = ListNode(-1)
        self.tail = ListNode(-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def push(self, x: int) -> None:
        new_node = ListNode(x)
        new_node.next = self.tail
        new_node.prev = self.tail.prev
        self.tail.prev.next = new_node
        self.tail.prev = new_node

    def pop(self) -> int:
        new_node = self.tail.prev
        self.tail.prev.prev.next = self.tail
        self.tail.prev = self.tail.prev.prev
        return new_node.val
        
    def top(self) -> int:
        return self.tail.prev.val

    def empty(self) -> bool:
        if self.head.next == self.tail:
            return True
        return False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()