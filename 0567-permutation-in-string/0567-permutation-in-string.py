class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        if n1 > n2:
            return False
        
        # 使用長度為 26 的列表記錄 a-z 出現次數
        s1_count = [0] * 26
        win_count = [0] * 26
        
        # 初始化：將字元轉換為 0-25 的索引 (a -> 0, b -> 1...)
        def get_idx(char):
            return ord(char) - ord('a')
        
        # 記錄 s1 的字元分佈
        for char in s1:
            s1_count[get_idx(char)] += 1
            
        # 開始遍歷 s2 (擴增 window)
        for right in range(n2):
            # 將當前字元加入 window
            win_count[get_idx(s2[right])] += 1
            
            # 當 window 長度超過 s1 時，縮減左側 (移出 window)
            if right >= n1:
                left_char = s2[right - n1]
                win_count[get_idx(left_char)] -= 1
            
            # 比較當前 window 是否與 s1 的組成一致
            # Python 的 list 直接比較會逐一比對內容
            if s1_count == win_count:
                return True
                
        return False
        