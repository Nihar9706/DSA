class Solution:
    def isPalindrome(self, s: str) -> bool:
        l=0
        r=len(s)-1
        ans=""
        if len(s)<2:
            return True

        for ch in s:
            if ch.isalnum():
                ans+=ch
        return ans.lower()==ans[::-1].lower()
