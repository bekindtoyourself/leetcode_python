# -*- coding: UTF-8 -*-

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        elems = []
        while self:
            elems.append(str(self.val))
            self = self.next
        return ('').join(elems)

class SLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.val = None
        self.next = None

    def add(self, *items):
        for item in items:
            node = ListNode(item)
            if not self.head:
                self.head = node
            else:
                cur = self.head
                while cur.next != None:
                    cur = cur.next
                cur.next = node
        self.next = self.head.next
        self.val = self.head.val

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        :type l1: SLinkedList
        :type l2: SLinkedList
        :rtype l: ListNode
        """
        n = l1.val + l2.val
        l3 = ListNode(n % 10)
        l3.next = ListNode(n // 10)
        p1 = l1.next
        p2 = l2.next
        p3 = l3
        while True:
            if p1 and p2:
                sum = p1.val + p2.val + p3.next.val
                p3.next.val = sum % 10
                p3.next.next = ListNode(sum // 10)
                p1 = p1.next
                p2 = p2.next
                p3 = p3.next
            elif p1 and not p2:
                sum = p1.val + p3.next.val
                p3.next.val = sum % 10
                p3.next.next = ListNode(sum // 10)
                p1 = p1.next
                p3 = p3.next
            elif not p1 and p2:
                sum = p2.val + p3.next.val
                p3.next.val = sum % 10
                p3.next.next = ListNode(sum // 10)
                p2 = p2.next
                p3 = p3.next
            else:
                if p3.next.val == 0:
                    p3.next = None
                break
        return l3

def main():
    l1 = SLinkedList()
    l2 = SLinkedList()
    l1.add(1,9,9,1)
    l2.add(9,2,3)

    result_list = Solution().addTwoNumbers(l1, l2)
    print(result_list)

if __name__ == '__main__':
    main()
