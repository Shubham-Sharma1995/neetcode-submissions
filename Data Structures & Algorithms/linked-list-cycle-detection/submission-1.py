# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow,fast= head,head #considering to both be in initial position
        while fast and fast.next: #means fast.next should not be null otherwise the pointers are not coming in a cyclic nature
             slow=slow.next
             fast= fast.next.next
             if slow==fast:
                return True



             


                
        return False




          
         


        