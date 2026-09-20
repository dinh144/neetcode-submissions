# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Nếu danh sách rỗng hoặc chỉ có 1 node, không thể có vòng lặp
        if not head or not head.next:
            return False
        fast = head
        slow = head
        # Di chuyển slow (1 bước) và fast (2 bước) cho đến khi gặp nhau hoặc đến cuối
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
            if fast == slow:
                return True
    
        return False