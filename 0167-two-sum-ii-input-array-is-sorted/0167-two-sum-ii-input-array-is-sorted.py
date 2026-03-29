class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0
        end = len(numbers) - 1
        res = []
        while start < end:
            sum = numbers[start] + numbers[end]
            if target > sum:
                start+=1
            elif target < sum:
                end-=1
            else:
                return [start + 1, end + 1]
        