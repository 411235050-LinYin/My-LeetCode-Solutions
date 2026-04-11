from typing import List

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        # 1. 按照「去 A 比去 B 省多少錢」來排序
        # x[0] - x[1] 就是價差
        costs.sort(key=lambda x: x[0] - x[1])
        
        total_cost = 0
        n = len(costs) // 2
        
        # 2. 前半段 n 個人去 A
        for i in range(n):
            total_cost += costs[i][0]
            
        # 3. 後半段 n 個人去 B
        for i in range(n, 2 * n):
            total_cost += costs[i][1]
            
        return total_cost