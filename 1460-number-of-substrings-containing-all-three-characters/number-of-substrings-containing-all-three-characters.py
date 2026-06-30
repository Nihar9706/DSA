class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        # Keep track of the most recent index where we saw 'a', 'b', and 'c'
        last_seen = {'a': -1, 'b': -1, 'c': -1}
        total_substrings = 0
        
        # Iterate through the string character by character
        for i, char in enumerate(s):
            # Update the last seen index for the current character
            last_seen[char] = i
            
            # Find the minimum index among the last seen positions of 'a', 'b', and 'c'
            min_idx = min(last_seen['a'], last_seen['b'], last_seen['c'])
            
            # If min_idx is -1, it means we haven't seen all three characters yet.
            # If we have seen all three, min_idx is the start of the shortest valid window ending at 'i'.
            # Any starting index from 0 up to min_idx will also form a valid substring ending at 'i'.
            # Therefore, we add (min_idx + 1) to our total.
            if min_idx != -1:
                total_substrings += (min_idx + 1)
                
        return total_substrings