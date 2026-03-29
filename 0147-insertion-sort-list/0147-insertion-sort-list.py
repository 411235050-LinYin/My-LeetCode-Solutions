# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return head
        
        dummy = ListNode(0)
        dummy.next = head
        last_sorted = head # 已排序部分的最後一個節點
        curr = head.next   # 準備要插入的節點
        
        while curr:
            if last_sorted.val <= curr.val:
                # 剛好比最大的還大，直接往後移一位
                last_sorted = last_sorted.next
            else:
                # 比較小，才需要從頭找位置
                prev = dummy
                while prev.next.val <= curr.val:
                    prev = prev.next
                
                # 進行節點大搬家
                last_sorted.next = curr.next
                curr.next = prev.next
                prev.next = curr
                
            curr = last_sorted.next
            
        return dummy.next