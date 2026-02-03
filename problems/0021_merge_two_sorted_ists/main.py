from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        merged_list = []
        while list1 != None:
            print(list1.val,list2.val)
            if list1.val <= list2.val:
                merged_list = list.append(list1.val)
                list1 = list1.next
            else: 
                merged_list.append(list2.val)
                list2 = list2.next
        while list2 != None:
            merged_list.append(list2.val)
            list2 = list2.next
    
        return merged_list
    
s = Solution()    
list1 = ListNode(1, ListNode(2, ListNode(4)))
list2 = ListNode(1, ListNode(3, ListNode(4)))

print(s.mergeTwoLists(list1,list2))