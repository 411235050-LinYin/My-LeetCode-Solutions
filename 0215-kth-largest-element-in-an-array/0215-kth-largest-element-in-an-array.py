import heapq

class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        # 1. 先把前 k 個元素放進堆疊（建立一個大小為 k 的小頂堆）
        heap = nums[:k]
        heapq.heapify(heap)
        
        # 2. 遍歷剩下的元素
        for i in range(k, len(nums)):
            # 如果目前數字比堆疊裡最小的還大
            if nums[i] > heap[0]:
                # 踢掉最小的，把目前數字塞進去
                heapq.heapreplace(heap, nums[i])
        
        # 3. 堆疊頂端就是第 k 大的元素
        return heap[0]