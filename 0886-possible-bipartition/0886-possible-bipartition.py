from collections import deque, defaultdict

class Solution:
    def possibleBipartition(self, n: int, dislikes: list[list[int]]) -> bool:
        # 1. 建立鄰接表
        graph = defaultdict(list)
        for u, v in dislikes:
            graph[u].append(v)
            graph[v].append(u)
            
        
        color = [0] * (n + 1)
        
        
        for i in range(1, n + 1):
            if color[i] != 0: # 已經被別群人染色過了，跳過
                continue
                
            
            queue = deque([i])
            color[i] = 1 # 起始點染成紅色
            
            while queue:
                curr = queue.popleft()
                
                for neighbor in graph[curr]:
              
                    if color[neighbor] == 0:
                        color[neighbor] = -color[curr] # 染成和 curr 相反的顏色 (1 變 -1, -1 變 1)
                        queue.append(neighbor)
                 
                    elif color[neighbor] == color[curr]:
                        return False
                        
        return True