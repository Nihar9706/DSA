from typing import List

class Solution:
    def sumAndMultiply(self, s: str, q: List[List[int]]) -> List[int]:
        n = len(s)
        M = (10**9) + 7
        out = []
        
        # Precompute powers of 10 modulo M to shift the prefix later
        pow10 = [1] * (n + 1)
        for i in range(1, n + 1):
            pow10[i] = (pow10[i - 1] * 10) % M

        # Your prefix sum array for the digits
        pref = [0] * (n + 1)
        
        # New arrays to extract the number 'x' in O(1)
        cntN0 = [0] * (n + 1) 
        p = [0] * (n + 1)

        # Build all prefix arrays in a single pass
        for i in range(n):
            d = int(s[i])
            
            # Your exact logic for the sum
            pref[i+1] = pref[i] + d
            
            # Logic for building the number value
            if d > 0:
                cntN0[i+1] = cntN0[i] + 1
                p[i+1] = (p[i] * 10 + d) % M
            else:
                cntN0[i+1] = cntN0[i]
                p[i+1] = p[i]

        # Answer queries
        for l, r in q:
            # Your exact logic to get the sum
            summ = pref[r+1] - pref[l]
            
            # 1. Find how many non-zero digits are in this window
            n0 = cntN0[r+1] - cntN0[l]
            
            x = (p[r+1] - p[l] * pow10[n0]) % M
            
            ans = (x * summ) % M
            out.append(ans)

        return out