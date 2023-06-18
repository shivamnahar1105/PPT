#Q1. 

def mySqrt(x):
    left = 0
    right = x
    
    while left <= right:
        mid = (left + right) // 2
        square = mid * mid
        
        if square > x:
            right = mid - 1
        else:
            left = mid + 1
    
    return right

  #Q2. 
  class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2):
    dummy = ListNode()
    curr = dummy
    carry = 0

    while l1 or l2:
        x = l1.val if l1 else 0
        y = l2.val if l2 else 0
        _sum = x + y + carry

        carry = _sum // 10
        curr.next = ListNode(_sum % 10)

        curr = curr.next
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next

    if carry:
        curr.next = ListNode(carry)

    return dummy.next

