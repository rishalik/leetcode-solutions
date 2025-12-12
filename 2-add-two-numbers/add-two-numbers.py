# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode], carry=0) -> Optional[ListNode]:
        return self._addTwoNumbers(l1, l2)

    def _addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode], carry=0) -> Optional[ListNode]:
        if l1 is None and l2 is None and carry == 0:
            return None
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0
        total_sum = val1 + val2 + carry
        next_carry = 1 if total_sum > 9 else 0
        digit = total_sum % 10
        result = ListNode(digit)
        next_l1 = l1.next if l1 else None
        next_l2 = l2.next if l2 else None
        result.next = self._addTwoNumbers(next_l1, next_l2, next_carry)
        return result



        