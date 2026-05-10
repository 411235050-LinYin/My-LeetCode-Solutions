class Solution:
    def rob(self, nums: list[int]) -> int:
   
        if len(nums) == 1:
            return nums[0]
        
      
        return max(self.rob_linear(nums[:-1]), self.rob_linear(nums[1:]))

    def rob_linear(self, nums: list[int]) -> int:
        prev_max = 0  
        curr_max = 0  
        
        for x in nums:
    
            temp = curr_max
            curr_max = max(curr_max, prev_max + x)
            prev_max = temp
            
        return curr_max