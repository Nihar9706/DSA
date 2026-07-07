class Solution(object):
    def isSubsequence(self, s, t):

        i, j = 0, 0
        while i < len(s) and j < len(t):
        # If characters match, move the pointer of s forward
            if s[i] == t[j]:
                i += 1
        # Always move the pointer of t forward
            j += 1
    
        # If we have traversed all characters of s, return True
        return i == len(s)
            
        