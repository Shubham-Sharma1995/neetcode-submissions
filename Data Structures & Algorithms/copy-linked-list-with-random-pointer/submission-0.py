"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToCopy={
            None:None
        }
    #cloning the linklist nodes and adding to the hash map
        cur= head
        while cur:
            copy=Node(cur.val)
            oldToCopy[cur]=copy
            cur= cur.next
      

        #2nd pass->connecting to pointer
        cur= head
        while cur:
            copy=oldToCopy[cur]
            copy.next= oldToCopy[cur.next]
            copy.random=oldToCopy[cur.random]
            cur=cur.next
        return oldToCopy[head]




        