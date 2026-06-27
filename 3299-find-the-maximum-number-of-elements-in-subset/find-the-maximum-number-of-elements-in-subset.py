class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        # Count the frequency of every number in the array
        counts = Counter(nums)
        
        # Every single element forms a valid pattern of length 1
        max_len = 1
        
        # Handle the special case for 1s
        if 1 in counts:
            ones = counts[1]
            # Pattern length must be odd. 
            # If we have an even number of 1s, we just leave one out.
            max_len = ones if ones % 2 == 1 else ones - 1
            
        # Check all other numbers to see how big of a mountain we can build
        for num in counts:
            if num == 1:
                continue # We already handled 1
            
            curr = num
            curr_len = 0
            
            # Build the sides of the mountain: we need at least 2 of the current number
            while counts[curr] > 1:
                curr_len += 2
                curr = curr * curr # Move to the next square
                
            # The loop breaks when we have 1 or 0 of the `curr` number.
            # If we have 1, it becomes the perfect peak!
            if counts[curr] > 0:
                curr_len += 1
            # If we have 0, it means the *previous* number had to be our peak.
            # We mistakenly counted 2 of the previous number in the loop, 
            # but a peak only requires 1, so we subtract 1 from our length.
            else:
                curr_len -= 1
                
            # Update our maximum length found so far
            max_len = max(max_len, curr_len)
            
        return max_len
        