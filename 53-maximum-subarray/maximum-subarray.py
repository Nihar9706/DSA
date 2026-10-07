class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        max_sum = float('-inf')
        curr = 0

        for num in nums:
            curr += num
            if curr > max_sum:
                max_sum = curr
            if curr<0:
                curr=0
        return max_sum
        