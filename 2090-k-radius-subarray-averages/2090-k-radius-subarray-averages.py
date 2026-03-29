class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        window_size = 2 * k + 1
        res = [-1] * n
        
        # 邊界情況：如果窗口比陣列大，直接回傳全 -1 的陣列
        if n < window_size:
            return res
        
        # 1. 計算第一個窗口的總和 (0 到 2*k)
        current_window_sum = sum(nums[:window_size])
        res[k] = current_window_sum // window_size
        
        # 2. 開始滑動窗口
        # i 代表「即將進入窗口」的新元素索引
        for i in range(window_size, n):
            # 加上新元素，減去最左邊過期的元素
            current_window_sum += nums[i] - nums[i - window_size]
            
            # 更新中心點的平均值
            # 當右邊界在 i 時，中心點正好在 i - k
            res[i - k] = current_window_sum // window_size
            
        return res