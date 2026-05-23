from collections import deque, defaultdict

class Solution:
    def possibleBipartition(self, n: int, dislikes: list[list[int]]) -> bool:
        # 1. 建立鄰接表（不喜歡是雙向的）
        graph = defaultdict(list)
        for u, v in dislikes:
            graph[u].append(v)
            graph[v].append(u)
            
        # 2. 顏色紀錄陣列：0 表示未染色，1 是紅，-1 是藍
        # 節點是 1 到 n，所以陣列大小開 n + 1
        color = [0] * (n + 1)
        
        # 3. 因為圖可能不是連通的（可能分成好幾群不相干的人），
        # 我們必須遍歷每一個人，確保每個人都被染色到。
        for i in range(1, n + 1):
            if color[i] != 0: # 已經被別群人染色過了，跳過
                continue
                
            # 開始 BFS 染色
            queue = deque([i])
            color[i] = 1 # 起始點染成紅色
            
            while queue:
                curr = queue.popleft()
                
                for neighbor in graph[curr]:
                    # 如果鄰居還沒染色
                    if color[neighbor] == 0:
                        color[neighbor] = -color[curr] # 染成和 curr 相反的顏色 (1 變 -1, -1 變 1)
                        queue.append(neighbor)
                    # 如果鄰居已經有顏色，且跟自己一樣 -> 衝突！
                    elif color[neighbor] == color[curr]:
                        return False
                        
        return True