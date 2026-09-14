class Solution:
    def isPalindrome(self, s: str) -> bool:
        ans=""
        for ch in s:
            if ch.isalnum():
                ans+=ch
        ans = ans.lower()
        return ans==ans[::-1]
        