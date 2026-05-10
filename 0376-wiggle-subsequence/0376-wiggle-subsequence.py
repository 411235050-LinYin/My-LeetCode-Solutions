class Solution:
    def wiggleMaxLength(self, nums: list[int]) -> int:
        n = len(nums)
        if n < 2:
            return n
        
      
        prev_diff = 0
       
        result = 1
        
        for i in range(n - 1):
            curr_diff = nums[i + 1] - nums[i]
            
        
            if (prev_diff <= 0 and curr_diff > 0) or (prev_diff >= 0 and curr_diff < 0):
                result += 1
                
                prev_diff = curr_diff
                
        return result
        