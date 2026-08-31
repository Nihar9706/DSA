class Solution:
    def firstUniqChar(self, s: str) -> int:
        count=Counter(s)
        for ch in s:
            if count.get(ch,0)==1:
                return s.index(ch)
        return -1
        