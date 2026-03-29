from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def mergeSort(left: int, right: int):
            # Base Case: 當區間只有一個元素或無效時停止
            if left >= right:
                return
            
            # 1. Divide: 找到中間點
            mid = left + (right - left) // 2
            
            # 2. Conquer: 遞迴處理左半部與右半部
            mergeSort(left, mid)
            mergeSort(mid + 1, right)
            
            # 3. Merge: 合併兩個已排序的子陣列
            a, b = left, mid + 1
            merging = []
            
            # 比較兩邊指針指向的數值，誰小就先放進暫存陣列
            while a <= mid and b <= right:
                if nums[a] <= nums[b]: # 使用 <= 可維持排序穩定性
                    merging.append(nums[a])
                    a += 1
                else:
                    merging.append(nums[b])
                    b += 1
            
            # 如果左半部還有剩餘元素
            while a <= mid:
                merging.append(nums[a])
                a += 1
                
            # 如果右半部還有剩餘元素
            while b <= right:
                merging.append(nums[b])
                b += 1
            
            # 將排序好的結果寫回原陣列的對應區間
            nums[left : right + 1] = merging

        # 初始呼叫：處理整個陣列索引從 0 到 n-1
        mergeSort(0, len(nums) - 1)
        return nums