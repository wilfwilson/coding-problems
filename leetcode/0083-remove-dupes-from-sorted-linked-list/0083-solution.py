class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        while node and node.next:
            next_node = node.next
            if node.val == next_node.val:
                node.next = next_node.next
            else:
                node = next_node
        
        return head
