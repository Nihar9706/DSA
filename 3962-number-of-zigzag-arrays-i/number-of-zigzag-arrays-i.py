class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7
        m = r - l + 1
        
        if n == 1:
            return m % MOD
            
        up = [0] * m
        down = [0] * m
        
        for v in range(m):
            up[v] = v
            down[v] = (m - 1) - v
            
        for length in range(3, n + 1):
            new_up = [0] * m
            new_down = [0] * m
            
            sum_down = 0
            for v in range(m):
                new_up[v] = sum_down
                sum_down = (sum_down + down[v]) % MOD
                
            sum_up = 0
            for v in range(m - 1, -1, -1):
                new_down[v] = sum_up
                sum_up = (sum_up + up[v]) % MOD
                
            up = new_up
            down = new_down
            
        return (sum(up) + sum(down)) % MOD