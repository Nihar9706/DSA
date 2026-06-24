class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        cnt=[0]*26

        n=len(s)

        for i in range(n):
            cnt[ord(s[i]) - ord('a')] += 1
            cnt[ord(t[i]) - ord('a')] -= 1
        
        return max(cnt) == 0



        