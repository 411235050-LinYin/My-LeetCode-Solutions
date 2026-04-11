from typing import List
class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        # 先把亂數排序,醜死了>> O(nlogn)
        nums.sort()

        #抓有幾個元素in nums(list)
        n = len(nums)
        #一開始的差距值:
        ans = nums[n-1] - nums[0]

        #總之先開始跑起來!
        #?i同時是索引值 和 分界牆兩個腳色:
        #!開始移動「切割牆」 i
        # i 是左半邊 (+k組) 的最後一個索引
        # i + 1 是右半邊 (-k組) 的第一個索引
        for i in range(0,n-1): #小心跑出迴圈index值
           #當下最小值
           lower =  min(nums[0]+k,nums[i+1]-k)
           
           #當下最大值,根據題目敘述:當牆的那位也要被+k or -k調整
           higher = max(nums[i]+k,nums[n-1]-k)
           #找新的var記錄差距
           CurrentGap = higher-lower

           #更新每一輪答案(用當前暫時的差距和計算後的值做比較找最小值)
           ans = min(ans,CurrentGap)
        return ans
        #*計得最後返回答案return answer  